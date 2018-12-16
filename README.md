# Tumblr OUT

A quick and dirty script to download your favorite Tumblr site contents before they shut down.

## Requirements
* A little knowledge about how to edit files and run things in a terminal.
* A Tumblr account
* [Create an app](https://www.tumblr.com/oauth/apps)
* Then get the rest of your [OAuth credentials](https://api.tumblr.com/console/calls/user/info)
* Python 2.7+
* The requirements from this repository installed. `pip install -r requirements.txt`

## Set up
1. Clone this repository
2. Edit tumblr_download.py
3. Input the four credentials

## Downloading
There's two main functions here. One for downloading all the media from your likes, and another to download all the media from your own blog posts.

To download your likes:
1. Open a terminal and navigate to where you cloned this repository.
2. Open a python shell
3. `import tumblr_download`
4. `tumblr_download.process_likes()`
5. If the process fails for any reason, note the last `STARTING TIMESTAMP` from your terminal output, then run `tumblr_download.process_likes(starting_timestamp=<STARTING TIMESTAMP>)`

To download all the posts from a blog:
1. Open a terminal and navigate to where you cloned this repository.
2. Open a python shell
3. `import tumblr_download`
4. `tumblr_download.process_posts(<tumblr url:something.tumblr.com>)`
