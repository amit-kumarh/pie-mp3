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
sR = board.get_pin('d:13:o') #inputs from board. change ports when needed.



wR = 0
wL = 0


