import os

import urllib3
import requests
from bs4 import BeautifulSoup
from pytumblr import TumblrRestClient

urllib3.disable_warnings()


client = TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
)


def download_save(url):
    filename = url.split('/')[-1]
    if os.path.exists(filename):
        print('SKIPPING {}, already have it'.format(filename))
        return
    file = requests.get(url, verify=False)
    open(filename, 'wb').write(file.content)

def process_page(posts):
    for idx, post in enumerate(posts):
        print('PROCESSING INDEX {} POST_ID {}'.format(idx, post.get('id')))
        if post['type'] == 'photo':
            for photo in post['photos']:
                url = photo['original_size']['url']
                download_save(url)
        elif post['type'] == 'text':
            try:
                html = BeautifulSoup(post['body'])
            except Exception as ex:
                print('ERROR: {}'.format(ex))
            
            if html.video:
                url = html.video.source.get('src')
                if url:
                    download_save(url)
            elif html.img:
                url = html.img.get('src')
                if url:
                    download_save(url)
        elif post['type'] == 'video':
            url = post.get('video_url')
            if url:
                download_save(url)
        else:
            print('{}: {}'.format(post['type'], idx))

def process_likes(starting_timestamp=None):
    if starting_timestamp:
        my_likes = client.likes(limit=42, before=starting_timestamp)
    else:
        my_likes = client.likes(limit=42)

    next_timestamp = my_likes['_links'].get('next', {}).get('query_params', {}).get('before', {})

    while next_timestamp:
        print('STARTING TIMESTAMP {}'.format(next_timestamp))
        process_page(my_likes['liked_posts'])
        next_timestamp = my_likes['_links'].get('next', {}).get('query_params', {}).get('before', {})
        my_likes = client.likes(limit=42, before=next_timestamp)
        print('NEXT TIMESTAMP {}'.format(next_timestamp))

def process_posts(blog_name):
    my_posts = client.posts(blogname=blog_name, limit=50)
    next_offset = my_posts.get('_links', {}).get('next', {}).get('query_params', {}).get('offset', {})

    while next_offset:
        print('STARTING OFFSET {}'.format(next_offset))
        process_page(my_posts['posts'])
        next_offset = my_posts.get('_links', {}).get('next', {}).get('query_params', {}).get('offset', {})
        my_posts =client.posts(blogname=blog_name, limit=50, offset=next_offset)
        print('NEXT OFFSET {}'.format(next_offset))


