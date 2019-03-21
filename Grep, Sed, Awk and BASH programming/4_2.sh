 #!/bin/bash
read -s pass
if [[ ${#pass} -ge 8 && "$pass" == *[@#\$%\&+\*\-=]* && "$pass" == *[:digit:]* ]]; then
	echo "This is Strong password :)"
else
	echo "Please enter the valid Password with 8 characters, with one numeric and one special symbol(@,*,&,etc...)"
fi	

