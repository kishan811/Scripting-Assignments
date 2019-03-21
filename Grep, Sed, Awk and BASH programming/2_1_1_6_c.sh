#!/bin/bash
cd /usr/share/dict/
cat words | sed -ne  "/[A-Z.*]/p" 