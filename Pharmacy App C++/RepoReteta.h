#pragma once
#include "Medicament.h"
#include "Repo.h"
#include <vector>
using std::vector;

class RepoReteta {
private:
	vector<Medicament> reteta;
public:
	/*
	Constructor pentru clasa RepoReteta.
	Returneaza o instanta a clasei RepoReteta.
	*/
	RepoReteta() = default;

	/*
	Constructor de copiere pentru clasa Repo.
	*/
	RepoReteta(const RepoReteta& ot) = delete;

	/*
	Scrie pe lista un medicament.
	med = referinta la instanta Medicament.
	preconditii: med este valid.
	postconditii: adauga in vectorul reteta pe med.
	Arunca o exceptie daca medicamentul exista deja pe reteta.
	*/
	void write(const Medicament& med);

	/*
	Returneaza dimensiunea retetei.
	*/
	int dim() const;

	/*
	Returneaza toate medicamentele din lista.
	*/
	vector<Medicament> get_all() const;

	/*
	Sterge toate medicamentele de pe reteta.
	preconditii: nu exista.
	postconditii: se sterg toate medicamentele.
	*/
	void clear();

	/*
	Exporta reteta in fisierul cu numele primit ca parametru.
	nume_fisier = string nume fisier.
	preconditii: nume_fisier sa fie un nume valid.
	postconditii: se exporta lista de medicamente.
	*/
	void exports(const string nume_fisier);
};