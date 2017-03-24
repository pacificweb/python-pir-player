#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import logging
import os
import time
import subprocess
from gpiozero import MotionSensor
from datetime import datetime

log = logging.getLogger(__name__)

class MotionLogic:

    def __init__(self, pin):

        # Detecteur de mouvement
        self.Sensor = MotionSensor(pin)

    def Dispose(self):
        del self.Sensor

	# Sensor -----------------------------------------
    def StartSensor(self):
        self.Sensor.when_motion = self.OnMotionStart
        self.Sensor.when_no_motion = self.OnMotionStop

	# Sensor Events
    def OnMotionStart(self):
        log.info("OnMotionStart")
	
    def OnMotionStop(self):
        log.info("OnMotionStop")
	# Sensor -----------------------------------------

##################################################################################################################################################

def main(args=None):

    logging.basicConfig(filename='pir-player.log',datefmt='%Y-%m-%d %I:%M:%S',format='%(levelname)s : %(asctime)s %(message)s',level=logging.DEBUG)

    logic = MotionLogic(7)
    logic.StartSensor()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt):
        print('exit(0)')
    finally:
        logic.Dispose()
        del logic
        log.info("Shutdown")
        sys.exit()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
