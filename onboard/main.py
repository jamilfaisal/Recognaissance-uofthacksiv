import subprocess
import time

picName = "/tmp/capture.jpg"

while True:
    res = subprocess.check_output(["sh", "./takepic.sh", picName])
    time.sleep(1)