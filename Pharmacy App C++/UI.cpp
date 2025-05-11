#include "UI.h"
#include <iostream>
#include "Validator.h"
#include <vector>
using std::cin;
using std::cout;
using std::vector;

void UI::run() {
	while (true) {
		//afisare reteta.
		cout << "Reteta curenta:\n";
		auto reteta = service_reteta.get_all();
		for (const Medicament& Med : reteta) {
			cout << Med.getDenumire() << " " << Med.getPret() << " " << Med.getProducator() << " " << Med.getSubstanta() << '\n';
		}
		//de aici ruleaza.
		cout << "1. Add\n2. Print\n3. Delete\n4. Update\n5. Find\n6. Filter\n7. Sort\n8. Reteta\n0. Exit\nCommand: ";
		int cmd{ 0 };
		cin >> cmd;
		if (cmd == 0) {
			break;
		}
		if (cmd == 1) {
			string denumire;
			double pret;
			string producator;
			string substanta;
			cout << "Denumire: ";
			cin >> denumire;
			cout << "Pret: ";
			cin >> pret;
			cout << "Producator: ";
			cin >> producator;
			cout << "Substanta: ";
			cin >> substanta;
			try {
				service1.add(denumire, pret, producator, substanta);
				cout << "Medicament adaugat!\n";
			}
			catch (ValidatorException& v) {
				cout << v.getMessage();
			}
			catch (RepoException& e) {
				cout << e.getMessage();
			}
		}
		if (cmd == 2) {
			auto meds = service1.getAll();
			for (const Medicament& Med1 : meds) {
				cout << Med1.getDenumire() << " " << Med1.getPret() << " " << Med1.getProducator() << " " << Med1.getSubstanta() << '\n';
			}
		}
		if (cmd == 3) {
			string denumire, producator;
			cout << "Denumire: ";
			cin >> denumire;
			cout << "Producator: ";
			cin >> producator;
			try {
				service1.del(denumire, producator);
				cout << "Medicament sters!\n";
			}
			catch (RepoException& e) {
				cout << e.getMessage();
			}
		}
		if (cmd == 4) {
			string denumire, producator;
			cout << "Denumire: ";
			cin >> denumire;
			cout << "Producator: ";
			cin >> producator;
			string Denumire, Producator, Substanta;
			double Pret{ 0 };
			cout << "Denumire noua: ";
			cin >> Denumire;
			cout << "Pret nou: ";
			cin >> Pret;
			cout << "Producator nou: ";
			cin >> Producator;
			cout << "Substanta noua: ";
			cin >> Substanta;
			try {
				service1.upd(denumire, producator, Denumire, Pret, Producator, Substanta);
				cout << "Medicament modificat!\n";
			}
			catch (ValidatorException& v) {
				cout << v.getMessage();
			}
			catch (RepoException& e) {
				cout << e.getMessage();
			}
		}
		if (cmd == 5) {
			string denumire, producator;
			cout << "Denumire: ";
			cin >> denumire;
			cout << "Producator: ";
			cin >> producator;
			try {
				Medicament Med1 = service1.fnd(denumire, producator);
				cout << Med1.getDenumire() << " " << Med1.getPret() << " " << Med1.getProducator() << " " << Med1.getSubstanta() << '\n';
			}
			catch (RepoException& e) {
				cout << e.getMessage();
			}
		}
		if (cmd == 6) {
			cout << "1. Pret\n2. Substanta\nCommand: ";
			int choice{ 0 };
			cin >> choice;
			if (choice == 1) {
				cout << "Pret mai mic decat: ";
				int choice2{ 0 };
				cin >> choice2;
				vector<Medicament> filtrate = service1.filter([&](const Medicament& m1) {
					if (m1.getPret() < choice2) return true;
					return false;
					});
				for (const auto& m1 : filtrate) {
					cout << m1.getDenumire() << " " << m1.getPret() << " " << m1.getProducator() << " " << m1.getSubstanta() << '\n';
				}
			}
			else if (choice == 2) {
				cout << "Introdu substanta: ";
				string choice3;
				cin >> choice3;
				vector<Medicament> filtrate = service1.filter([&](const Medicament& m1) {
					if (m1.getSubstanta() == choice3) return true;
					return false;
					});
				for (const auto& m1 : filtrate) {
					cout << m1.getDenumire() << " " << m1.getPret() << " " << m1.getProducator() << " " << m1.getSubstanta() << '\n';
				}
			}
			else {
				cout << "Alegerea este invalida!\n";
			}
		}
		if (cmd == 7) {
			cout << "1. Denumire\n2. Producator\n3. Substanta + Pret\nCommand: ";
			int choice{ 0 };
			cin >> choice;
			if (choice == 1) {
				vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
					return m1.getDenumire() < m2.getDenumire();
					});
				for (const auto& m1 : sortate) {
					cout << m1.getDenumire() << " " << m1.getPret() << " " << m1.getProducator() << " " << m1.getSubstanta() << '\n';
				}
			}
			else if (choice == 2) {
				vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
					return m1.getProducator() < m2.getProducator();
					});
				for (const auto& m1 : sortate) {
					cout << m1.getDenumire() << " " << m1.getPret() << " " << m1.getProducator() << " " << m1.getSubstanta() << '\n';
				}
			}
			else if (choice == 3) {
				vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
					if (m1.getSubstanta() != m2.getSubstanta()) return m1.getSubstanta() < m2.getSubstanta();
					return m1.getPret() < m2.getPret();
					});
				for (const auto& m1 : sortate) {
					cout << m1.getDenumire() << " " << m1.getPret() << " " << m1.getProducator() << " " << m1.getSubstanta() << '\n';
				}
			}
			else {
				cout << "Alegerea este invalida!\n";
			}
		}
		if (cmd == 8) {
			cout << "1. Clear\n2. Write\n3. Generate\n4. Export\nCommand: ";
			int choice{ 0 };
			cin >> choice;
			if (choice == 1) {
				service_reteta.clear();
				cout << "Reteta este acum goala!\n";
			}
			else if (choice == 2) {
				string denumire, producator;
				cout << "Denumire: ";
				cin >> denumire;
				cout << "Producator: ";
				cin >> producator;
				try {
					service_reteta.write(denumire, producator);
				}
				catch (RepoException& e) {
					cout << e.getMessage();
				}
			}
			else if (choice == 3) {
				int elem_nr;
				cout << "Introdu numar de elemente pentru generat: ";
				cin >> elem_nr;
				//adaugam niste date pentru generare.
				vector<string> denumiri, producatori, substante;
				vector<double> preturi;
				denumiri.push_back("Dulcolax");
				denumiri.push_back("Emetix");
				denumiri.push_back("Dulcosolvan");
				denumiri.push_back("GripActiv");
				preturi.push_back(19.99);
				preturi.push_back(21.99);
				preturi.push_back(32.33);
				producatori.push_back("CFR");
				producatori.push_back("SUA");
				substante.push_back("Speis");
				substante.push_back("Cacao");
				substante.push_back("Zahar");
				service_reteta.generate(elem_nr, denumiri, preturi, producatori, substante);
				cout << "Elementele au fost generate cu succes!\n";
			}
			else if (choice == 4) {
				string nume_fisier;
				cout << "Introdu numele fisierului: ";
				cin >> nume_fisier;
				service_reteta.exports(nume_fisier);
				cout << "Reteta a fost exportata cu succes!\n";
			}
		}
	}
}