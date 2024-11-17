from future import *

sw = 0
leds = 0


sw = 0
leds = 0
screen.sync = 0
screen.clear()
screen.loadPng('tree.png',0,0)
screen.text('Merry Christmas',10,117,1,(0, 0, 255))
screen.refresh()
neopix=NeoPixel('P7',3)
while True:
  if sensor.btnValue('a'):
    neopix=NeoPixel('P7',3)
    leds = 1
  if sensor.btnValue('b'):
    neopix.setColorAll((0,0,0))
    leds = 0
  if sw == 0:
    sw = 1
    if leds == 1:
      neopix.setColor(0, (0, 255, 0))
      neopix.setColor(1, (255, 0, 0))
      neopix.setColor(2, (0, 255, 0))
      neopix.update()
  else:
    sw = 0
    if leds == 1:
      neopix.setColor(0, (255, 0, 0))
      neopix.setColor(1, (0, 255, 0))
      neopix.setColor(2, (255, 0, 0))
      neopix.update()
  sleep(1)
