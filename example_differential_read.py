#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcf8591
import time

pcf = pcf8591.PCF8591()

while True:
    val = pcf.read(pcf8591.DIF0)
    print(val)
    time.sleep(0.5)
