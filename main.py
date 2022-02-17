#import the functions from water_pump.py and water_sensoring.py
from msilib.schema import PublishComponent
import numpy
import time


#Main file to drive the code


while True:
    #function monitoring the moisture

    if monitoring == dry:
        activate pump 
        
    time.sleep(60*60)
