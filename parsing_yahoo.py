#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:55:38 2018

@author: andreyb
"""

import urllib.request
import os
import time

path = '/home/andreyb/sendtex/intraQuarter'

def Check_Yahoo():
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    
    for ticker in stock_list[1:]:
        try:
            ticker = ticker.replace('/home/andreyb/sendtex/intraQuarter/_KeyStats/', '')
            link = 'https://finance.yahoo.com/quote/'+ticker.upper()+'/key-statistics?p='
            resp = urllib.request.urlopen(link).read()
            save = 'forward/' + str(ticker) + '.html'
            store = open(save, 'w')
            store.write(str(resp))
            store.close()
        except Exception as e:
            print(str(e), ticker)
            
Check_Yahoo()
