// CMSC 430 Compiler Theory and Design
// Project 3 Skeleton
// UMGC CITE
// Summer 2023

//Michael Rodriguez, Project 3, 03Mar2024
// This file contains the bodies of the functions that produces the 
// compilation listing

#include <cstdio>
#include <string>
using namespace std;
#include "listing.h"
#include <vector>

static int lineNumber;
static string error = "";
static vector<string> errorQueue;
static int totalErrors, lexicalErrors, semanticErrors, syntaxErrors = 0;

static void displayErrors();

void firstLine()
{
	lineNumber = 1;
	printf("\n%4d  ",lineNumber);
}

void nextLine()
{
	displayErrors();
	lineNumber++;
	printf("%4d  ",lineNumber);
}

int lastLine()
{
	printf("\r");
	displayErrors();
	printf("     \n");

	if (totalErrors==0){
		printf("\tCompiled Successfully\n");
	}
	else {
		printf("Lexical Errors %i\n", lexicalErrors);
		printf("Syntax Errors %i\n", syntaxErrors);
		printf("Semantic Errors %i\n", semanticErrors);
	}

	
	return totalErrors;
}
    
void appendError(ErrorCategories errorCategory, string message)
{
	string messages[] = { "Lexical Error, Invalid Character ", "",
		"Semantic Error, ", "Semantic Error, Duplicate ",
		"Semantic Error, Undeclared " };

	error = messages[errorCategory] + message;
	errorQueue.push_back(error);

	if (messages[errorCategory]=="Lexical Error, Invalid Character "){
		lexicalErrors++;
	}
	else if (messages[errorCategory]=="Syntax Error" || errorCategory==SYNTAX){
		syntaxErrors++;
	}
	else if (messages[errorCategory]=="Semantic Error, " || 
			 messages[errorCategory]=="Semantic Error, Duplicate" ||
			 messages[errorCategory]=="Semantic Error, Undeclared "){
		semanticErrors++;
	}
	totalErrors++;
}

void displayErrors()
{
	while (!errorQueue.empty()){
		printf("%s\n", errorQueue.back().c_str());
		errorQueue.pop_back();
	}
	
}
