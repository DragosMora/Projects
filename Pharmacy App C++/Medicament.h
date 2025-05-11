#pragma once
#include <string>
using std::string;

class Medicament {
private:
	string denumire;
	double pret = 0;
	string producator;
	string substanta;
public:
	/*
	Constructor Medicament.
	Denumire = string denumire medicament.
	Pret = double pret medicament.
	Producator = string nume producator medicament.
	Substanta = string nume substanta activa medicament.
	preconditii: parametrii sa fie valizi.
	postconditii: atributele primesc valorile corespunzatoare.
	Se returneaza o instanta a clasei Medicament.
	*/
	Medicament(string Denumire, double Pret, string Producator, string Substanta) : denumire{ Denumire }, pret{ Pret }, producator{ Producator }, substanta{ Substanta } {

	}

	/*
	Constructor default.
	*/
	Medicament() = default;

	/*
	Constructor de copiere pentru clasa Medicament.
	*/
	Medicament(const Medicament& ot) : denumire{ ot.denumire }, pret{ ot.pret }, producator{ ot.producator }, substanta{ ot.substanta } {

	}

	/*
	Getter method pentru denumire medicament.
	Se returneaza valoarea atributului denumire.
	*/
	string getDenumire() const;

	/*
	Getter method pentru pret medicament.
	Se returneaza valoarea atributului pret.
	*/
	double getPret() const;
	/*
	Getter method pentru producator medicament.
	Se returneaza valoarea atributului producator.
	*/
	string getProducator() const;

	/*
	Getter method pentru substanta medicament.
	Se returneaza valoarea atributului substanta.
	*/
	string getSubstanta() const;
};