
from gpiozero import LED, Button
from signal import pause
import urllib2

led =LED(17)
button = Button(2)

def ifttt():
	urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/oH66Ag4cn26KLekr2DRox_OiXwFENSg90j-cx1lxBEe£").read()

button.when_pressed = ifttt

pause()
