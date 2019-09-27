#!/usr/bin/python

import pyaudio
import wave
import sys
import resource
import time

chunk = 1024

RATE = 44100
CHANNELS = 2
FORMAT = pyaudio.paInt16

print "STREAM List:"
print "0. Exit program"
print "1. Planet Rock"
channel=raw_input("Enter number for channel: ")
today=time.strftime("%Y%m%d_%H%M")

if ( channel == "0" ):
  raise SystemExit
elif ( channel == "1" ):
  STREAM_URL = 'http://live-bauer-mz.sharp-stream.com/planetrock.aac?direct=true&amsparams=playerid:BMUK_html5;skey:1504037263;&awparams=loggedin:false'
  STREAM_NAME='Planet_Rock'
else:
  STREAM_URL = ''

import urllib2

# Content-Type: audio/aacp
f = urllib2.urlopen(STREAM_URL)

# # Pyaudio stream requires format conversion
# p = pyaudio.PyAudio()
# stream = p.open(format = FORMAT,
#                 channels = CHANNELS,
#                 rate = RATE,
#                 output = True)

# while True:
#     data = f.read(100)
#     stream.write(data)
# stream.close()

# Write raw data
# Note that metadata is included
outfile = open(today+"-"+STREAM_NAME+".dump","wb")
while True:
  data = f.read(100)
  outfile.write(data)
  

outfile.close()
p.terminate()
