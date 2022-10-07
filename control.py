"""
Functions below drive our car
We initialize wheel value for right wheel (wR) and left wheel (wL)
read data in this file or another file?
Initilize values to read data with right sesnor (sR) adn left sensor (sL)
Takes data and gives car wheels the values it needs to drive
"""
import pyfirmata
from pyfirmata import Arduino #imports Arduino
board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

sR = board.get_pin('d:10:i') #inputs from board. change ports when needed.
sL = board.get_pin('d:13:o') #inputs from board. change ports when needed.

mRight = board.get_pin('d:13:o')#need to change the pins
mLeft = board.get_pin('d:13:o')#need to change the pins

wR = 0
wL = 0

go = 1

while go == 1: #while true
    if sR < 0.5 and sL < 0.5:
        wR = 1
        wL = 1
    elif sR > 0.5 and sL < 0.5:
        wR = 0.3
        wL = 1
    elif sR < 0.5 and sL > 0.5:
        wR = 1
        wL = 0.3

    mRight.write(wR)
    mLeft.write(wL)