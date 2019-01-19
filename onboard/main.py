import time
import timeit
import image_slicer
import requests

# Given the prefix of the filename, upload the images to the other server
def uploadImages(pre):
    try:
        for x in range(1, 4):
            for y in range(1, 4):
                with open('./data/' + pre + '_0' + str(x) + '_0' + str(y) + '.png', 'rb') as f:
                    requests.post('http://demo0328641.mockable.io/upload', files={'img.jpg': f})
    except Exception as e:
        print(str(curTime) + " - UPLOAD FAILURE - " + str(e))


# Start VLC fullscreen vid
# subprocess.check_output(["vlc", "--fullscreen", "--loop", "./data/360p.mp4"])

# Get reference time
start = timeit.default_timer()

while True:
    curTime = timeit.default_timer()
    if curTime >= start + 4 and curTime <= start + 6:
        print(str(curTime) + " - sending image for processing FR1")
        image_slicer.slice('./data/1.jpg', 9)
        uploadImages("1")


    # Resets the clock once the video is done
    if curTime >= start + 20:
        print(str(curTime) + " - RESETTING")
        start = timeit.default_timer()

    print(str(curTime) + " - sending image for processing")
    time.sleep(2)

