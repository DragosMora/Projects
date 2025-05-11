#pragma once
#include <string>
#include "Repo.h"
#include "Medicament.h"
//#include "VectorDinamic.h"
#include <functional>
#include <iostream>
#include "ActiuneUndo.h"
using std::string;
using std::vector;
using std::unique_ptr;

class Service {
private:
	Repo& repo1;
	vector<unique_ptr<ActiuneUndo>> undoActions;
public:
	/*
	Constructor pentru clasa Service.
	repo1 = instanta a clasei Repo.
	Returneaza o instanta din clasa Service.
	*/
	Service(Repo& Repo1) : repo1{ Repo1 } {

	}

	/*
	Constructor de copiere pentru clasa Service.
	ot = referinta la instanta Service.
	*/
	Service(const Service& ot) = delete;

	/*
	Constructor default pentru clasa Service.
	Returneaza o instanta din clasa Service.
	*/
	Service() = default;

	/*
	Creaza un medicament si il stocheaza in repo.
	Denumire = string denumire medicament.
	Pret = double pret medicament.
	Producator = string nume producator medicament.
	Substanta = string nume substanta activa medicament.
	preconditii: nu exista.
	postconditii: se apeleaza repo.
	*/
	void add(string Denumire, double Pret, string Producator, string Substanta);

	/*
	Obtine vectorul de medicamente din repo.
	Returneaza vectorul de medicamente obtinut.
	*/
	vector<Medicament> getAll() const;

	/*
	Apeleaza repo pentru stergere.
	denumire = string denumire medicament.
	producator = string denumire producator.
	*/
	void del(const string denumire, const string producator);

	/*
	Creaza un medicament si il modifica in repo.
	nume = string nume medicament pentru cautare.
	prod = string nume produs medicament pentru cautare.
	Denumire = string denumire medicament.
	Pret = double pret medicament.
	Producator = string nume producator medicament.
	Substanta = string nume substanta activa medicament.
	preconditii: nu exista.
	postconditii: se modifica in repo medicamentul.
	*/
	void upd(const string nume, const string prod, string Denumire, double Pret, string Producator, string Substanta);

	/*
	Apeleaza repo pentru cautare medicament.
	denumire = string denumrie medicament cautat.
	producator = string nume producator cautat.
	preconditii: nu exista.
	postconditii: cauta in repo medicamentul.
	Returneaza medicamentul gasit.
	*/
	Medicament fnd(const string denumire, const string producator);

	/*
	Filtreaza medicamente dupa functia transmisa ca parametru.
	filtru = functie lambda.
	Returneaza vector dinamic filtrat.
	*/
	vector<Medicament> filter(std::function<bool(const Medicament&)>filtru) const;

	/*
	Sorteaza medicamente dupa functia transmisa ca parametru.
	m1 = referinta Medicament.
	m2 = referinta Medicament.
	Returneaza vector dinamic sortat.
	*/
	vector<Medicament> sorts(std::function<int(const Medicament& m1, const Medicament& m2) > cmp) const;
};