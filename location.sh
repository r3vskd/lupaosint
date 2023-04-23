#!/bin/bash

echo 'Enter IP' | read ipaddr | whois ipaddr | grep 'City\|StateProv\|Country'
