#include "Teste.h"
#include "Medicament.h"
#include "Validator.h"
#include "Repo.h"
#include "Service.h"
#include <assert.h>
#include "VectorDinamic.h"
#include "RepoReteta.h"
#include "ServiceReteta.h"

void Teste::ruleaza_toate_testele() const {
	domain_tests();
	validator_tests();
	repo_tests();
	service_tests();
	vector_dinamic_tests();
	repo_reteta_tests();
	service_reteta_tests();
}

void Teste::domain_tests() const {
	Medicament Med1{ "Dicarbocalm", 19.99, "CFR", "Speis" };
	assert(Med1.getDenumire() == "Dicarbocalm");
	assert(Med1.getPret() == 19.99);
	assert(Med1.getProducator() == "CFR");
	assert(Med1.getSubstanta() == "Speis");
}

void Teste::validator_tests() const {
	Medicament Med_invalid("", -10, "", "");
	Validator v1;
	try {
		v1.validate(Med_invalid);
	}
	catch (ValidatorException& v) {
		assert(v.getMessage() != "");
	}
}

void Teste::repo_tests() const {
	Repo repo1;
	Medicament Med1{ "Analgezic", 12.49, "Catena", "Boaba" };
	repo1.store(Med1);
	const auto& meds = repo1.getAll();
	assert(meds.size() == 1);
	try {
		repo1.store(Med1);
		//assert(false);
	}
	catch (RepoException& e) {
		assert(e.getMessage() != "");
	}
	Medicament Med2{ "Dulcolax", 19.99, "Catena", "Speis" };
	repo1.store(Med2);

	repo1.erase("Dulcolax", "Catena");
	const auto& meds2 = repo1.getAll();
	assert(meds2.size() == 1);
	try {
		repo1.erase("Dulcolax", "Catena");
		//assert(false);
	}
	catch (RepoException& e) {
		assert(e.getMessage() != "");
	}
	repo1.erase("Analgezic", "Catena");
	const auto& meds3 = repo1.getAll();
	assert(meds3.size() == 0);

	Medicament Med3{ "Sanohepat-Slim", 31.99, "Catena", "LSD" };
	repo1.store(Med3);
	repo1.store(Med1);
	repo1.update("Analgezic", "Catena", Med2);
	const auto& meds4 = repo1.getAll();
	assert(meds4.size() == 2);
	Medicament aux = meds4[1];
	assert(aux.getDenumire() == "Dulcolax");
	assert(aux.getPret() == 19.99);
	assert(aux.getProducator() == "Catena");
	assert(aux.getSubstanta() == "Speis");
	try {
		repo1.update("ceva", "altceva", Med2);
		//assert(false);
	}
	catch (RepoException& e) {
		assert(e.getMessage() != "");
	}

	Medicament aux2 = repo1.find("Dulcolax", "Catena");
	assert(aux2.getDenumire() == "Dulcolax");
	assert(aux2.getPret() == 19.99);
	assert(aux2.getProducator() == "Catena");
	assert(aux2.getSubstanta() == "Speis");

	try {
		Medicament aux3 = repo1.find("ceva", "altceva");
		//assert(false);
	}
	catch (RepoException& e) {
		assert(e.getMessage() != "");
	}
}

void Teste::service_tests() const {
	Repo repo1;
	Service service1{ repo1 };
	service1.add("Dulcolax", 27.99, "BigPharma", "Smekerie");
	const auto& meds = service1.getAll();
	assert(meds.size() == 1);
	try {
		service1.add("Dulcolax", 27.99, "BigPharma", "Smekerie");
		//assert(false);
	}
	catch (RepoException& e) {
		assert(e.getMessage() != "");
	}
	service1.del("Dulcolax", "BigPharma");
	const auto& meds2 = service1.getAll();
	assert(meds2.size() == 0);

	service1.add("Sanohepat", 19.99, "Catena", "LSD");
	service1.upd("Sanohepat", "Catena", "Analgezic", 21.99, "Catena", "Speed");
	const auto& meds3 = service1.getAll();
	assert(meds3.size() == 1);
	Medicament aux = meds3[0];
	assert(aux.getDenumire() == "Analgezic");
	assert(aux.getPret() == 21.99);
	assert(aux.getProducator() == "Catena");
	assert(aux.getSubstanta() == "Speed");

	Medicament aux2 = service1.fnd("Analgezic", "Catena");
	assert(aux2.getDenumire() == "Analgezic");
	assert(aux2.getPret() == 21.99);
	assert(aux2.getProducator() == "Catena");
	assert(aux2.getSubstanta() == "Speed");
	int choice2 = 25;
	vector<Medicament> filtrate = service1.filter([&](const Medicament& m1) {
		if (m1.getPret() < choice2) return true;
		});
	//std::cout << service1.getAll().size();
	service1.add("Emetix", 20, "LSD", "CFR");
	vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
		return m1.getDenumire() < m2.getDenumire();
		});
}

void Teste::vector_dinamic_tests() const {
	VectorDinamic<Medicament> vec1;
	Medicament med1{ "Dulcosolvan", 19.99, "CFR", "Speis" };
	vec1.push_back(med1);
	assert(vec1.size() == 1);
	VectorDinamic<Medicament> vec2;
	Medicament med2{ "Docosan", 19.99, "CFR", "LSD" };
	Medicament med3{ "Emetix", 24.99, "CCC", "Speis" };
	vec2.push_back(med2);
	vec2.push_back(med3);
	assert(vec2.size() == 2);
	vec1 = vec2;
	assert(vec1.size() == 2);
	vec1.erase(0);
	assert(vec1.size() == 1);
	vec1.push_back(med3);
	assert(vec1.size() == 2);
	Medicament med4{ "Encefaz", 21.45, "LPS", "SPEED" };
	vec1.insert(1, med4);
	assert(vec1.size() == 3);
	Medicament med5 = vec1.get(1);
	assert(med4.getDenumire() == med5.getDenumire());
	assert(med4.getPret() == med5.getPret());
	assert(med4.getProducator() == med5.getProducator());
	assert(med4.getSubstanta() == med5.getSubstanta());

	//testele pentru iterator.
	IteratorVectorT<Medicament> itv = vec1.begin();
	assert(itv == vec1);
	IteratorVectorT<Medicament> itv2 = vec1.end();
	IteratorVectorT<Medicament> itv1{ vec1, vec1.size() };
	assert(itv2 == itv1);
	assert(!itv2.valid());
	IteratorVectorT<Medicament> itv3{ vec1, 0 };
	Medicament med6 = itv3.element();
	assert(med6.getDenumire() == med3.getDenumire());
	assert(med6.getPret() == med3.getPret());
	assert(med6.getProducator() == med3.getProducator());
	assert(med6.getSubstanta() == med3.getSubstanta());
	itv3.next();
	Medicament med7 = itv3.element();
	assert(med7.getDenumire() == med4.getDenumire());
	assert(med7.getPret() == med4.getPret());
	assert(med7.getProducator() == med4.getProducator());
	assert(med7.getSubstanta() == med4.getSubstanta());
	Medicament med8 = *itv3;
	assert(med8.getDenumire() == med4.getDenumire());
	assert(med8.getPret() == med4.getPret());
	assert(med8.getProducator() == med4.getProducator());
	assert(med8.getSubstanta() == med4.getSubstanta());
	IteratorVectorT<Medicament> itv4{ vec1, 0 };
	++itv4;
	assert(itv4.valid());
	IteratorVectorT<Medicament> itv5{ vec1, 0 };
	assert(itv5 != itv4);

	//alte teste
	vec1 = vec1;
	VectorDinamic<Medicament> vec3 = vec1;
	assert(vec3.size() == 3);
	for (int i = 0; i < 3; i++) vec3.erase(0);
	assert(vec3.size() == 0);
	for (int i = 0; i < 12; i++) vec3.push_back(med1);
	assert(vec3.size() == 12);
	vec3.set(0, med2);
	Medicament med9 = vec3.get(0);
	assert(med9.getDenumire() == med2.getDenumire());
	assert(med9.getPret() == med2.getPret());
	assert(med9.getProducator() == med2.getProducator());
	assert(med9.getSubstanta() == med2.getSubstanta());
}

void Teste::repo_reteta_tests() const {
	RepoReteta re1;
	Medicament med1{ "Dulcolax", 19.99, "CFR", "Speis" };
	re1.write(med1);
	assert(re1.dim() == 1);
	Medicament med2{ "Dulcosolvan", 21.59, "CFR", "Speis" };
	re1.write(med2);
	assert(re1.dim() == 2);
	re1.clear();
	assert(re1.dim() == 0);
	re1.write(med1);
	re1.write(med2);
	assert(re1.dim() == 2);
	vector<Medicament> meds = re1.get_all();
	assert(meds.size() == 2);
	re1.exports("reteta_test.txt");
}

void Teste::service_reteta_tests() const {
	Repo r1;
	Medicament med1{ "Dulcolax", 19.99, "CFR", "Speis" };
	r1.store(med1);
	RepoReteta re1;
	ServiceReteta se1{ re1, r1 };
	se1.write("Dulcolax", "CFR");
	assert(se1.dim() == 1);
	se1.clear();
	assert(se1.dim() == 0);
	se1.write("Dulcolax", "CFR");
	se1.exports("reteta_test.txt");
	se1.clear();

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
	se1.generate(3, denumiri, preturi, producatori, substante);
	assert(se1.dim() == 3);
	vector<Medicament> meds = se1.get_all();
	assert(meds.size() == 3);
	se1.exports("reteta_test.txt");
}