import json
import re
from urllib import request, parse
from QQ_music.util.url_util import UrlUtil


class QQMusicSpider:
    @staticmethod
    def run(song):
        html = QQMusicSpider.QQ_music_spider(song)
        mid = QQMusicSpider.get_music_id(html)
        url = UrlUtil.get_music_home(mid)
        print(url)
        return url

    @staticmethod
    def QQ_music_spider(song):
        # song = "告白气球 周杰伦"
        url_song = parse.quote(song)
        url = UrlUtil.get_client_search(url_song)
        req = request.Request(url=url)
        response = request.urlopen(req).read()
        html = response.decode("utf-8")
        # print(html)
        return html

    @staticmethod
    def get_music_id(html):
        result = re.match("[\w']*\(({[\w\W]*})\)", html).group(1)
        # print(result)
        data = json.loads(result, strict=False)
        mid = data['data']['song']['list'][00]['file']['media_mid']
        print(mid)
        return mid
