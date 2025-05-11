#include "ServiceReteta.h"
#include <random>
using std::max;

void ServiceReteta::write(const string denumire, const string producator) {
	Medicament med = repo.find(denumire, producator);
	repo_reteta.write(med);
}

int ServiceReteta::dim() const {
	return repo_reteta.dim();
}

vector<Medicament> ServiceReteta::get_all() const {
	return repo_reteta.get_all();
}

void ServiceReteta::clear() {
	repo_reteta.clear();
}

void ServiceReteta::exports(const string nume_fisier) const {
	repo_reteta.exports(nume_fisier);
}

void ServiceReteta::generate(int nr, vector<string>denumiri, vector<double>preturi, vector<string>producatori, vector<string>substante) {
	while (nr) {
		std::mt19937 mt{ std::random_device{}() };
		std::uniform_int_distribution<> dist1(0, denumiri.size() - 1);
		int rndNr1 = dist1(mt);// numar aleator intre [0,size-1]
		string denumire = denumiri[rndNr1];

		std::uniform_int_distribution<> dist2(0, preturi.size() - 1);
		int rndNr2 = dist2(mt);// numar aleator intre [0,size-1]
		double pret = preturi[rndNr2];

		std::uniform_int_distribution<> dist3(0, producatori.size() - 1);
		int rndNr3 = dist3(mt);// numar aleator intre [0,size-1]
		string producator = producatori[rndNr3];

		std::uniform_int_distribution<> dist4(0, substante.size() - 1);
		int rndNr4 = dist4(mt);// numar aleator intre [0,size-1]
		string substanta = substante[rndNr4];

		Medicament med1{ denumire, pret, producator, substanta };
		try {
			repo_reteta.write(med1);
		}
		catch (RepoException) {
			nr++;
		}
		nr--;
	}
}