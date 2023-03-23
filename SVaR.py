# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:41:14 2023

@author: ndumasw1
"""

#Importing necessary modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading input file
FX = pd.read_excel("Input.xlsx")


# 1)Calculate 10 day returns
# 2)Multiply by risk i.e. FX delta in this case

FX['daily_return'] = (FX['USDTRY']/FX['USDTRY'].shift(-10)) - 1 
FX['PnL'] = FX['daily_return'] * -1000000 

# Remove the last 10 rows as not required 
FX.drop(FX.tail(10).index, inplace = True) 

#Sort PnL ascending
FX.sort_values(by=['PnL'], ascending=True, inplace=True)

# Isolating 99% confidence interval, which is 98% expected shortfall

FX['Driver Date'] = FX['Date'].head(5)

FX['VaR Tail'] = FX['PnL'].head(5)

SVaR = (FX['VaR Tail']).mean()

print(SVaR)

FX.to_excel("Output.xlsx")
