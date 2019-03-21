#!/bin/bash
cd /usr/share/dict/
cat words | grep -v "[A-Z]" | grep -E '^.....$|^..........$'



