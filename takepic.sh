unamestr=`uname`
fname=$1
if [[ "$unamestr" == 'Linux' ]]; then
   fswebcam -d /dev/video2 -r 1280x720 $fname
else
   imagesnap $fname
fi