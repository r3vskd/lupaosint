#!/bin/bash

# Ask user for URL to scrap
cd scrapper
read string
wget $string
# Use grep to find all lines with the search string and awk to print the 10 characters after the match
less index.html | grep -o -E "phone.{0,14}" | awk '{print substr($0, length("'"phone"'")+1)}' | egrep -o '[0-9.]+' | tr '\n,. ' ' '
