import os
# result = os.popen("ipconfig")
# print(result.read)
# print(os.system('ipconfig'))
import win32com.client
import winsound
import time
# speak = win32com.client.Dispatch('SAPI.SPVOICE')
# # winsound.Beep(2015, 3000)
# speak.Speak('给你马两刀!')
os.system('给你马两刀.mp3')
import mp3play
def playmusic(path):
    clip = mp3play.load(path)
    clip.play()
    time.sleep(10)   
    clip.stop()
playmusic('给你马两刀.mp3')