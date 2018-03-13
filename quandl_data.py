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

#data = quandl.get('WIKI/AAPL', trim_start = '2000-12-12', trim_end = '2014-12-13',authtoken = auth_tok)
#
#print(data['Adj. Close'])

path_name = '/home/andreyb/sendtex/intraQuarter'

def Stock_Prices():
    df = pd.DataFrame()
    stats_path = path_name+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(stats_path)]
    
    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split('/')[-1]
            print(ticker)
            name = 'WIKI/'+ticker.upper()
            data = quandl.get(name, trim_start = '2000-12-12',
                              trim_end = '2014-12-13',
                              authtoken = auth_tok)
            data[ticker.upper()] = data['Adj. Close']
            df = pd.concat([df, data[ticker.upper()]], axis = 1)
        except Exception as e:
            print(str(e))
            time.sleep(10)
            try:
                ticker = each_dir.split('/')[-1]
                print(ticker)
                name = 'WIKI/'+ticker.upper()
                data = quandl.get(name, trim_start = '2000-12-12',
                                  trim_end = '2014-12-13',
                                  authtoken = auth_tok)
                data[ticker.upper()] = data['Adj. Close']
                df = pd.concat([df, data[ticker.upper()]], axis = 1)
                
            except Exception as e:
                print(str(e))
    df.to_csv('stock_prices.csv')
Stock_Prices()