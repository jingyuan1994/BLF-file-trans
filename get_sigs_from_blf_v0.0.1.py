## BLF file trans
# Version: 0.0.1
# Author: Jingyuan Jiang
# E-mail: jingyuan.jiang@faw-vw.com
# Orgnization: FAW-Volkswagen E-Antrieb
# Project: Get special singial(s)'s value from .blf file
# Date: 2020-06-16
# Description: This script could be used as reference for transform the data from .blf file by dbc
#              via Python

## import the library
import can
import cantools
import csv
from pprint import pprint
import numpy

ist = []
soll = []
D1 = []
D2 = []
t1 = []
t2 = []

## dbc load
db = cantools.db.load_file('HCAN_KMatrix.dbc')
## blf read
can_log = can.BLFReader('20200527_PVS_V1.blf')

## sellect and decode msg
for msg in can_log:
  # msg1 id filter
  if msg.arbitration_id == 152:

    t1.append(msg.timestamp) # time recode
    D1 = db.decode_message('EM', msg.data)
    ist.append(D1['IstMoment']) # value recode

  # msg2 id filter
  if msg.arbitration_id == 144:

    t2.append(msg.timestamp)
    D2 = db.decode_message('MSG', msg.data)
    soll.append(D2['SollMoment'])

## reset the matrix
Data = list(zip(t2,soll,t1,ist))

## write in csvfile
with open("outputV2.csv", "w", newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(Data)
  csvfile.close()