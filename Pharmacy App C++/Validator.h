#pragma once
#include <string>
#include "Medicament.h"
using std::string;

class ValidatorException {
	string msg;
public:
	/*
	Constructor pentru clasa ValidatorException.
	m = string exceptie.
	preconditii: m sa fie nu fie sir vid.
	posconditii: msg primeste sirul primit ca parametru.
	Returneaza o instanta a clasei ValidatorException.
	*/
	ValidatorException(string m) : msg{ m } {

	}
	/*
	Getter method pentru atributul msg.
	Returneaza atributul msg.
	*/
	string getMessage() const;
};

class Validator {
public:
	/*
	Constructor pentru clasa Validator.
	*/
	Validator() {

	}

	/*
	Valideaza un medicament.
	med = instanta a clasei Medicament.
	preconditii: nu exista.
	postconditii: arunca exceptii daca exista erori sau nu arunca nimic.
	*/
	void validate(const Medicament& med) const;
};