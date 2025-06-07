#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)  
next(reader) 

for row in reader:
    if len(row) > 2:  
        sentiment = row[2]  
        print(f"{sentiment}\t1")
