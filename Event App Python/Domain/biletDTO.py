class BiletDTO:
    def __init__(self, biletID, personID, evenimentID):
        """
            Initializeaza biletul de inscriere.
            biletID = id-ul biletului
            personID = id-ul persoanei care primeste biletul
            evenimentID = id-ul evenimentului
        """
        self.__biletID = biletID
        self.__personID = personID
        self.__evenimentID = evenimentID

    def get_bilet_id(self):
        """
            Getter method pentru biletID.
        """
        return self.__biletID


    def get_person_id(self):
        """
            Getter method pentru personID.
        """
        return self.__personID


    def get_eveniment_id(self):
        """
            Getter method pentru evenimentID.
        """
        return self.__evenimentID
    
    def __str__(self):
        """
            __str__ method pentru biletDTO.
        """
        return f"[{self.__biletID}] {self.__personID}, {self.__evenimentID}"
    
    def __repr__(self):
        """
            __repr__ method pentru biletDTO.
        """
        return f"{self.__biletID},{self.__personID},{self.__evenimentID}"
    
    
        
    


