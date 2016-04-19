
from pylsl import StreamInlet, resolve_stream
import pyautogui

# stream name of classifier output in openvibe
stream_name = "hyperplane"

# rough prototype, we'll use a simple threshold for now
threshold = 0.1

# first resolve an EEG stream on the lab network
print("looking for LSL stream named [" + stream_name +"]")
streams = resolve_stream('name', stream_name)

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

print("got it")

while True:
    # get a new sample
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)
    # retrieve first channel
    value = sample[0]
    if value <= -threshold:
      print "left"
      pyautogui.press('left')
    if value >= threshold:
      print "right"
      pyautogui.press('right')
    