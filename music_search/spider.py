'''
通过urllib请求
'''
import json
import os
from urllib import request, parse

from io_util import IOUtil
from music_search.header import Header


class MusicSearchSpider:
    @staticmethod
    def music_search_spider(song_url):
        url = u"http://www.guqiankun.com/tools/music/"
        post_data = {u'input': song_url,
                     u'filter': u'url',
                     u'type': u'_',
                     u'page': u'1'}
        headers = {u'X-Requested-With': Header.x_requested_with}
        data = parse.urlencode(post_data).encode('utf-8')
        req = request.Request(url=url, headers=headers, data=data)
        response = request.urlopen(req).read()
        html = response.decode('gbk')

        url2, singer, title = MusicSearchSpider.parse(html)

        if url2 is None:
            print(title + ": 获取下载连接失败。")
            return
        req = request.Request(url2)
        response = request.urlopen(req).read()
        music = response
        print(title + ': 下载完毕:')
        music_name = singer + ' - ' + title + '.mp3'
        MusicSearchSpider.save_music(music, music_name)

    @staticmethod
    def parse(data_str):
        data = json.loads(data_str, strict=False)
        music_msg = data['data'][0]
        url = music_msg['url']
        singer = music_msg['author']
        title = music_msg['title']
        print(singer + " " + title)
        # print(url)
        return url, singer, title

    @staticmethod
    def save_music(music, music_name):
        path = IOUtil.get_path()
        f = open(path + '/' + music_name, "wb")
        f.write(music)
        f.close()
        print('保存完毕：' + music_name + ' ' + path)
