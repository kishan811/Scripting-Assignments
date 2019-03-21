#!/bin/bash
sed -n -E 's/(.*),(.*),(.*),(.*),(..\/..\/..8[0-9])(.*)/\1/p' address-book.csv | wc -l
