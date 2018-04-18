import threading

from QQ_music.spider import QQMusicSpider
from io_util import IOUtil
from music_search.spider import MusicSearchSpider

song_list = IOUtil.read_song_list()

for song in song_list:
    str = song.song + ' ' + song.singer
    music_url = QQMusicSpider.run(str)
    # MusicSearchSpider.music_search_spider(music_url)
    t = threading.Thread(target=MusicSearchSpider.music_search_spider, args=(music_url,))
    t.start()



