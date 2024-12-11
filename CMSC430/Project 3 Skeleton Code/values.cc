// CMSC 430 Compiler Theory and Design
// Project 3 Skeleton
// UMGC CITE
// Summer 2023

// This file contains the bodies of the evaluation functions

#include <string>
#include <cmath>
using namespace std;
#include "values.h"
#include "listing.h"
#include <string.h>
#include <vector>
#include <algorithm>

double evaluateArithmetic(double left, Operators operator_, double right) {
	double result;
	switch (operator_) {
		case ADD:
			result = left + right;
			break;
		case SUBTRACT:
			result = left - right;
			break;
		case MULTIPLY:
			result = left * right;
			break;
		case DIVIDE:
			result = left / right;
			break;
		case MODULUS:
			result = int(left) % int(right);
			break;
		case EXPONENT:
			result = pow(left, right);
			break;
	}
	return result;
}

double evaluateRelational(double left, Operators operator_, double right) {
	double result;
	switch (operator_) {
		case LESS:
			result = left < right;
			break;
		case GREATER:
			result = left > right;
			break;
		case LESS_EQUAL:
			result = left <= right;
			break;
		case GREATER_EQUAL:
			result = left <= right;
			break;
		case EQUALS:
			result = left == right;
			break;
		case NOTEQUALS:
			result = left != right;
			break;
	}
	return result;
}

double evalutateNegation(string prim){
	double result;
	result = stod(prim) * -1;
	return result;
}

double evalutateNegation(double prim){
	double result;
	result = prim * -1;
	return result;
}

int evaluateChar(string charLit){
	int result;
	string s(charLit);

	if (charLit.size() == 3){
		result = charLit[1];
		//newChar = charLit.substr(1,2);
	}
	else{
		if ( charLit == "\'\\n\'"){
			result = 10;
		}
		else if ( charLit == "\'\\f\'"){
			result = 12;
		}
		else if ( charLit == "\'\\t\'"){
			result = 9;
		}
		else if ( charLit == "\'\\r\'"){
			result = 13;
		}
		else if ( charLit == "\'\\b\'"){
			result = 8;
		}
	}
	return result;
}

int evaluateHex(string hex){
	int result;
	result = stoi(hex.substr(1), nullptr, 16);
	return result;
}

double evaluateFold(string direction, Operators operator_, vector<double> list){
	
	double result;

	if(list.empty()){
		return 0;
	}
	else if (list.size() == 1){
		return list[0];
	}

	if (direction == "right"){

		reverse(list.begin(), list.end());
	}

	result = list[0];
	for(int i = 1; i < list.size(); i++){

		result = evaluateArithmetic(result, operator_, list[i]);

	}

	return result;
}