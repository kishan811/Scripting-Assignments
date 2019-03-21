#!/bin/bash
if [ -f $1 ]; then
  case $1 in
    *.tar.gz)tar zxf $1  ;;
    *.zip)unzip $1       ;;
    *.tar.xz)tar zvxf $1 ;;
    *.bz2)bunzip2 $1     ;;
    *.rar)rar x $1       ;;
    *.gz)gunzip $1       ;;
    *.tar.bz2)tar xjf $1 ;;
    *.tar)tar xf $1      ;;
    *.tbz2)tar xjf $1    ;;
    *)echo "Cannot be extracted!!!" ;;
  esac
else
  echo "Incompatible File type for decompression..."
fi