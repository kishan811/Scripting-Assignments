
awk '{if(NR>1) {total=$3+$4+$5; print $1, ":" , total}}' marks.txt