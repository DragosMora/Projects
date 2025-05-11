from Domain.biletDTO import BiletDTO
import sortari

class ServiceBilete:
    def __init__(self, repo_persoane, repo_evenimente, repo_bilete):
        """
            Initializeaza service bilete.
            repo_persoane = repo pentru persoane
            repo_evenimente = repo pentru evenimente
            repo_bilete = repo pentru bilete
        """
        self.__repo_persoane = repo_persoane
        self.__repo_evenimente = repo_evenimente
        self.__repo_bilete = repo_bilete
        
    def __len__(self):
        """
            Returneaza lungimea lui repo bilete.
        """
        return len(self.__repo_bilete)
    
    def get_all(self):
        """
            Returneaza fiecare bilet din repo.
        """
        return self.__repo_bilete.get_all()
        
    def add_bilet(self, id_bilet, id_persoana, id_eveniment):
        """
            Creeaza un bilet daca exista persoana si evenimentul respectiv si il adauga in repo bilete.
            id_bilet = id-ul biletului
            id_persoana = id-ul persoanei
            id_eveniment = id-ul evenimentului
        """
        self.__repo_persoane.find_persoana(id_persoana)
        self.__repo_evenimente.find_eveniment(id_eveniment)
        bilet = BiletDTO(id_bilet, id_persoana, id_eveniment)
        self.__repo_bilete.add_bilet(bilet)
        
    def __sortare_descriere(self, lista_evenimente):
        """
            Sorteaza o lista dupa descriere.
            lista_evenimente = lista de evenimente
        """
        sortari.shaker_sort(lista_evenimente, key = lambda x:x.get_descriere())
        #lista_evenimente.sort(key = lambda x:x.get_descriere())
        return lista_evenimente
        
    def rap_desc(self, id_persoana):
        """
            Returneaza o lista de evenimente la care participa o persoana sortata dupa descriere.
            id_persoana = id-ul persoanei
        """
        self.__repo_persoane.find_persoana(id_persoana)
        lista_bilete = self.__repo_bilete.get_all()
        lista_evenimente = []
        for bilet in lista_bilete:
            if bilet.get_person_id() == id_persoana:
                id_eveniment = bilet.get_eveniment_id()
                eveniment = self.__repo_evenimente.find_eveniment(id_eveniment)
                lista_evenimente.append(eveniment)
        lista_sortata = self.__sortare_descriere(lista_evenimente)
        return lista_sortata
    
    def __criteriu_sortare_data(self, eveniment):
        """
            Aplica criteriile pentru sortarea listei de evenimente.
            lista_evenimente = lista de evenimente
            Returneaza anul, luna si ziua pentru a fi comparate.
        """
        data_eveniment = eveniment.get_data()
        parti = data_eveniment.split(".")
        zi = int(parti[0])
        luna = int(parti[1])
        an = int(parti[2])
        return an, luna, zi
    
    def __sortare_data(self, lista_evenimente):
        """
            Sorteaza o lista dupa data.
            lista_evenimente = lista de evenimente
            Returneaza lista de evenimente sortata dupa data.
        """
        sortari.selection_sort(lista_evenimente, key = lambda x:self.__criteriu_sortare_data(x))
        return lista_evenimente
    
    def rap_data(self, id_persoana):
        """
            Returneaza o lista de evenimente la care participa o persoana sortata dupa data.
            id_persoana = id-ul persoanei
        """
        self.__repo_persoane.find_persoana(id_persoana)
        lista_bilete = self.__repo_bilete.get_all()
        lista_evenimente = []
        for bilet in lista_bilete:
            if bilet.get_person_id() == id_persoana:
                id_eveniment = bilet.get_eveniment_id()
                eveniment = self.__repo_evenimente.find_eveniment(id_eveniment)
                lista_evenimente.append(eveniment)
        lista_sortata = self.__sortare_data(lista_evenimente)
        return lista_sortata
    
    def __recursive_cauta_maxim_persoana(self, lista_id_persoane, lista_bilete, Max):
        """
            Returneaza numarul de persoane participante la cele mai multe evenimente.
            lista_id_persoane = lista cu id-ul persoanelor
            lista_bilete = lista cu bilete
            Max = numarul maxim gasit
        """
        if lista_id_persoane == []:
            return Max
        lista_bilete_copy = lista_bilete
        counter = 0
        for bilet in lista_bilete:
            if lista_id_persoane[0] == bilet.get_person_id():
                counter += 1
        if counter > Max:
            Max = counter
        return self.__recursive_cauta_maxim_persoana(lista_id_persoane[1:], lista_bilete_copy, Max)
        
    def __recursive_lista_maxim(self, lista_id_persoane, lista_bilete, maxim, lista):
        """
            Transmite functiei rap_pers o lista cu numarul de persoane participante la cele mai multe evenimente.
            lista_id_persoane = lista cu id-ul persoanelor
            lista_bilete = lista cu bilete
            maxim = numarul maxim
        """
        if lista_id_persoane == []:
            return lista
        lista_bilete_copy = lista_bilete
        counter = 0
        for bilet in lista_bilete:
            if lista_id_persoane[0] == bilet.get_person_id():
                counter += 1
        if counter == maxim:
            lista.append(lista_id_persoane[0])
        return self.__recursive_lista_maxim(lista_id_persoane[1:], lista_bilete_copy, maxim, lista)
    
    def rap_pers(self):
        """
            Returneaza o lista de persoane participante la cele mai multe evenimente.
        """
        lista_bilete = self.__repo_bilete.get_all()
        lista_id_persoane = []
        for bilet in lista_bilete:
            id_persoana = bilet.get_person_id()
            if id_persoana not in lista_id_persoane:
                lista_id_persoane.append(id_persoana)
        maxim = self.__recursive_cauta_maxim_persoana(lista_id_persoane, lista_bilete, 0)
        lista_participari_maxime = self.__recursive_lista_maxim(lista_id_persoane, lista_bilete, maxim, [])
        
        lista_persoane = []
        for id_persoana in lista_participari_maxime:
            persoana = self.__repo_persoane.find_persoana(id_persoana)
            lista_persoane.append(persoana)
        return maxim, lista_persoane
    
    def __lista_evenimente_participanti(self, lista_id_evenimente, lista_bilete):
        """
            Returneaza o lista de evenimente si numarul de participanti.
            lista_id_evenimente = lista cu id-ul evenimentelor
            lista_bilete = lista cu bilete
        """
        lista = []
        for id_eveniment in lista_id_evenimente:
            counter = 0
            for bilet in lista_bilete:
                if id_eveniment == bilet.get_eveniment_id():
                    counter += 1
            eveniment = self.__repo_evenimente.find_eveniment(id_eveniment)
            descriere = eveniment.get_descriere()
            lista.append([id_eveniment, counter, descriere])
        return lista
    
    def __lista_descrescatoare(self, lista):
        """
            Sorteaza lista de evenimente dupa numarul de participanti.
            lista = lista nesortata
        """
        lista.sort(key = lambda x:x[1], reverse = True)
        return lista
    
    def rap_20(self):
        """
            Returneaza primele 20% evenimente cu cei mai multi participanti.
        """
        lista_bilete = self.__repo_bilete.get_all()
        lista_id_evenimente = []
        for bilet in lista_bilete:
            id_eveniment = bilet.get_eveniment_id()
            if id_eveniment not in lista_id_evenimente:
                lista_id_evenimente.append(id_eveniment)
        lista_nesortata = self.__lista_evenimente_participanti(lista_id_evenimente, lista_bilete)
        lista_sortata = self.__lista_descrescatoare(lista_nesortata)
        lungime = int(len(lista_sortata) * 0.2)
        return lista_sortata[:lungime]
        
    
        
            
    
    
    
    
    
    


