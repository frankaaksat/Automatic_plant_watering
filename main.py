#import the functions from water_pump.py and water_sensoring.py
import numpy
import time


#Main file to drive the code




#This value might change, threeshold value for when watering the plant
dry = 50

while True:
    #function monitoring the moisture output

    if monitoring <= dry:
        activate pump 

    #monitors every hour
    time.sleep(60*60)
