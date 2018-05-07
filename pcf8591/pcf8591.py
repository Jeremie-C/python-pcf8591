#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smbus
# PCF8591 default
DEVICE = 0x48
# Mode 00 : 4 single-endend inputs
AIN0 = 0x40
AIN1 = 0x41
AIN2 = 0x42
AIN3 = 0x43
# Mode 11 : Two differential inputs
DIF0 = 0x70
DIF1 = 0x71
# Mode 01 : Three differential inputs
TDIF0 = 0x50
TDIF1 = 0x51
TDIF2 = 0x52
# Mode 10 : Single-endend and one differential
SIN0 = 0x60
SIN1 = 0x61
DIF2 = 0x62

# Classe
class PCF8591:
    def __init__(self, i2cbus=1, device_address=DEVICE):
        self.bus = smbus.SMBus(i2cbus)
        self.adr = device_address

    def read(self, chan):
        # Channel
        if chan not in [AIN0, AIN1, AIN2, AIN3, DIF0, DIF1, DIF2, TDIF0, TDIF1, TDIF2, SIN0, SIN1]:
            raise ValueError('Unexpected chan value {0}.'.format(chan))
        # Read
        self.bus.write_byte(self.adr, chan)
        self.bus.read_byte(self.adr)
        return self.bus.read_byte(self.adr)

    def write(self, val):
        try:
            val = int(val)
            self.bus.write_byte_data(self.adr, 0x40, val)
        except Exception, e:
            print "Error: Device address: 0x%2X" % self.adr
            print e
