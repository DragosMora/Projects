from Domain.eveniment import Eveniment

class ServiceEvenimente:
    def __init__(self, validator_eveniment, repo_evenimente):
        """
           Initializeaza service evenimente. 
           validator_eveniment = validatorul pentru eveniment
           repo_eveniment = repo pentru eveniment
        """
        self.__validator_eveniment = validator_eveniment
        self.__repo_evenimente = repo_evenimente
        
    def __len__(self):
        """
           Returneaza lungimea lui repo_evenimente. 
        """
        return len(self.__repo_evenimente)
    
    def get_all(self):
        """
            Returneaza fiecare eveniment din repo.
        """
        return self.__repo_evenimente.get_all()
        
    def add_eveniment(self, ID, data, timp, descriere):
        """
           Creeaza un eveniment, il valideaza si il adauga in repo evenimente.
           ID = id-ul evenimentului
           data = data evenimentului
           timp = timpul evenimentului
           descriere = descrierea evenimentului
        """
        eveniment = Eveniment(ID, data, timp, descriere)
        self.__validator_eveniment.validate(eveniment)
        self.__repo_evenimente.add_eveniment(eveniment)
        
    def modify_eveniment(self, ID, data, timp, descriere):
        """
           Creeaza un eveniment, il valideaza si il modifica in repo evenimente.
           ID = id-ul evenimentului
           data = data evenimentului
           timp = timpul evenimentului
           descriere = descrierea evenimentului
        """
        eveniment = Eveniment(ID, data, timp, descriere)
        self.__validator_eveniment.validate(eveniment)
        self.__repo_evenimente.modify_eveniment(eveniment)
        
    def del_eveniment(self, ID):
        """
            Valideaza id-ul si sterge evenimentul din repo evenimente.
            ID = id-ul evenimentului
        """
        self.__validator_eveniment.validate_id(ID)
        self.__repo_evenimente.del_eveniment(ID)
        
    def find_eveniment(self, ID):
        """
            Valideaza id-ul si cauta evenimentul in repo evenimente.
            ID = id-ul evenimentului
        """
        self.__validator_eveniment.validate_id(ID)
        return self.__repo_evenimente.find_eveniment(ID)
        


