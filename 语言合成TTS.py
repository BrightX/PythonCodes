import win32com.client as wincl
from tkinter import *


def text2Speech():
    speak = wincl.Dispatch("SAPI.SpVoice")
    text = e.get()
    if ".txt" in text:
        with open(text, "r", encoding = "utf8") as f:
            print(text)
            print("OK  正在播放音频…")
            for line in f.readlines():
                print(line)
                speak.Speak(line)
    else:
        speak.Speak(text)

tts = Tk()
tts.wm_title("语音合成TTS")
tts.geometry("600x400")
tts.config(background = "#708090")

f = Frame(tts, height = 600, width = 800, bg = "#bebebe")
f.grid(row = 0, column = 0, padx = 10, pady = 5)
lbl = Label(f, text="输入需要转换的文本")
lbl.grid(row = 1, column = 0, padx = 10, pady = 2)
e = Entry(f, width = 80)
e.grid(row = 2, column = 0, padx = 10, pady = 2)
btn = Button(f, text="语音输出", command=text2Speech)
btn.grid(row = 3, column = 0, padx = 20, pady = 10)
tts.mainloop()
