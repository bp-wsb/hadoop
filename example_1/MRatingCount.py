#!/usr/bin/env python
"""mapper.py"""

# The structure of the input dataset
# HName         = Hotel Name
# HStar         = Star category of hotel
# HRooms        = Number of rooms in the hotel
# UCountry      = User Country
# NrReviews     = Number of reviews 
# rating        = Average rating by the user
# StayPeriod    = Period of Stay
# TType         = Traveller Type
# Pool          = Hotel Has Pool?
# Gym           = Hotel Has Gym?
# TCourt        = Hotel Has Tennis Court?
# Spa           = Hotel Has Spa?
# Casino        = Hotel Has Casino?
# Internet      = Hotel Has Free Internet?
# UContinent    = Users Continent
# ReviewMonth   = Month of Review
# ReviewDay     = Day of the review
 
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

# read the data and split the line by tab 
    HName, HStar, HRooms, UCountry, NrReviews, rating, \
    StayPeriod, TType, Pool, Gym, TCourt, Spa, Casino, \
    Internet, UContinent, ReviewMonth, ReviewDay = line.split("\t")

# Create the rating and count key-value pair
    rating_result = [rating, "1"]

# Print the result to the STDOUT
    print ("\t".join(rating_result))
