/* CMSC 430 Compiler Theory and Design
   Project 3 Skeleton
   UMGC CITE
   Summer 2023
   //Michael Rodriguez 03Mar2024 Parser tokens & Productions
   Project 3 Parser with semantic actions for the interpreter */

%{

#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#include "values.h"
#include "listing.h"
#include "symbols.h"
#include <stack>

std::stack<double> params;

/*int paramsMax = 0;
//int z = 0;
//double *params;
*/

int yylex();
void yyerror(const char* message);
double extract_element(CharPtr list_name, double subscript);

Symbols<double> scalars;
Symbols<vector<double>*> lists;
double result;

%}

%define parse.error verbose

%union {
	CharPtr iden;
	Operators oper;
	double value;
	vector<double>* list;
}

%token <iden> IDENTIFIER

%token <value> INT_LITERAL CHAR_LITERAL REAL_LITERAL

%token <oper> ADDOP MULOP ANDOP RELOP OROP NOTOP REMOP NEGOP EXPOP

%token ARROW

%token BEGIN_ CASE CHARACTER ELSE END ENDSWITCH FUNCTION INTEGER IS LIST OF OTHERS
	RETURNS SWITCH WHEN ELSIF ELSIFS ENDFOLD ENDIF FOLD IF LEFT REAL RIGHT THEN

%type <value> body statement_ statement cases case expression term primary
	 condition relation exprimary unprimary andcondition notcondition
	 elsif elsifs direction operator 

%type <list> list list_choice expressions

%%

function:	
	function_header optional_variables body ';' {result = $3;} ;
	
function_header:	
	FUNCTION IDENTIFIER parameter parameters RETURNS type ';' |
	error ;

type:
	INTEGER | REAL | CHARACTER ;
	
optional_variables:
	optional_variables variable | %empty |
	error ;
    
parameters:
	',' parameter parameters | %empty ;

parameter:
	IDENTIFIER ':' type 
	{if (!params.empty()){
		scalars.insert($1, params.top());
		params.pop();
	}
	else{
		appendError(UNDECLARED, $1);
	};}
	| %empty;
	
variable:	
	IDENTIFIER ':' type IS statement ';' {scalars.insert($1, $5);}; |
	IDENTIFIER ':' LIST OF type IS list ';' {lists.insert($1, $7);} ;

list:
	'(' expressions ')' {$$ = $2;} ;

expressions:
	expressions ',' expression {$1->push_back($3); $$ = $1;} | 
	expression {$$ = new vector<double>(); $$->push_back($1);}

body:
	BEGIN_ statement_ END {$$ = $2;} ;

statement_:
	statement ';' |
	error ';' {$$ = 0;} ;
    
direction:
	LEFT | RIGHT ;

operator:
	ADDOP | MULOP ;

list_choice:
	list | IDENTIFIER ;
	
elsifs:
	elsifs elsif {$$ = !isnan($1) ? $1 : $2;}|
	%empty {$$ = NAN;};

elsif:
	ELSIF condition THEN statement_ {$$ = $2 ? $4 : NAN;};

statement:
	expression |
	WHEN condition ',' expression ':' expression {$$ = $2 ? $4 : $6;} |
	FOLD direction operator list_choice ENDFOLD {$$ = evaluateFold($2, $3, $4)};|
	IF condition THEN statement_ elsifs ELSE statement_ ENDIF 
		{$$ = $2 ? $4 : !isnan($5) ? $5 : $7;} |
	SWITCH expression IS cases OTHERS ARROW statement ';' ENDSWITCH
		{$$ = !isnan($4) ? $4 : $7;} ;
cases:
	cases case {$$ = !isnan($1) ? $1 : $2;} |
	%empty {$$ = NAN;} ;
	
case:
	CASE INT_LITERAL ARROW statement ';' {$$ = $<value>-2 == $2 ? $4 : NAN;} ; 

condition:
	condition OROP andcondition {$$ = $1 || $3;} |
	andcondition ;

andcondition:
	andcondition ANDOP notcondition {$$ = $1 && $3;} |
	notcondition ;

notcondition:
	NOTOP relation {$$ = !$2;}|
	relation ;

relation:
	'(' condition ')' {$$ = $2;} |
	expression RELOP expression {$$ = evaluateRelational($1, $2, $3);} ;

expression:
	expression ADDOP term {$$ = evaluateArithmetic($1, $2, $3);} |
	term ;
      
term:
	term MULOP exprimary {$$ = evaluateArithmetic($1, $2, $3);} |
	term REMOP exprimary {$$ = evaluateArithmetic($1, $2, $3);} |
	exprimary ;

exprimary:
	unprimary EXPOP exprimary {$$ = evaluateArithmetic($1, $2, $3);}|
	unprimary;

unprimary:
	NEGOP INT_LITERAL {$$ = evalutateNegation($2);} |
	NEGOP REAL_LITERAL {$$ = evalutateNegation($2);} |
	NEGOP IDENTIFIER {$$ = evalutateNegation($2);} |
	primary;

primary:
	'(' expression ')' {$$ = $2;} |
	INT_LITERAL | REAL_LITERAL | CHAR_LITERAL |
	IDENTIFIER '(' expression ')' {$$ = extract_element($1, $3); } |
	IDENTIFIER {if (!scalars.find($1, $$)) appendError(UNDECLARED, $1);} ;

%%

void yyerror(const char* message) {
	appendError(SYNTAX, message);
}

double extract_element(CharPtr list_name, double subscript) {
	vector<double>* list; 
	if (lists.find(list_name, list))
		return (*list)[subscript];
	appendError(UNDECLARED, list_name);
	return NAN;
}

int main(int argc, char *argv[]) {

	/*
	paramsMax = argc - 1;
	double paramArgs[argc-1];
	params = paramArgs;
	*/

	for(int i = argc-1; i >= 1; i--){
		params.push(atof(argv[i]));
		//params[i] = atof(argv[i]);
	}

	firstLine();
	yyparse();
	if (lastLine() == 0)
		cout << "Result = " << result << endl;
	return 0;
} 
