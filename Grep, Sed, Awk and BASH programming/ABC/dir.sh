cd $1
items=$(ls | grep $2)
mkdir $2
for item in $items
do
	mv $item ./$2
done