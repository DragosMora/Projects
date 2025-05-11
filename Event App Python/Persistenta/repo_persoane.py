from Erori.erori import RepoError
from Domain.persoana import Persoana

class RepoPersoane:
    def __init__(self):
        """
           Initializeaza repo persoane. 
        """
        self._persoane = {}
        
    def __len__(self):
        """
           Returneaza lungimea dictionarului de persoane. 
        """
        return len(self._persoane)
    
    def get_all(self):
        """
            Returneaza fiecare persoana din dictionar.
        """
        if len(self._persoane) == 0:
            raise RepoError("Lista de persoane este goala!")
        return [str(self._persoane[persoana]) for persoana in self._persoane]
    
    def add_persoana(self, persoana):
        """
           Adauga persoana in repo persoane.
           persoana = persoana adaugata 
        """
        person_id = persoana.get_person_id()
        if person_id in self._persoane:
            raise RepoError("Persoana existenta!")
        self._persoane[person_id] = persoana
        
    def modify_persoana(self, persoana):
        """
            Modifica persoana in repo persoane.
            persoana = persana modificata
        """
        person_id = persoana.get_person_id()
        if person_id not in self._persoane:
            raise RepoError("Persoana nu exista!")
        self._persoane[person_id] = persoana
        
    def del_persoana(self, personID):
        """
            Sterge persoana din repo persoane.
            personID = id-ul persoanei
        """
        if personID not in self._persoane:
            raise RepoError("Persoana nu exista!")
        del self._persoane[personID]
        
    def find_persoana(self, personID):
        """
            Cauta persoana in repo persoane.
            personID = id-ul persoanei
        """
        if personID not in self._persoane:
            raise RepoError("Persoana nu exista!")
        return self._persoane[personID]

    
class FileRepoPersoane(RepoPersoane):
    def __init__(self, file_path):
        """
            Initializeaza file repo persoane.
            file_path = locatia fisierului
        """
        self.__file_path = file_path
        RepoPersoane.__init__(self)
        self.__read_all_persoane_from_file()
        

    def __read_all_persoane_from_file(self):
        """
            Citeste toate persoanele din fisier.
        """
        with open(self.__file_path, "r") as f:
            self._persoane.clear()
            lines = f.readlines()
            c = 0
            for line in lines:
                c += 1
                line = line.strip()
                if line != "":
                    if c % 3 == 1:
                        id_persoana = int(line)
                    elif c % 3 == 2:
                        nume = line
                    elif c % 3 == 0:
                        adresa = line
                        persoana = Persoana(id_persoana, nume, adresa)
                        self._persoane[id_persoana] = persoana    
    
    def __write_all_persoane_to_file(self):
        """
            Scrie toate persoanele in fisier.
        """
        with open(self.__file_path, "w") as f:
            for id_persoana in self._persoane:
                id_persoana = self._persoane[id_persoana].get_person_id()
                nume = self._persoane[id_persoana].get_nume()
                adresa = self._persoane[id_persoana].get_adresa()
                f.write(str(id_persoana) + "\n")
                f.write(nume + "\n")
                f.write(adresa + "\n")
            
    def __len__(self):
        """
            Returneaza lungimea dictionarului de persoane.
        """
        self.__read_all_persoane_from_file()
        return RepoPersoane.__len__(self)
        

    def __append_persoana_to_file(self, persoana):
        """
            Adauga o persoana in fisier.
            persoana = persoana adaugata
        """
        with open(self.__file_path, "a") as f:
            id_persoana = persoana.get_person_id()
            nume = persoana.get_nume()
            adresa = persoana.get_adresa()
            f.write(str(id_persoana) + "\n")
            f.write(nume + "\n")
            f.write(adresa + "\n")
    
    
    def add_persoana(self, persoana):
        """
           Adauga persoana in repo persoane.
           persoana = persoana adaugata 
        """
        self.__read_all_persoane_from_file()
        RepoPersoane.add_persoana(self, persoana)
        self.__append_persoana_to_file(persoana)
        
    def find_persoana(self, personID):
        """
            Cauta persoana in repo persoane.
            personID = id-ul persoanei
        """
        self.__read_all_persoane_from_file()
        return RepoPersoane.find_persoana(self, personID)
    
    def del_persoana(self, personID):
        """
            Sterge o persoana din repo persoane.
            personID = id-ul persoanei
        """
        self.__read_all_persoane_from_file()
        RepoPersoane.del_persoana(self, personID)
        self.__write_all_persoane_to_file()
        
    def modify_persoana(self, persoana):
        """
            Modifica persoana din repo persoane.
            persoana = persoana modificata
        """
        self.__read_all_persoane_from_file()
        RepoPersoane.modify_persoana(self, persoana)
        self.__write_all_persoane_to_file()
    



















