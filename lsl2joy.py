
from pylsl import StreamInlet, resolve_stream
import uinput, time

# map output to angles, continuous

# how many seconds without samples should we wait before we timeout?
LSL_DECO_TIMEOUT=2

# we are not doing blocking call for LSL, but we don't want to use too much CPU either. Warning: if lower than input frequency, missed samples and/or shift will occur.
LSL_MAX_FREQ=1024

# rough prototype, we'll use a simple threshold for now
threshold = 0.3

# stream name of classifier output in openvibe
stream_name = "hyperplane"

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

inlet = None

# used to (re)connect to LSL
def lookout_stream():
    # first resolve an EEG stream on the lab network
    print("looking for LSL stream named [" + stream_name +"]")
    streams = resolve_stream('name', stream_name)

    # create a new inlet to read from the stream
    print("got it")
    return StreamInlet(streams[0])  

while True:
    # connect / reco. NB: blocking call until one stream is found
    if inlet == None:
        inlet = lookout_stream()
        # init lsl for timeout detection
        last_sample = time.time()
        
    # get a new sample
    try:
        sample, timestamp = inlet.pull_sample(0)
       
    except:
        print "disconnected"
        inlet = None
        continue
    else:
        # check for time out and loop over if no sample
        if not sample:
            # let stream go and loop over if reached timeout
            time_since_last_sample = time.time() - last_sample
            if time_since_last_sample > LSL_DECO_TIMEOUT:
                print "time out"
                inlet = None
            # loop no matter what
            continue
        else:
            last_sample = time.time()
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

    