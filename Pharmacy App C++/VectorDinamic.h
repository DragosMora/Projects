#pragma once
template <typename TElem>
class IteratorVectorT;

template <typename TElem>
class VectorDinamic {
private:
	int cap;
	int lg;
	TElem* elems;
public:
	/*
	Constructor default.
	*/
	VectorDinamic();

	/*
	Constructor de copiere.
	ot = referinta la celalalt vector.
	*/
	VectorDinamic(const VectorDinamic& ot);

	/*
	Destructor instanta VectorDinamic.
	*/
	~VectorDinamic();

	/*
	Operator assigment.
	ot = referinta la instanta din clasa VectorDinamic.
	*/
	VectorDinamic& operator=(const VectorDinamic& ot);

	/*
	Verifica daca trebuie facut redimensionare si daca trebuie face.
	*/
	void resize();

	/*
	Adauga un element la finalul vectorului.
	med = referinta la o instanta din clasa Medicament.
	preconditii: nu exista.
	postconditii: se adauga elementul in vector.
	*/
	void push_back(const TElem& med);

	/*
	Sterge un element din vectorul dinamic.
	poz = integer pozitie unde sterge.
	preconditii: nu exista.
	postconditii: se sterge elementul gasit sau se arunca o exceptie.
	*/
	void erase(const int poz);

	/*
	Insereaza un medicament pe o pozitie in vector.
	poz = integer pozitie inserare.
	med = referinta la o instanta din clasa medicament.
	preconditii: nu exista.
	postconditii: se insereaza elementul in vector.
	*/
	void insert(const int poz, const TElem& med);

	/*
	Obtine un element din vector.
	poz = integer pozitie din vector.
	preconditii: nu exista.
	postconditii: se obtine o referinta la medicament.
	Returneaza o referinta la element.
	*/
	TElem& get(int poz) const;

	/*
	Seteaza la o pozitie un medicament.
	poz = integer pozitie din vector.
	med = referinta la instanta din clasa Medicament.
	preconditii: nu exista.
	postconditii: se seteaza la pozitia respectiva elementul.
	*/
	void set(int poz, const TElem& med);

	/*
	Obtine dimensiunea vectorului.
	Returneaza dimensiunea vectorului.
	*/
	int size() const;

	//aici iterator si functii care creaza iteratori.

	friend class IteratorVectorT<TElem>;
	IteratorVectorT<TElem> begin();
	IteratorVectorT<TElem> end();
};

template<typename TElem>
class IteratorVectorT {
private:
	const VectorDinamic<TElem>& v;
	int poz = 0;
public:
	/*
	Constructor iterator.
	v = instanta din clasa vector dinamic.
	preconditii: nu exista.
	postconditii: se initializeaza iteratorul.
	*/
	IteratorVectorT(const VectorDinamic<TElem>& v) noexcept;

	/*
	Constructor iterator.
	v = instanta din clasa vector dinamic.
	poz = integer pozitie.
	preconditii: nu exista.
	postconditii: se initializeaza iteratorul.
	*/
	IteratorVectorT(const VectorDinamic<TElem>& v, int poz) noexcept;

	/*
	Verifica daca am ajuns la finalul vectorului.
	Returneaza pozitia la care suntem in vector.
	*/
	bool valid() const;

	/*
	Returneaza elementul de pe pozitia curenta din vector.
	*/
	TElem& element() const;

	/*
	Incrementeaza pozitia din vector.
	*/
	void next();

	/*
	Apeleaza metoda element.
	*/
	TElem& operator*();

	/*
	Apeleaza metoda next.
	Returneaza instanta curenta.
	*/
	IteratorVectorT& operator++();

	/*
	Compara pozitiile a doi iteratori.
	ot = instanta din clasa iterator.
	preconditii: nu exista.
	postconditii: verifica daca pozitia iteratorului este egala cu pozitia lui ot.
	Returneaza true daca cele doua pozitii sunt egale.
	*/
	bool operator==(const IteratorVectorT& ot) noexcept;

	/*
	Compara pozitiile a doi iteratori.
	ot = instanta din clasa iterator.
	preconditii: nu exista.
	postconditii: verifica daca pozitia iteratorului nu este egala cu pozitia lui ot.
	Returneaza true daca cele doua pozitii sunt diferite.
	*/
	bool operator!=(const IteratorVectorT& ot) noexcept;
};


template<typename TElem>
VectorDinamic<TElem>::VectorDinamic() : cap{ 10 }, lg{ 0 }, elems{ new TElem[cap] } {}

template<typename TElem>
VectorDinamic<TElem>::VectorDinamic(const VectorDinamic<TElem>& ot) {
	elems = new TElem[ot.cap];
	for (int i = 0; i < ot.lg; i++) {
		elems[i] = ot.elems[i];
	}
	lg = ot.lg;
	cap = ot.cap;
}

template<typename TElem>
VectorDinamic<TElem>::~VectorDinamic() {
	delete[] elems;
}

template<typename TElem>
VectorDinamic<TElem>& VectorDinamic<TElem>::operator=(const VectorDinamic<TElem>& ot) {
	if (this == &ot) {
		return *this;
	}
	delete[] elems;
	elems = new TElem[ot.cap];
	for (int i = 0; i < ot.lg; i++) {
		elems[i] = ot.elems[i];
	}
	lg = ot.lg;
	cap = ot.cap;
	return *this;
}

template<typename TElem>
void VectorDinamic<TElem>::resize() {
	if (cap == lg) {
		TElem* aux = new TElem[cap * 2];
		for (int i = 0; i < lg; i++) {
			aux[i] = elems[i];
		}
		delete[] elems;
		elems = aux;
		cap = cap * 2;
	}
}

template<typename TElem>
void VectorDinamic<TElem>::push_back(const TElem& med) {
	resize();
	elems[lg++] = med;
}

template<typename TElem>
void VectorDinamic<TElem>::erase(const int poz) {
	//posibil memory leak pentru ca nu dealoci medicamentul de pe pozitie.
	for (int i = poz; i < lg - 1; i++) {
		elems[i] = elems[i + 1];
	}
	lg--;
}

template<typename TElem>
void VectorDinamic<TElem>::insert(const int poz, const TElem& med) {
	resize();
	for (int i = lg + 1; i > poz; i--) {
		elems[i] = elems[i - 1];
	}
	elems[poz] = med;
	lg++;
}

template<typename TElem>
TElem& VectorDinamic<TElem>::get(int poz) const {
	return elems[poz];
}

template<typename TElem>
void VectorDinamic<TElem>::set(int poz, const TElem& med) {
	elems[poz] = med;
}

template<typename TElem>
int VectorDinamic<TElem>::size() const {
	return lg;
}

template<typename TElem>
IteratorVectorT<TElem> VectorDinamic<TElem>::begin() {
	return IteratorVectorT<TElem>(*this);
}

template<typename TElem>
IteratorVectorT<TElem> VectorDinamic<TElem>::end() {
	return IteratorVectorT<TElem>(*this, lg);
}

template<typename TElem>
IteratorVectorT<TElem>::IteratorVectorT(const VectorDinamic<TElem>& v) noexcept : v{ v } {}

template<typename TElem>
IteratorVectorT<TElem>::IteratorVectorT(const VectorDinamic<TElem>& v, int poz) noexcept : v{ v }, poz{ poz } {}

template<typename TElem>
bool IteratorVectorT<TElem>::valid() const {
	return poz < v.lg;
}

template<typename TElem>
TElem& IteratorVectorT<TElem>::element() const {
	return v.elems[poz];
}

template<typename TElem>
void IteratorVectorT<TElem>::next() {
	poz++;
}

template<typename TElem>
TElem& IteratorVectorT<TElem>::operator*() {
	return element();
}

template<typename TElem>
IteratorVectorT<TElem>& IteratorVectorT<TElem>::operator++() {
	next();
	return *this;
}

template<typename TElem>
bool IteratorVectorT<TElem>::operator==(const IteratorVectorT<TElem>& ot) noexcept {
	return poz == ot.poz;
}

template<typename TElem>
bool IteratorVectorT<TElem>::operator!=(const IteratorVectorT<TElem>& ot) noexcept {
	return !(*this == ot);
}