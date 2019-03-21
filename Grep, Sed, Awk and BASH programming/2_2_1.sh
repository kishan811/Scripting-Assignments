#!/bin/bash
sed -n -E 's/(.*),(.*),(.*),(Anycity),(.*)(.*)/\1/p' address-book.csv