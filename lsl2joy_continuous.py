
from pylsl import StreamInlet, resolve_stream
import uinput

# map output to angles, continuous

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
    # convert to angle, from -1,1 to 0, 255
    joy_angle = int((value + 1.) * (255/2))
    if joy_angle < 0:
        joy_angle = 0
    if joy_angle > 255:
        joy_angle = 255
    print "output angle:", joy_angle
    device.emit(uinput.ABS_X, joy_angle) 

    