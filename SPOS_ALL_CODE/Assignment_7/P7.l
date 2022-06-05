%{ #include<stdio.h>
   #include "y.tab.h"
%}
verb is|am|are|was|were|be|play
adverb very|simply|gently|calmly
preposition to|from|above|behind|before
conjuction if|then|and|or|but
adjective their|my|your|its|her|his
pronoun i|you|he|she|they
noun [A-Za-z]+
%%
{verb} return VERB;
{adverb} return ADVERB;
{preposition} return PREPOSITION;
{conjuction} return CONJUCTION;
{adjective} return ADJECTIVE;
{pronoun} return PRONOUN;
{noun} return NOUN;
"\n" return NL;
%%
