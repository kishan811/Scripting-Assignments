#!/bin/bash
cd /usr/share/dict/
cat words | grep -iE '^(.).*(\1)$|^.$'



