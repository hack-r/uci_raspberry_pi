~~~~~~~~~~~~~~~~~~~~~
https://www.raspberrypi.org/help/camera-module-setup/

https://www.raspberrypi.org/documentation/usage/camera/README.md

https://www.raspberrypi.org/documentation/usage/camera/python/README.md

~~~~~~~~~~~~~~~~~~~~~~

sudo raspi-config
Select Enable Camera, Finish

sudo apt-get update
sudo apt-get install python3-picamera
~~~~~~~~~~~~~~~~~~~~~~
import picamera
camera = picamera.PiCamera()

camera.capture("pict.jpg") # take a picture

camera.hflip = T
camera.vflip = T
camera.brightness = 50
camera.sharpness = 0

# view video on RPi screen
camera.start_preview()
camera.stop_preview()

~~~~~~~~~~~~~~~~~~~~~~

mysocket = socket.socket()
mysocket.connect(('aserver', 8000))
conn = mysocket.makefile('wb')
camera.capture(conn,'jpeg')

# wb = write bytes

    ~~~~~~~~~~~~~~~~~~~~~~

# timelapse photography

camera.capture_continuous("picture{counter}.jpg")

# {counter} or {timestamp} can be substituted
~~~~~~~~~~~~~~~~~~~~~~

camera = picamera.PiCamera()
     for filename in
     camera.capture_continuous('img{counter}.jpg'):
         time.sleep(300)

~~~~~~~~~~~~~~~~~~~~~~
