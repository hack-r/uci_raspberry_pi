# these are code blocks / notes; this is not a runnable file

~~~~~~~~~~~~~~
from alchemyapi import AlchemyAPI

demo_html = '<html><body>AlchemyAPI works on HTML </body></html>'

response = alchemyapi.sentiment('html',demo_html)

if 'score' in response['docSentiment']:
     print('score: ', response['docSentiment']['score'])

~~~~~~~~~~~~~~
pip install twython # currrently python 3.x version is broken, but I opened a GitHub ticket
~~~~~~~~~~~~~~~~~~~
from twython import Twython

C_KEY =  ""
C_SECRET = ""
A_TOKEN = "-"
A_SECRET = ""

api = Twython(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

api.update_status(status="Hello World")

~~~~~~~~~~~~~~~~~~~

# TwythonStreamer allows you to examine public streams, e.g. stream.statuses.filter(track='Harris')

# on_success() is a callback; called when a tweet is found matching your search criteria
~~~~~~~~~~~~~~~~~~~

class MyStreamer(TwythonStreamer):
     def on_success(self, data):
         if 'text' in data:
              print("Found it.")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track = "Harris")

def blink():
     GPIO.output(13, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(13, GPIO.LOW)

class MyStreamer(TwythonStreamer):
     def on_success(self, data):
         if 'text' in data:
              blink()

~~~~~~~~~~~~~~~~~~~
from twython import TwythonStreamer

C_KEY =  ""
C_SECRET = ""
A_TOKEN = "-"
A_SECRET = ""

class MyStreamer(TwythonStreamer):
     def on_success(self, data):
         if 'text' in data:
              print("Got it.")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="pibot_iot_test")


