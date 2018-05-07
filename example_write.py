#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcf8591
import time

pcf = pcf8591.PCF8591()
val = 0

while True:
    pcf.write(val)
    val += 1
    if val == 256:
        val = 0
    print("Analog OUT :%3d" %val)
    time.sleep(0.05)
