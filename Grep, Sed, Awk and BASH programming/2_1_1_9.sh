#!/bin/bash
cd /usr/share/dict/
cat words | sed -nE '/^(.).*(\1)$|^.$/p'



