#!/bin/bash
c=`tput cols`;
L=`tput lines`;
let x=$c/2;
let y=$L/2;
d=0;
le=3;
t="$y;$x";
i=0;
j=0;
S=0;
read -sN1 -t 0.01 k
while (1)
{
	A(){ let i=($RANDOM%$c);let j=($RANDOM%$L);};A
}
