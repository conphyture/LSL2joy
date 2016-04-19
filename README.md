Translate a LSL stream to keyboard events.

Depends on LSL

* pip install pylsl --user

And on python-uinput

* sudo apt-get install libudev-dev
* pip install python-uinput --user

Make sure `uinput` module is loaded: `sudo modprobe uinput`. Run script with sudo for permissions.

To link classifier output to LSL output in openvibe: set `` in `~/.config/openvibe/openviberc` and use a "Matrix Transpose" box in-between.
