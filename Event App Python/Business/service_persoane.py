from Domain.persoana import Persoana

class ServicePersoane:
    def __init__(self, validator_persoana, repo_persoane):
        """
            Initializeaza service persoane.
            validator_persoana = validatorul pentru persoana
            repo_persoane = repo pentru persoane
        """
        self.__validator_persoana = validator_persoana
        self.__repo_persoane = repo_persoane
        
    def __len__(self):
        """
           Returneaza lungimea lui repo_persoane. 
        """
        return len(self.__repo_persoane)
    
    def get_all(self):
        """
            Returneaza fiecare persoana din repo.
        """
        return self.__repo_persoane.get_all()
    
    def add_persoana(self, personID, nume, adresa):
        """
           Creeaza o persoana, o valideaza si o adauga in repo persoane.
           personID = id-ul persoanei
           nume = numele persoanei
           adresa = adresa persoanei 
        """
        persoana = Persoana(personID, nume, adresa)
        self.__validator_persoana.validate(persoana)
        self.__repo_persoane.add_persoana(persoana)
        
    def modify_persoana(self, personID, nume, adresa):
        """
            Creeaza o persoana, o valideaza si o modifica in repo persoane.
            personID = id-ul persoanei
            nume = numele persoanei
            adresa = adresa persoanei
        """
        persoana = Persoana(personID, nume, adresa)
        self.__validator_persoana.validate(persoana)
        self.__repo_persoane.modify_persoana(persoana)
        
    def del_persoana(self, personID):
        """
            Valideaza id-ul si sterge persoana din repo persoane.
            personID = id-ul persoanei
        """
        self.__validator_persoana.validate_id(personID)
        self.__repo_persoane.del_persoana(personID)
        
    def find_persoana(self, personID):
        """
            Valideaza id-ul si cauta persoana in repo persoane.
            personID = id-ul persoanei
        """
        self.__validator_persoana.validate_id(personID)
        return self.__repo_persoane.find_persoana(personID)
