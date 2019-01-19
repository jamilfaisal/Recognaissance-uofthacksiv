import time
import timeit
import image_slicer
import requests

# Given the prefix of the filename, upload the images to the other server
def uploadImages(pre, lat, long):
    try:
        for x in range(1, 3):
            for y in range(1, 3):
                with open('./data/' + pre + '_0' + str(x) + '_0' + str(y) + '.png', 'rb') as f:
                    multipart_form_data = {
                        'img.jpg': ('img.jpg', f),
                        'lat': (None, str(lat)),
                        'long': (None, str(long))
                    }
                    r = requests.post('http://a4c94c54.ngrok.io/upload', files=multipart_form_data)
                    print(r.text)
    except Exception as e:
        print(str(curTime) + " - UPLOAD FAILURE - " + str(e))

# Get reference time
start = timeit.default_timer()

while True:
    curTime = timeit.default_timer()
    if curTime >= start + 4 and curTime <= start + 6:
        print(str(curTime) + " - sending image for processing FR1")
        image_slicer.slice('./data/1.jpg', 9)
        uploadImages("1", 100, 101)


    # Resets the clock once the video is done
    if curTime >= start + 20:
        print(str(curTime) + " - RESETTING")
        start = timeit.default_timer()

    print(str(curTime) + " - sending image for processing")
    time.sleep(2)

