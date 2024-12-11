// CMSC 430 Compiler Theory and Design
// Project 3 Skeleton
// UMGC CITE
// Summer 2023

//Michael Rodriguez 03Mar2024 Parser tokens & Productions
// This file contains type definitions and the function
// definitions for the evaluation functions

#include <vector>

typedef char* CharPtr;

//enum Direction {LEFT, RIGHT};

enum Operators {ADD, SUBTRACT, MULTIPLY, MODULUS, DIVIDE, EXPONENT, NEGATION,
                LESS, GREATER, LESS_EQUAL, GREATER_EQUAL, AND, OR, NOT,
                NOTEQUALS, EQUALS};

double evaluateArithmetic(double left, Operators operator_, double right);
double evaluateRelational(double left, Operators operator_, double right);
double evalutateNegation(string prim);
double evalutateNegation(double prim);
int evaluateChar(string charLit);
int evaluateHex(string hex);
double evaluateFold(string direction, Operators operator_, vector<double> list);