#!/bin/bash
read s
echo $s | sed -n -E "/([0-1][0-9][0-9]|[2][0-4][0-9]|25[0-5])\.([0-1][0-9][0-9]|[2][0-4][0-9]|25[0-5])\.([0-1][0-9][0-9]|[2][0-4][0-9]|25[0-5])\.([0-1][0-9][0-9]|[2][0-4][0-9]|25[0-5])/p" 
