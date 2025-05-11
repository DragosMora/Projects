from Erori.erori import RepoError
from Domain.eveniment import Eveniment

class RepoEvenimente:
    def __init__(self):
        """
           Initializeaza repo evenimente. 
        """
        self._evenimente = {}
        
    def __len__(self):
        """
           Returneaza lungimea dictionarului de evenimente. 
        """
        return len(self._evenimente)
    
    def get_all(self):
        """
            Returneaza fiecare eveniment din dictionar.
        """
        if len(self._evenimente) == 0:
            raise RepoError("Lista de evenimente este goala!")
        return [str(self._evenimente[eveniment]) for eveniment in self._evenimente]
    
    def add_eveniment(self, eveniment):
        """
           Adauga eveniment in repo evenimente.
           eveniment = evenimentul adaugat 
        """
        eveniment_id = eveniment.get_id()
        if eveniment_id in self._evenimente:
            raise RepoError("Eveniment existent!")
        self._evenimente[eveniment_id] = eveniment
        
    def modify_eveniment(self, eveniment):
        """
            Modifica eveniment in repo evenimente.
            eveniment = eveniment modificat
        """
        eveniment_id = eveniment.get_id()
        if eveniment_id not in self._evenimente:
            raise RepoError("Evenimentul nu exista!")
        self._evenimente[eveniment_id] = eveniment
        
    def del_eveniment(self, ID):
        """
            Sterge eveniment din repo evenimente.
            ID = id-ul evenimentului
        """
        if ID not in self._evenimente:
            raise RepoError("Evenimentul nu exista!")
        del self._evenimente[ID]
        
    def find_eveniment(self, ID):
        """
            Cauta evenimentul in repo evenimente.
            ID = id-ul evenimentului
        """
        if ID not in self._evenimente:
            raise RepoError("Evenimentul nu exista!")
        return self._evenimente[ID]
        
        
class FileRepoEvenimente(RepoEvenimente):
    def __init__(self, file_path):
        """
            Initializeaza file repo evenimente.
            file_path = locatia fisierului
        """
        self.__file_path = file_path
        RepoEvenimente.__init__(self)
        self.__read_all_evenimente_from_file()

    def __read_all_evenimente_from_file(self):
        """
            Citeste toate evenimentele din fisier.
        """
        with open(self.__file_path, "r") as f:
            self._evenimente.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parti = line.split(",")
                    id_eveniment = int(parti[0])
                    data = parti[1]
                    timp = parti[2]
                    descriere = parti[3]
                    eveniment = Eveniment(id_eveniment, data, timp, descriere)
                    self._evenimente[id_eveniment] = eveniment
                    
    def __write_all_evenimente_to_file(self):
        """
            Scrie toate evenimentele in fisier.
        """
        with open(self.__file_path, "w") as f:
            for id_eveniment in self._evenimente:
                f.write(repr(self._evenimente[id_eveniment]) + "\n")
                
    def __len__(self):
        """
            Returneaza lungimea dictionarului de evenimente.
        """
        self.__read_all_evenimente_from_file()
        return RepoEvenimente.__len__(self)
    
    def __append_eveniment_to_file(self, eveniment):
        """
            Adauga un eveniment in fisier.
            eveniment = evenimentul adaugat
        """
        with open(self.__file_path, "a") as f:
            f.write(repr(eveniment) + "\n")
            
    def add_eveniment(self, eveniment):
        """
            Adauga eveniment in repo evenimente.
            eveniment = evenimentul adaugat
        """
        self.__read_all_evenimente_from_file()
        RepoEvenimente.add_eveniment(self, eveniment)
        self.__append_eveniment_to_file(eveniment)
        
    def find_eveniment(self, ID):
        """
            Cauta eveniment in repo evenimente.
            ID = id-ul evenimentului
        """
        self.__read_all_evenimente_from_file()
        return RepoEvenimente.find_eveniment(self, ID)
    
    def del_eveniment(self, ID):
        """
            Sterge un eveniment din repo evenimente.
            ID = id-ul evenimentului
        """
        self.__read_all_evenimente_from_file()
        RepoEvenimente.del_eveniment(self, ID)
        self.__write_all_evenimente_to_file()
        
    def modify_eveniment(self, eveniment):
        """
            Modifica un eveniment din repo evenimente.
            eveniment = evenimentul modificat
        """
        self.__read_all_evenimente_from_file()
        RepoEvenimente.modify_eveniment(self, eveniment)
        self.__write_all_evenimente_to_file()














