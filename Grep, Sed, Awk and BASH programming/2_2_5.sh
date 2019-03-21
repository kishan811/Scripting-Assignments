#!/bin/bash
echo "Names after Swap:-"
sed -E 's/(.*),(.*),(.*),(.*),(.*),(.*)/\2 : \1/g' address-book.csv
