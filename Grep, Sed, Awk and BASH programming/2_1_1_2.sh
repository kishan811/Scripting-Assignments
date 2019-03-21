#!/bin/bash
cd /usr/share/dict/
cat words | sed -nE '/^[aeiouAEIOU]/p' 
cat words | sed -nE '/^[aeiouAIEOU]/p'| wc -w
