%{
#include<stdlib.h>
#include<stdio.h>
int yylex();
int yyerror();
%}
%token TYPE COMMA SC ID NL;
%%
start : TYPE varlist SC NL
	{printf("Input is valid");}
	;
varlist: varlist COMMA ID
	|ID
	;
%%
int main(){
yyparse();
}
int yyerror(){
printf("Invalid Statement");
}
int yywrap(){
return 1;
}
