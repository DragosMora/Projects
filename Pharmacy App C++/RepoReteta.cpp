#include "RepoReteta.h"
#include <fstream>
using std::ofstream;

void RepoReteta::write(const Medicament& med) {
	for (const Medicament& M : reteta) {
		if (M.getDenumire() == med.getDenumire() && M.getProducator() == med.getProducator()) {
			throw RepoException("Medicament existent!\n");
		}
	}
	reteta.push_back(med);
}

int RepoReteta::dim() const {
	return reteta.size();
}

vector<Medicament> RepoReteta::get_all() const {
	return reteta;
}

void RepoReteta::clear() {
	reteta.clear();
}

void RepoReteta::exports(const string nume_fisier) {
	ofstream file(nume_fisier);
	for (const Medicament& med : reteta) {
		file << med.getDenumire() << "," << med.getPret() << "," << med.getProducator() << "," << med.getSubstanta() << '\n';
	}
	file.close();
}