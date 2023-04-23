#!/bin/bash

# Ask user for URL to scrap
cd scrapper
read string
wget $string
# Use grep to find all lines with the search string and awk to print the 10 characters after the match
less index.html | grep -o -E "email.{0,33}" index.html | awk '{print substr($0, length("'"email"'")+1)}'
cd ..


#notes:
# To scrap for emails
#less index.html | grep -o -E "mail.{0,33}" | awk '{print substr($0, length("'"email"'")+#1)}' | head -1
# To srap phone numbers
#less index.html | grep -o -E "phone.{0,14}" | awk '{print substr($0, length("'"phone"'")+1)}' | egrep -o '[0-9.]+' | tr '\n,. ' ' '
