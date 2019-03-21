#!/bin/bash
cd /usr/share/dict/
cat words | grep -iE '^[aeiou].*[aeiou]$'
