
from pylsl import StreamInlet, resolve_stream
import uinput

# stream name of classifier output in openvibe
stream_name = "hyperplane"

# rough prototype, we'll use a simple threshold for now
threshold = 0.1

# one virtual keyboard
device = uinput.Device([
        uinput.KEY_LEFT,
        uinput.KEY_RIGHT,
        ])

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
      device.emit_click(uinput.KEY_LEFT)
    if value >= threshold:
      print "right"
      device.emit_click(uinput.KEY_RIGHT)
    