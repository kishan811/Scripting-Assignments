#!/bin/bash
ls -lh | sed -n "/^d/p" | wc -l
