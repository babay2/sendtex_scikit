#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:04:07 2018

@author: andreyb
"""

import pandas as pd
import os
import quandl
import time

auth_tok = open('save.txt', 'r').read()
data = quandl.get('WIKI/AAPL', trim_start = '2000-12-12', trim_end = '2014-12-13',authtoken = auth_tok)

print(data)
