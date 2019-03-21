awk 'BEGIN{max = 0;p=0;avg=0; print "Student : Gender: Total Marks"} 
{ if(NR==2){total=$3+$4+$5;min=total;name=$1;max=total;i=0;}
if(NR>1) {
total=$3+$4+$5;
p=p+total; 
x[i]=total;
     y[i]=$1;
     i++;
    if(max<total)
    {
    max=total;
    name=$1;
    }
    min=(min>total)?total:min;
   
 print $1, ":", $2, ":" , total}} 
 END{
    avg=p/(NR-1); 
    print "\n Students with above average marks are:- ";
for(i=1; i<NR-1; i++)
 {

 	if(x[i]>avg)
 		{
 			print y[i] "-->" x[i];
 		}
 }
 print "Student with highest marks (Topper) is : " name " with total of " max " marks."}' marks.txt
