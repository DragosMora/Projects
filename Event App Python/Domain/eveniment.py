class Eveniment:
    def __init__(self, ID, data, timp, descriere):
        """
           Initializeaza evenimentul.
           ID = id-ul evenimentului
           data = data evenimentului
           timp = timpul de inceput al evenimentului
           descriere = descrierea evenimentului 
        """
        self.__ID = ID
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def get_id(self):
        """
           Getter method pentru id-ul evenimentului. 
        """
        return self.__ID


    def get_data(self):
        """
           Getter method pentru data evenimentului. 
        """
        return self.__data


    def get_timp(self):
        """
           Getter method pentru timpul evenimentului. 
        """
        return self.__timp


    def get_descriere(self):
        """
            Getter method pentru descrierea evenimentului.
        """
        return self.__descriere


    def set_data(self, value):
        """
           Setter method pentru data evenimentului. 
        """
        self.__data = value


    def set_timp(self, value):
        """
           Setter method pentru timpul evenimentului. 
        """
        self.__timp = value


    def set_descriere(self, value):
        """
           Setter method pentru descrierea evenimentului. 
        """
        self.__descriere = value

    def __str__(self):
        """
           __str__ method pentru eveniment. 
        """
        return f"[{self.__ID}] {self.__data}, {self.__timp}, {self.__descriere}"
    
    def __repr__(self):
        """
            __repr__ method pentru eveniment.
        """
        return f"{self.__ID},{self.__data},{self.__timp},{self.__descriere}"
    


