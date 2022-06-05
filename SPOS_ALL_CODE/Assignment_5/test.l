%{
%}
letter [A-Za-z]
digit [0-9]
identifier {letter}({letter}|{digit})*
number {digit}+(\.{digit}+)?
punctuation [;|,|.|"|#|()|{}]
operators [+|-|=|*|<|>]
keywords if|else|for|int|while|do|void
literal \".*\"
comment "//".*
headerfile "#".*
multicomment "/*".*"*/"
%%

{headerfile} {printf("\n Headerfile %s is found" ,yytext);}
{keywords} {printf("\n keywords %s is found" ,yytext);}
{identifier} {printf("\n identifier %s is found" ,yytext);}
{number} {printf("\n number %s is found" ,yytext);}
{punctuation} {printf("\n punctuation %s is found" ,yytext);}
{literal} {printf("\n literal %s is found" ,yytext);}
{operators} {printf("\n operators %s is found" ,yytext);}
{comment} {printf("\n comment %s is found" ,yytext);}
{multicomment} {printf("\n multicomment %s is found" ,yytext);}
%%

int main()
{ yylex();
}
int yywrap()
{ return 1;
}
