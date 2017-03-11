#! /usr/bin/python

# Simple random card webpage
# Extract c.zip before use

# Import Random Functions
import random

# Generate Random Number 
num = str(random.randrange(0,67))

# Allow HTML output
print ("Content-type: text/html\n\n")

# Print page with image related to randomnumber
print ("<html><body style='background-color: black; text-align: center; color: white;'><a href='rcard.py'><img src='c/ (%s).png'></a><p>Click on image to generate new card</p></body></html>" % num)
