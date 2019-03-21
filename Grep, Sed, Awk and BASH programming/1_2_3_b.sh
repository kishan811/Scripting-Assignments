#!/bin/bash
# regex for ipv6 format address{seperated by either hyphen or colon}
read x
echo $x | grep -E '^[0-9a-f]{2}(\:)[0-9a-f]{2}\1[0-9a-f]{2}\1[0-9a-f]{2}\1[0-9a-f]{2}\1[0-9a-f]{2}$'