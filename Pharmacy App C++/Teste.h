#pragma once

class Teste {
private:
	/*
	Ruleaza testele pentru domain Medicament.
	*/
	void domain_tests() const;

	/*
	Ruleaza testele pentru validator Medicament.
	*/
	void validator_tests() const;

	/*
	Ruleaza testele pentru repo Medicament.
	*/
	void repo_tests() const;

	/*
	Ruleaza testele pentru service Medicament.
	*/
	void service_tests() const;

	/*
	Ruleaza testele pentru vector dinamic.
	*/
	void vector_dinamic_tests() const;

	/*
	Ruleaza testele pentru repo reteta.
	*/
	void repo_reteta_tests() const;

	/*
	Ruleaza testele pentru service reteta.
	*/
	void service_reteta_tests() const;
public:
	/*
	Constructor pentru clasa Teste.
	Se returneaza o instanta a clasei Teste.
	*/
	Teste() {

	}

	/*
	Ruleaza toate functiile cu teste din clasa Teste.
	*/
	void ruleaza_toate_testele() const;
};