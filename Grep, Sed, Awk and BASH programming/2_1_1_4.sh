#!/bin/bash
cd /usr/share/dict/	
cat words | sed -ne '/.*aaa*.*/p'
