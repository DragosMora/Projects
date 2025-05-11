#pragma once
#include <string>
#include "Repo.h"
#include "Medicament.h"
//#include "VectorDinamic.h"
#include <functional>
#include <iostream>
#include "RepoReteta.h"
using std::string;

class ServiceReteta {
private:
	RepoReteta& repo_reteta;
	Repo& repo;
public:
	/*
	Constructor pentru clasa ServiceReteta.
	Repo1 = instanta a clasei RepoReteta.
	Returneaza o instanta din clasa ServiceReteta.
	*/
	ServiceReteta(RepoReteta& Repo1, Repo& repo1) : repo_reteta{ Repo1 }, repo{ repo1 } {

	}

	/*
	Constructor de copiere pentru clasa ServiceReteta.
	ot = referinta la instanta ServiceReteta.
	*/
	ServiceReteta(const ServiceReteta& ot) = delete;

	/*
	Constructor default pentru clasa ServiceReteta.
	Returneaza o instanta din clasa ServiceReteta.
	*/
	ServiceReteta() = default;

	/*
	Apeleaza RepoReteta pentru adaugare in lista.
	med = referinta a instantei Medicament.
	preconditii: nu exista.
	postconditii: se adauga pe reteta medicamentul.
	*/
	void write(const string denumire, const string producator);

	/*
	Apeleaza RepoReteta pentru dimensiune vector.
	Returneaza dimensiunea listei.
	*/
	int dim() const;

	/*
	Apeleaza RepoReteta pentru get_all.
	*/
	vector<Medicament> get_all() const;

	/*
	Apeleaza RepoReteta pentru clear.
	*/
	void clear();

	/*
	Apeleaza RepoReteta pentru export.
	nume_fisier = string nume fisier pentru export.
	preconditii: nume_fisier sa fie valid.
	postconditii: se apeleaza corespunzator.
	*/
	void exports(const string nume_fisier) const;

	/*
	Genereaza aleator medicamente.
	nr = const integer numar medicamente.
	denumiri = vector string denumiri medicamente.
	preturi = vector int preturi.
	producatori = vector string producatori.
	substante = vector string substante.
	preconditii: nr sa fie valid.
	postconditii: se genereaza aleator medicamentele.
	*/
	void generate(int nr, vector<string>denumiri, vector<double>preturi, vector<string>producatori, vector<string>substante);
};