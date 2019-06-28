#!/usr/bin/python
import sys
import time
import difflib
import pigpio
RX=20
TX=21
try:
    pi = pigpio.pi()
    pi.set_mode(RX, pigpio.INPUT)
    pi.set_mode(TX, pigpio.OUTPUT)
    pi.bb_serial_read_open(RX, 4800, 8)
    pi.set_pull_up_down(23, pigpio.PUD_DOWN)
    print(pi.read(23))
    0
    pi.set_pull_up_down(23, pigpio.PUD_UP)
    print(pi.read(23))
    1
except:
    pi.bb_serial_read_close(RX)
    pi.stop()