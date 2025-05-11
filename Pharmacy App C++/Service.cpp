#include "Service.h"
#include "Validator.h"
#include <algorithm>
using std::copy_if;
using std::back_inserter;
using std::sort;

void Service::add(string Denumire, double Pret, string Producator, string Substanta) {
	Medicament Med1{ Denumire, Pret, Producator, Substanta };
	Validator v1;
	v1.validate(Med1);
	repo1.store(Med1);
}

vector<Medicament> Service::getAll() const {
	return repo1.getAll();
}

void Service::del(const string denumire, const string producator) {
	repo1.erase(denumire, producator);
}

void Service::upd(const string nume, const string prod, string Denumire, double Pret, string Producator, string Substanta) {
	Medicament Med1{ Denumire, Pret, Producator, Substanta };
	Validator v1;
	v1.validate(Med1);
	repo1.update(nume, prod, Med1);
}

Medicament Service::fnd(const string denumire, const string producator) {
	Medicament aux = repo1.find(denumire, producator);
	return aux;
}

vector<Medicament> Service::filter(std::function<bool(const Medicament&)>filtru) const {
	vector<Medicament> vec1 = repo1.getAll();
	vector<Medicament> rez;
	copy_if(vec1.begin(), vec1.end(), back_inserter(rez), filtru);
	return rez;
}

vector<Medicament> Service::sorts(std::function<int(const Medicament& m1, const Medicament& m2)>cmp) const {
	vector<Medicament> vec1 = repo1.getAll();
	sort(vec1.begin(), vec1.end(), cmp);
	//for (int i = 0; i < vec1.size() - 1; i++) {
	//	for (int j = i + 1; j < vec1.size(); j++) {
	//		if (cmp(vec1[i], vec1[j])) {
	//			auto& aux = vec1[i];
	//			vec1[i] = vec1[j];
	//			vec1[j] = aux;
	//			//vec1.set(i, vec1.get(j));
	//			//vec1.set(j, aux);
	//		}
	//	}
	//}
	return vec1;
}