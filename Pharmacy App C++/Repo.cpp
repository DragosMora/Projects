#include "Repo.h"
#include <algorithm>
using std::find_if;

string RepoException::getMessage() const {
	return msg;
}

void Repo::store(const Medicament& med) {
	for (const Medicament& M : medicamente) {
		if (M.getDenumire() == med.getDenumire() && M.getProducator() == med.getProducator()) {
			throw RepoException("Medicament existent!\n");
		}
	}
	medicamente.push_back(med);
}

vector<Medicament> Repo::getAll() const {
	return medicamente;
}

void Repo::erase(const string denumire, const string producator) {
	int i{ 0 };
	for (const Medicament& M : medicamente) {
		if (M.getDenumire() == denumire && M.getProducator() == producator) {
			//medicamente.erase(i);
			medicamente.erase(medicamente.begin() + i);
			return;
		}
		i++;
	}
	throw RepoException("Medicament inexistent!\n");
}

void Repo::update(const string denumire, const string producator, const Medicament& med) {
	int i{ 0 };
	for (const Medicament& M : medicamente) {
		if (M.getDenumire() == denumire && M.getProducator() == producator) {
			//medicamente.begin() + i = med;
			//replace(medicamente.begin(), medicamente.end(), medicamente.begin() + i, med);
			medicamente.insert(medicamente.begin() + i, med);
			medicamente.erase(medicamente.begin() + i + 1);
			return;
		}
		i++;
	}
	throw RepoException("Medicament inexistent!\n");
}

Medicament Repo::find(const string denumire, const string producator) {
	//auto it = std::copy_if (foo.begin(), foo.end(), bar.begin(), [](int i){return !(i<0);} );
	//const auto& rez = find_if(medicamente.begin(), medicamente.end(), [](const Medicament& M, const string denumire, const string producator) {if (M.getDenumire() == denumire && M.getProducator() == producator) return true; });
	for (const Medicament& M : medicamente) {
		if (M.getDenumire() == denumire && M.getProducator() == producator) {
			return M;
		}
	}
	throw RepoException("Medicament inexistent!\n");
}