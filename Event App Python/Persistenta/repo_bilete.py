from Erori.erori import RepoError
from Domain.biletDTO import BiletDTO

class RepoBilete:
    def __init__(self):
        """
            Initializeaza repo bilete.
        """
        self._bilete = {}
        
    def __len__(self):
        """
            Returneaza lungimea dictionarului de bilete.
        """
        return len(self._bilete)
    
    def get_all(self):
        """
            Returneaza fiecare bilet din dictionar.
        """
        if len(self._bilete) == 0:
            raise RepoError("Lista de bilete este goala!")
        return [self._bilete[bilet] for bilet in self._bilete]
    
    def add_bilet(self, bilet):
        """
            Adauga bilet in repo bilete.
            bilet = biletul adaugat
        """
        bilet_id = bilet.get_bilet_id()
        if bilet_id in self._bilete:
            raise RepoError("Bilet existent!")
        self._bilete[bilet_id] = bilet


class FileRepoBilete(RepoBilete):
    def __init__(self, file_path):
        """
            Initializeaza file repo bilete.
            file_path = locatia fisierului
        """
        self.__file_path = file_path
        RepoBilete.__init__(self)
        self.__read_all_bilete_from_file()
        
    def __read_all_bilete_from_file(self):
        """
            Citeste toate biletele din fisier.
        """
        with open(self.__file_path, "r") as f:
            self._bilete.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parti = line.split(",")
                    id_bilet = int(parti[0])
                    id_persoana = int(parti[1])
                    id_eveniment = int(parti[2])
                    bilet = BiletDTO(id_bilet, id_persoana, id_eveniment)
                    self._bilete[id_bilet] = bilet
                
    def __len__(self):
        """
            Returneaza lungimea dictionarului bilete.
        """
        self.__read_all_bilete_from_file()
        return RepoBilete.__len__(self)
    
    def __append_bilet_to_file(self, bilet):
        """
            Adauga un bilet in fisier.
            bilet = biletul adaugat
        """
        with open(self.__file_path, "a") as f:
            f.write(repr(bilet) + "\n")
            
    def add_bilet(self, bilet):
        """
            Adauga un bilet in repo bilete.
            bilet = biletul adaugat
        """
        self.__read_all_bilete_from_file()
        RepoBilete.add_bilet(self, bilet)
        self.__append_bilet_to_file(bilet)
        


















