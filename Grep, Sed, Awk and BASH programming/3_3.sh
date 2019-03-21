
 awk 'BEGIN { print "[" ;}                    
      { subs1 = substr($0, 6)
      a=substr($1,1,length($1)-1);
      b=substr($(NF-1),2,4);

        ravi=$2
        for(i=3;i<NF-1;i++){
          ravi=ravi " " $i
        }
        if(NR != 250){
          print  " {"                             
            print  "   \"ID\" : \""     a  "\","   
            print  "   \"Name\" : \""  ravi "\","   
            print  "   \"Year\" : \""  b  "\","   
            print  "   \"Rating\" : \"" $NF  "\""   
            print  " } ,"                             
        }
        else{
          print  " {"                             
            print  "   \"ID\" : \""     a  "\","   
            print  "   \"Name\" : \""   ravi "\","   
            print  "   \"Year\" : \""  b  "\","   
            print  "   \"Rating\" : \"" $NF  "\""   
            print  " } "  
        }                           
      }                              
      END { print "]" }'  imdb-top-250.txt > imdb-top-250.json