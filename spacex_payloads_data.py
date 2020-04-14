#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:03:12 2020

@author: renan
"""


import matplotlib.ticker as tck
import numpy as np
import matplotlib.pyplot as plt
import requests
from pandas import DataFrame
api_url = 'https://api.spacexdata.com/v3/payloads'

req_url = requests.get(api_url)

if req_url.status_code == 200:

    dados = req_url.json()

payload_ =[]
class payload():
    def __init__(self,payload_id,reused):#,manufacturer,nationality,payload_type):#,payload_mass_kg):
        self.payload_id = payload_id
        self.reused = reused
#        self.manufacturer = manufacturer
#        self.nationality = nationality
#        self.payload_type = payload_type
#        self.payload_mass_kg = payload_mass_kg 
        
           
       
for i in range(0,len(dados),1):
    payload_.append(i)
   
for i in range(0,len(dados),1):    
    payload_id = dados[i]['payload_id']
    reused = dados[i]['reused']
#    manufacturer = dados[i]['manufacturer'] #consertar a aquisição de dados daqui pra baixo
#    nationality = dados[i]['nationality']
#    payload_type = dados[i]['payload_type']
#    payload_mass_kg = dados[i]['payload_mass_kg']
    

    
    if i<(len(dados)+1):  
        payload_[i] = payload(payload_id,reused)#,manufacturer,nationality,payload_type)#,payload_mass_kg)
        
reused_payload=[]    
notreused_payload=[]
      
for i in range (0,len(payload_),1):
    if payload_[i].reused == True: 
        reused_payload.append(payload_[i].payload_id)
    if payload_[i].reused == False:
        notreused_payload.append(payload_[i].payload_id)
#-----------------------------------------------------------------------------------------------------------
#for i in range(0,len(dados),1):
        
df =DataFrame(list(dados[i].items()),columns = ['coluna 1','coluna 2']) 
print(df.head())        