# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:10:09 2021

@author: Nelly
"""


import pandas as pd
import numpy as np
import math
import re
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from surprise import Reader, Dataset, SVD


### import coordinates

df = pd.read_csv('ferdige_soner.csv', encoding ='ISO-8859-1')
samlede_koodinater = pd.read_csv('Koordinater arter.csv', encoding ='ISO-8859-1')
#samlede_koodinater = samlede_koodinater['Samlede_koordinater']  #kun beholde en kolonne

all_kor = pd.merge(df, samlede_koodinater, how='left')
nye_koordinater = all_kor.iloc[:, 0:7].copy()



## check types

nye_koordinater.columns
nye_koordinater['nordkoordinat']
nye_koordinater['Østkoordinat']


## 
## needs to make prob for plants in area 


## koodinattelling 
koordinat_telling = nye_koordinater()








