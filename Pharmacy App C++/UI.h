#pragma once
#include "Service.h"
#include "ServiceReteta.h"

class UI {
private:
	Service& service1;
	ServiceReteta& service_reteta;
public:
	/*
	Constructor pentru clasa UI.
	serv = instanta a clasei Service.
	Returneaza o instanta a clasei Service.
	*/
	UI(Service& serv, ServiceReteta& servr) : service1{ serv }, service_reteta{ servr } {

	}

	/*
	Ruleaza UI.
	*/
	void run();
};
