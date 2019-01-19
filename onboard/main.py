import time
import timeit
import image_slicer
from PIL import Image

picName = "/tmp/capture.jpg"

# Given the image path, show it on the screen
def showImage(img):
    image = Image.open(img)
    image.show()
    time.sleep(1)

# Start VLC fullscreen vid
# subprocess.check_output(["vlc", "--fullscreen", "--loop", "./data/360p.mp4"])

# Get reference time
start = timeit.default_timer()

while True:
    curTime = timeit.default_timer()
    if curTime >= start + 4 and curTime <= start + 5:
        print("Sending frame 1")
        showImage('./data/1_01_01.png')
        showImage('./data/1_01_02.png')
        showImage('./data/1_02_01.png')
        showImage('./data/1_02_02.png')


    # Resets the clock once the video is done
    if curTime >= start + 20:
        print("Video Restart")
        start = timeit.default_timer()

    print(curTime)
    time.sleep(1)

