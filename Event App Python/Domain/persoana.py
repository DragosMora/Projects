class Persoana:
    def __init__(self, personID, nume, adresa):
        """
           Initializeaza persoana.
           personID = id-ul persoanei
           nume = numele persoanei
           adresa = adresa persoanei 
        """
        self.__personID = personID
        self.__nume = nume
        self.__adresa = adresa

    def get_person_id(self):
        """
           Getter method pentru id-ul persoanei. 
        """
        return self.__personID


    def get_nume(self):
        """
           Getter method pentru numele persoanei. 
        """
        return self.__nume


    def get_adresa(self):
        """
           Getter method pentru adresa persoanei. 
        """
        return self.__adresa


    def set_nume(self, value):
        """
           Setter method pentru numele persoanei. 
        """
        self.__nume = value


    def set_adresa(self, value):
        """
           Setter method pentru adresa persoanei. 
        """
        self.__adresa = value
        
    def __str__(self):
        """
            __str__ method pentru persoana.
        """
        return f"[{self.__personID}] {self.__nume}, {self.__adresa}"
    
    def __repr__(self):
        """
            __repr__ method pentru persoana.
        """
        return f"{self.__personID},{self.__nume},{self.__adresa}"
    
        

