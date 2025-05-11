#pragma once
#include "Medicament.h"
//#include "VectorDinamic.h"
#include <vector>
using std::vector;

class RepoException {
	string msg;
public:
	/*
	Constructor pentru clasa RepoException.
	m = string exceptie.
	preconditii: m sa fie nu fie sir vid.
	posconditii: msg primeste sirul primit ca parametru.
	Returneaza o instanta a clasei RepoException.
	*/
	RepoException(string m) : msg{ m } {

	}
	/*
	Getter method pentru atributul msg.
	Returneaza atributul msg.
	*/
	string getMessage() const;
};

class Repo {
private:
	vector<Medicament> medicamente;
public:
	/*
	Constructor pentru clasa Repo.
	Returneaza o instanta a clasei Repo.
	*/
	Repo() = default;

	/*
	Constructor de copiere pentru clasa Repo.
	*/
	Repo(const Repo& ot) = delete;

	/*
	Stocheaza un medicament in repo.
	med = instanta a clasei Medicament.
	preconditii: nu exista.
	postconditii: med va fi stocat in vector.
	Arunca o exceptie daca denumirea si producatorul medicamentului exista deja.
	*/
	void store(const Medicament& med);

	/*
	Obtine toate medicamentele din repo.
	Returneaza vectorul cu medicamente.
	*/
	vector<Medicament> getAll() const;

	/*
	Sterge un medicament din repo.
	denumire = string denumire medicament.
	producator = string nume producator medicament.
	preconditii: nu exista.
	postconditii: medicamentul va fi sters din vector.
	Arunca o exceptie daca medicamentul nu exista.
	*/
	void erase(const string denumire, const string producator);

	/*
	Modifica un medicament din repo.
	denumire = string denumire medicament.
	producator = string denumire producator.
	med = instanta a clasei Medicament.
	preconditii: nu exista.
	postconditii: se modifica medicamentul cu denumirea si producatorul date.
	Arunca o exceptie daca medicamentul nu exista.
	*/
	void update(const string denumire, const string producator, const Medicament& med);

	/*
	Cauta un medicament in repo.
	denumire = string denumire medicament.
	producator = string denumire producator.
	preconditii: nu exista.
	postconditii: se cauta medicamentul in repo.
	Returneaza medicamentul gasit.
	Arunca o exceptie daca medicamentul nu exista.
	*/
	Medicament find(const string denumire, const string producator);
};

