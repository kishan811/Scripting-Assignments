awk '{if ($2=="M") print}' marks.txt > male.txt
awk '{if ($2=="F") print}' marks.txt > females.txt