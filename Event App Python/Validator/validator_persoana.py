from Erori.erori import ValidationError

class ValidatorPersoana:
    def validate(self, persoana):
        """
            Valideaza o persoana.
            persoana = persoana validata
        """
        erori = ""
        if persoana.get_person_id()<0:
            erori += "ID-ul persoanei este invalid!\n"
        if persoana.get_nume() == "":
            erori += "Numele persoanei este invalid!\n"
        if persoana.get_adresa() == "":
            erori += "Adresa persoanei este invalida!\n"
        if len(erori)>0:
            raise ValidationError(erori)
        
    def validate_id(self, id):
        """
            Valideaza un id.
            id = id-ul validat
        """
        erori = ""
        if id<0:
            erori += "ID-ul persoanei este invalid!\n"
        if len(erori)>0:
            raise ValidationError(erori)

