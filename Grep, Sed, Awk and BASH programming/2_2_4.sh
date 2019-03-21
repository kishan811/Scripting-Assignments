#!/bin/bash
sed -e 's/[[:punct:]]/*/g' -e 's/[0-9]/?/g' address-book.csv