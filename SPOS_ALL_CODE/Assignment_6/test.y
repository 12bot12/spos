%{ 
   #include<stdio.h>
   int yylex();	
   int yyerror(); 
%}
%token TYPE ID SC COMMA NL
%%
start: TYPE varlist SC NL {printf("statement valid \n");}
varlist: varlist COMMA ID | ID;
%%
int main()
{
	yyparse();       
}
int yyerror()
{
 	printf("InValid statement\n");
}
int yywrap()
{
   return 1;
}