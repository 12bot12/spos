%{ 
    #include<stdio.h>
    int yylex();
    int yyerror();
 %}
 %token VERB ADVERB PREPOSITION CONJUCTION ADJECTIVE PRONOUN NOUN NL
 %%
 sentence:simplesentence NL {printf("simple sentence");};|compoundsentence NL {printf("compund sentence");};
 simplesentence:subject VERB object | subject VERB object prephase;
 compoundsentence:simplesentence CONJUCTION simplesentence|compoundsentence CONJUCTION simplesentence;
 subject: NOUN|PRONOUN|ADJECTIVE subject;
 object: NOUN|ADJECTIVE object;
 prephase:PREPOSITION NOUN;
 %%
 int main()
{
	yyparse();       
}
int yyerror()
{
 	return 0;
}
int yywrap()
{
   return 1;
}

