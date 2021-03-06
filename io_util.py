import os

from entity import Song


class IOUtil:
    @staticmethod
    def read_conf():
        conf = {}
        file = open('configure.conf')
        for line in file:
            line = line.strip()
            if line[0:2] == "//":
                continue
            else:
                map = line.split('=')
                conf[map[0].strip()] = map[1].strip()
        file.close()
        # print(conf)
        return conf

    @staticmethod
    def read_song_list():
        song_list = []
        file = open('sing.txt', encoding='utf-8')
        for line in file:
            line = line.strip()
            if line == "":
                continue
            elif line[0:2] == "//":
                continue
            else:
                strs = line.split(" ")
                length = len(strs)
                song = Song()
                if length > 0:
                    song.song = strs[0].strip()
                if length > 1:
                    song.singer = strs[1].strip()
                if length > 2:
                    song.index = strs[2].strip()
                song_list.append(song)
        # print(song_list)
        return song_list

    @staticmethod
    def get_path():
        conf = IOUtil.read_conf()
        path = conf.get("path")
        if path is None:
            print("配置文件没有配置path路径，音乐默认保存到运行文件的文件夹下。")
            path = os.getcwd()
        else:
            if os.path.isdir(path) is not True:
                print("配置文件path路径不是文件夹，请检查路径是否正确。")
            else:
                print("获取到路径：" + path)
        return path
