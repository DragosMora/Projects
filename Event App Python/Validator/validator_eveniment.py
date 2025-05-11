from Erori.erori import ValidationError

class ValidatorEveniment:
    def validate(self, eveniment):
        """
           Valideaza un eveniment.
           eveniment = evenimentul validat
        """
        erori = ""
        if eveniment.get_id()<0:
            erori += "ID-ul evenimentului este invalid!\n"
        
        data = eveniment.get_data()
        data = data.split(".")
        try:
            if len(data) != 3 or int(data[0]) > 31 or int(data[1]) < 1 or int(data[1]) > 12 or int(data[2]) < 0:
                erori += "Data evenimentului este invalida!\n"
        except ValueError:
            erori += "Data evenimentului nu este numerica!\n"
        
        timp = eveniment.get_timp()
        timp = timp.split(":")
        try:
            if len(timp) != 2 or int(timp[0]) > 23 or int(timp[1]) > 59:
                erori += "Timpul evenimentului este invalid!\n"
        except ValueError:
            erori += "Timpul evenimentului nu este numeric!\n"
            
        if eveniment.get_descriere() == "":
            erori += "Descrierea evenimentului este invalida!\n"
            
        if len(erori)>0:
            raise ValidationError(erori)
        
    def validate_id(self, id):
        """
            Valideaza un id.
            id = id-ul validat
        """
        erori = ""
        if id<0:
            erori += "ID-ul evenimentului este invalid!\n"
        if len(erori)>0:
            raise ValidationError(erori)
        
            
