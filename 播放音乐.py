import time
import pygame
# from mutagen.mp3 import MP3

path = "E:\\哆来咪"  # 路径
# sn = '\\s0.wav'
# 初始化
pygame.mixer.init()
with open(path + "\\大鱼.txt", 'r') as f:
    for line in f.readlines():
        for n in line:
            if n in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                sn = '\\s%s.wav' % n
                pygame.mixer.music.load(path + sn)
                pygame.mixer.music.play()
                time.sleep(0.4)

        time.sleep(0.5)
pygame.mixer.music.pause()
pygame.mixer.music.stop()

# 加载
# pygame.mixer.music.load(path + sn)

# 播放
# pygame.mixer.music.play()

# 获取MP3音频文件的时长
# audio = MP3(path+sn)
# print(audio.info.length)
# time.sleep(audio.info.length)
# time.sleep(0.5)
# 暂停
# pygame.mixer.music.pause()

# 停止
# pygame.mixer.music.stop()
