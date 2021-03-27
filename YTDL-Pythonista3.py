from __future__ import unicode_literals
import youtube_dl
import os

import appex

DOWNLOAD_DIR = '~/Documents/Videos'

class MyLogger(object):

    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('ダウンロードに成功しました！')

def download_video(url):
    ydl_opts = {
        'outtmpl': DOWNLOAD_DIR + '/%(title)s.%(ext)s',
        'logger': MyLogger(),
        'progress_hooks': [my_hook]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        http://ydl.download([url])

def main():
    if not http://appex.is_running_extension():
        print('このコードは、共有から開く事を想定して構成されてます〜')
        return
    url = appex.get_url()
    if not url:
        print('うらるが見つからないよ！')
        return

    download_video(url)

if __name__ == '__main__':
    main()