#pragma once
#include "Repo.h"

class ActiuneUndo {
public:
	/*
	Executa operatia undo.
	*/
	virtual void doUndo() = 0;

	/*
	Destructor virtual clasa ActiuneUndo.
	*/
	virtual ~ActiuneUndo() = default;
};

class UndoAdauga : public ActiuneUndo {
	Medicament medAdaugat;
	Repo& repo;
public:
	/*
	Constructor pentru clasa UndoAdauga.
	repo = referinta la repo.
	med = referinta la medicament.
	*/
	UndoAdauga(Repo& repo, const Medicament& med) : repo{ repo }, medAdaugat{ med } {}

	/*
	Executa operatia undo.
	*/
	void doUndo() override {
		repo.erase(medAdaugat.getDenumire(), medAdaugat.getProducator());
	}
};

class UndoSterge : public ActiuneUndo {
	Medicament medSters;
	Repo& repo;
public:
	/*
	Constructor pentru clasa UndoSterge.
	repo = referinta la repo.
	med = referinta la medicament.
	*/
	UndoSterge(Repo& repo, const Medicament& med) : repo{ repo }, medSters{ med } {};

	/*
	Executa operatia undo.
	*/
	void doUndo() override {
		repo.store(medSters);
	}
};

class UndoModifica : public ActiuneUndo {
	Medicament medModificat;
	Medicament medCurent;
	Repo& repo;
public:
	/*
	Constructor pentru clasa UndoModifica.
	repo = referinta la repo.
	med = referinta la medicament.
	*/
	UndoModifica(Repo& repo, const Medicament& med1, const Medicament& med2) : repo{ repo }, medModificat{ med1 }, medCurent{ med2 } {};

	void doUndo() override {
		repo.update(medCurent.getDenumire(), medCurent.getProducator(), medModificat);
	}
};