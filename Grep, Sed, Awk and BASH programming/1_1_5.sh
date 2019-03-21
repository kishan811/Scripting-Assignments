#!/bin/bash
cd /usr/share/dict/
cat words | grep -E '[[:punct:]]'
