#!/usr/bin/env python
"""reducer.py"""

# reducer to read and process the data
 
import sys

# initialize and define the variables
current_rating = 0
current_count = 0
rating = 0

# input comes from STDIN (standard input)
for line in sys.stdin:

# remove any spaces or blanks
    line = line.strip()
   
# read the rating and count delimited by tab
    rating, count = line.split("\t")
    count = int(count)

# Check if the rating has changed in the sorted stream of data
    if current_rating == rating:
        current_count += count
    else:
        if current_rating:
            print (current_rating,current_count)
        current_count = count
        current_rating = rating

# print the last rating count
if current_rating == rating:
     print (current_rating,current_count)
