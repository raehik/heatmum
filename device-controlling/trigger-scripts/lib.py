#!/usr/bin/env python
import energenie

def set_socket(num, state):
    if state == True:
        energenie.Devices.ENER002(num).turn_on()
    else:
        energenie.Devices.ENER002(num).turn_off()

def energenie_main(f):
    energenie.init()
    try:
        f()
    finally:
        energenie.finished()
