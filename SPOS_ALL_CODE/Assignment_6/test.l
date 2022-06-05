%{ 
   #include<stdio.h>
   #include"y.tab.h"
%}

letter [A-Za-z]
digit [0-9]
identifier {letter}({letter}|{digit})*
keywords int|float|char|double
%%

{keywords} {return TYPE;}
{identifier} {return ID;}
"," {return COMMA;}
";" {return SC;}
"\n" {return NL;}
%%
