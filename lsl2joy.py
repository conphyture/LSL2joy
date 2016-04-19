
from pylsl import StreamInlet, resolve_stream
import uinput

# stream name of classifier output in openvibe
stream_name = "hyperplane"

# rough prototype, we'll use a simple threshold for now
threshold = 0.3

# one virtual joystick
events = (
    uinput.BTN_JOYSTICK,
    uinput.ABS_X + (0, 255, 0, 0),
    uinput.ABS_Y + (0, 255, 0, 0),
    )
device = uinput.Device(events)

# center
device.emit(uinput.ABS_X, 128)
device.emit(uinput.ABS_Y, 128)
  
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
      device.emit(uinput.ABS_X, 0) 
    elif value >= threshold:
      print "right"
      device.emit(uinput.ABS_X, 255)
    else:
      print "center"
      device.emit(uinput.ABS_X, 128) 

    