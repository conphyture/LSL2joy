Translate a LSL stream to keyboard events.

Tested with kubuntu 14.04.

Depends on LSL

* pip install pylsl --user

And on python-uinput

* sudo apt-get install libudev-dev
* pip install python-uinput --user

Make sure `uinput` module is loaded: `sudo modprobe uinput`. Run script with sudo for permissions.

# Test with OpenViBE

You may use the files in `ov_scenarios` folder to test the script in combination with OpenViBE. Tested with OpenViBE 1.0.1.

In case you're really into BCI and you'd want to use motor imagery paradigm (who knows ^^), some tunings are mantadory. To link classifier output to LSL output in openvibe: set `Designer_AllowUpCastConnection = True` in `~/.config/openvibe/openviberc` and use a "Matrix Transpose" box in-between.
