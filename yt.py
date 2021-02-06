import os
import time
path = "/sdcard/"
try:
    import pafy
    import pyfiglet
    import termcolor
except ImportError:
    os.system("pip install youtube-dl")
    os.system("pip install pafy")
    os.system("pip install pyfiglet")
    os.system("pip install termcolor")
    os.system("clear")
    import pafy
    import pyfiglet
    import termcolor

os.system('clear')
toolName = termcolor.colored(pyfiglet.figlet_format("YOUTUBE"),color="green")

print(toolName)
print("Dowloader YT Kualitas HD")
random_video ="https://youtu.be/lTTajzrSkCw"


url = input("Link Video Youtube: ")
try:
    video = pafy.new(url)
except ValueError:
    print("Link Salah, Mendownloads Video Random")
    url = random_video
    video = pafy.new(url)
bestVideoQuality = video.getbest()
bestVideoQuality.download(path)
print("done")
time.sleep(1)
print("Tersimpan Di /storage/")
