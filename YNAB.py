#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import sys

with open(sys.argv[1], 'rt') as input_file:
    reader = csv.reader(input_file, delimiter=',', quotechar='"')
    for row in reader:
        str = row[0]
        print(str.replace("AMSTERDAM", "POOP"))
