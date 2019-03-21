#!/bin/bash
cd /usr/share/dict/
cat words | grep -iE '^[aeiou]'
cat words | grep -iE '^[aeiou]'| wc -w
