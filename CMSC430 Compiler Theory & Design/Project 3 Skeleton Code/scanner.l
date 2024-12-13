/* CMSC 430 Compiler Theory and Design
   Project 3 Skeleton
   UMGC CITE
   Summer 2023 */

Michael Rodriguez, Project 3, 03Mar2024
/* This file contains flex input file */

%{
#include <cstdio>
#include <string>
#include <vector>
using namespace std;
#include "values.h"
#include "listing.h"
#include "tokens.h"

%}

%option noyywrap

ws		[ \t\r]+
comment		(\/\/|--).*\n?
line		[\n]
id		[A-Za-z]([A-Za-z0-9])*
digit		[0-9]
dec		{digit}+
hexint		#[0-9A-Fa-f]+
char		'\\?.'
punc		[\(\),:;]
reallit		[0-9]*\.[0-9]+([eE](\+|-)?[0-9]*)?
%%

{ws}		{ ECHO; }
{comment}	{ ECHO; nextLine(); }
{line}		{ ECHO; nextLine(); }
"+"		{ ECHO; yylval.oper = ADD; return(ADDOP); }
"*"		{ ECHO; yylval.oper = MULTIPLY; return(MULOP); }
"&"		{ ECHO; yylval.oper = AND; return(ANDOP); }
"<"		{ ECHO; yylval.oper = LESS; return(RELOP); }
"=>"		{ ECHO; return(ARROW); }
begin		{ ECHO; return(BEGIN_); }
case		{ ECHO; return(CASE); }
character	{ ECHO; return(CHARACTER); }
end		{ ECHO; return(END); }
endswitch	{ ECHO; return(ENDSWITCH); }
function	{ ECHO; return(FUNCTION); }
integer		{ ECHO; return(INTEGER); }
is		{ ECHO; return(IS); }
list		{ ECHO; return(LIST); }
of		{ ECHO; return(OF); }
others		{ ECHO; return(OTHERS); }
returns		{ ECHO; return(RETURNS); }
switch		{ ECHO; return(SWITCH); }
when		{ ECHO; return(WHEN); }

else	   {ECHO; return(ELSE); }
elsif	   {ECHO; return(ELSIF); }
endfold		{ECHO; return(ENDFOLD); }
endif	   {ECHO; return(ENDIF); }
fold	   {ECHO; return(FOLD); }
if	      {ECHO; return(IF); }
left	   {ECHO; return(LEFT); }
real	   {ECHO; return(REAL); }
right	   {ECHO; return(RIGHT); }
then	   {ECHO; return(THEN); }
"|"		{ECHO; yylval.oper = OR; return(OROP); }
"!"		{ECHO; yylval.oper = NOT; return(NOTOP); }
"="		{ECHO; yylval.oper = EQUALS; return(RELOP); }
"<>"	   {ECHO; yylval.oper = NOTEQUALS; return(RELOP); }
">"		{ECHO; yylval.oper = GREATER; return(RELOP); }
">="	   {ECHO; yylval.oper = GREATER_EQUAL; return(RELOP); }
"<="	   {ECHO; yylval.oper = LESS_EQUAL; return(RELOP); }
"-"		{ECHO; yylval.oper = SUBTRACT; return(ADDOP); }
"/"		{ECHO; yylval.oper = DIVIDE; return(MULOP); }
"%"		{ECHO; yylval.oper = MODULUS; return(REMOP); }
"^"		{ECHO; yylval.oper = EXPONENT; return(EXPOP); }
"~"		{ECHO; yylval.oper = NEGATION; return(NEGOP); }
{hexint}	{ECHO; yylval.value = evaluateHex(yytext); return(INT_LITERAL);}
{reallit}	{ECHO; yylval.value = atof(yytext); return(REAL_LITERAL);}

{id}		{ ECHO; yylval.iden = (CharPtr)malloc(yyleng + 1); 
			strcpy(yylval.iden, yytext); return(IDENTIFIER);}
{dec}		{ ECHO; yylval.value = atoi(yytext); return(INT_LITERAL); }
{char}		{ ECHO; yylval.value = evaluateChar(yytext); return(CHAR_LITERAL); }
{punc}		{ ECHO; return(yytext[0]); }
.		{ ECHO; appendError(LEXICAL, yytext); }
%%
