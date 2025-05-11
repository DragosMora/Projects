#include "Validator.h"
#include <typeinfo>

string ValidatorException::getMessage() const {
	return msg;
}

void Validator::validate(const Medicament& med) const {
	string erori = "";
	if (med.getDenumire() == "") erori += "Denumire invalida!\n";
	if (med.getPret() < 1) erori += "Pret invalid!\n";
	if (med.getProducator() == "") erori += "Producator invalid!\n";
	if (med.getSubstanta() == "") erori += "Substanta invalida!\n";
	if (erori != "") throw ValidatorException(erori);
}