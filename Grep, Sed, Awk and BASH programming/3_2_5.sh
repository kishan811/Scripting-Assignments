awk 'BEGIN{print "\n\n*** Grade Report for the ABC course *** \n\nStudent : Gender: Grade" 
 max = 0;p=0;avg=0} 
{ if(NR==2){total=$3+$4+$5;min=total;name=$1;max=total;i=0;}
if(NR>1) {
total=$3+$4+$5;
p=p+total;
    if(max<total)
    {
    max=total;
    name=$1;
    }
    min=(min>total)?total:min;
    
if(total>=95&&total<=100) grade="A";
else if(total>=90&&total<95) grade="A-";
else if(total>=85&&total<90) grade="B";
else if(total>=80&&total<85) grade="B-";
else if(total>=75&&total<80) grade="C";
else if(total>=70&&total<75) grade="C-";
else if(total>=60&&total<70) grade="D";
else if(total<60) grade="F";
 print $1, ":", $2, ":" , grade}} 
 END{
 avg=p/(NR-1);
  print "\nTotal Students in the course-> " NR-1 " \nHighest Marks-> " max "\nLowest Marks-> " min "\nAverage Marks-> "avg "\n\n*** END OF GRADE REPORT ***\n"}' marks.txt
