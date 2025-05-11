from Erori.erori import ValidationError, RepoError
import time
import random

class Consola:
    def __init__(self, service_persoane, service_evenimente, service_bilete):
        """
           Initializeaza consola.
           service_persoane = service pentru persoane
           service_evenimente = service pentru evenimente
        """
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente
        self.__service_bilete = service_bilete
        self.__comenzi = {
            "Add_persoana":self.__ui_add_persoana,
            "Add_eveniment":self.__ui_add_eveniment,
            "Mod_persoana":self.__ui_mod_persoana,
            "Mod_eveniment":self.__ui_mod_eveniment,
            "Del_persoana":self.__ui_del_persoana,
            "Del_eveniment":self.__ui_del_eveniment,
            "Find_persoana":self.__ui_find_persoana,
            "Find_eveniment":self.__ui_find_eveniment,
            "Signup_persoana":self.__ui_signup_persoana,
            "Rap_desc":self.__ui_rap_desc,
            "Rap_data":self.__ui_rap_data,
            "Rap_pers":self.__ui_rap_pers,
            "Rap_20":self.__ui_rap_20,
            "Print_persoane":self.__ui_print_persoane,
            "Print_evenimente":self.__ui_print_evenimente,
            "Help":self.__ui_help
            }
        
    def __ui_add_persoana(self, params):
        """
           Trimite spre service persoane parametri valizi pentru adaugare persoana.
           params = parametri primiti
        """
        if len(params) != 3:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            nume = params[1]
            adresa = params[2]
            self.__service_persoane.add_persoana(id, nume, adresa)
            print("Persoana a fost adaugata cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_add_eveniment(self, params):
        """
           Trimite spre service evenimente parametri valizi pentru adaugare eveniment.
           params = parametri primiti
        """
        if len(params) != 4:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            data = params[1]
            timp = params[2]
            descriere = params[3]
            self.__service_evenimente.add_eveniment(id, data, timp, descriere)
            print("Evenimentul a fost adaugat cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_mod_persoana(self, params):
        """
            Trimite spre service persoane parametri valizi pentru modificare persoana.
            params = parametri primiti 
        """
        if len(params) != 3:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            nume = params[1]
            adresa = params[2]
            self.__service_persoane.modify_persoana(id, nume, adresa)
            print("Persoana a fost modificata cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
    
    def __ui_mod_eveniment(self, params):
        """
            Trimite spre service evenimente parametri valizi pentru modificare eveniment.
            params = parametri primiti 
        """
        if len(params) != 4:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            data = params[1]
            timp = params[2]
            descriere = params[3]
            self.__service_evenimente.modify_eveniment(id, data, timp, descriere)
            print("Evenimentul a fost modificat cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
        
    def __ui_del_persoana(self, params):
        """
            Trimite spre service persoane parametri pentru stergere persoana.
            params = parametri primiti
        """
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            self.__service_persoane.del_persoana(id)
            print("Persoana a fost stearsa din lista cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_del_eveniment(self, params):
        """
            Trimite spre service evenimente parametri pentru stergere eveniment.
            params = parametri primiti
        """
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            self.__service_evenimente.del_eveniment(id)
            print("Evenimentul a fost sters din lista cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_find_persoana(self, params):
        """
            Trimite spre service persoane parametri pentru cautare persoana.
            params = parametri primiti
        """
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            persoana = self.__service_persoane.find_persoana(id)
            print(persoana)
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_find_eveniment(self, params):
        """
            Trimite spre service evenimente parametri pentru cautare eveniment.
            params = parametri primiti
        """
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            id = int(params[0])
            eveniment = self.__service_evenimente.find_eveniment(id)
            print(eveniment)
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_signup_persoana(self, params):
        """
            Trimite spre service bilete parametri pentru adaugare bilet.
            params = parametri primiti
        """
        if len(params) != 3:
            print("Numar parametri invalid!")
            return
        try:
            id_bilet = int(params[0])
            id_persoana = int(params[1])
            id_eveniment = int(params[2])
            self.__service_bilete.add_bilet(id_bilet, id_persoana, id_eveniment)
            print("Persoana a fost inscrisa la eveniment cu succes!")
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_rap_desc(self, params):
        """
            Afiseaza raportul pentru evenimente.
            params = parametri primiti
        """
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            id_persoana = int(params[0])
            lista = self.__service_bilete.rap_desc(id_persoana)
            for item in lista:
                print(item)
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_rap_data(self, params):
        """
            Afiseaza raportul pentru evenimente.
            params = parametri primiti
        """
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            id_persoana = int(params[0])
            lista = self.__service_bilete.rap_data(id_persoana)
            for item in lista:
                print(item)
        except ValueError:
            print("Valoarea parametrilor invalida!")
        except ValidationError as ve:
            print(ve)
        except RepoError as re:
            print(re)
            
    def __ui_rap_pers(self, params):
        """
            Afiseaza raportul pentru persoane.
        """
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        try:
            inscrieri, lista = self.__service_bilete.rap_pers()
            print(f"Urmatoarele persoane participa la {inscrieri} evenimente:")
            for elem in lista:
                print(elem)
        except RepoError as re:
            print(re)
            
    def __ui_rap_20(self, params):
        """
            Afiseaza raportul pentru evenimente si participanti.
        """
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        try:
            lista = self.__service_bilete.rap_20()
            for elem in lista:
                print(f"[{elem[0]}] {elem[1]}, {elem[2]}")
        except RepoError as re:
            print(re)
        except IndexError:
            print("Lista cu rapoarte este goala!")
            
    def __ui_print_persoane(self, params):
        """
            Afiseaza toate persoanele din lista de persoane.
        """
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        try:    
            lista_persoane = self.__service_persoane.get_all()
            for persoana in lista_persoane:
                print(persoana)
        except RepoError as re:
            print(re)
        
    def __ui_print_evenimente(self, params):
        """
            Afiseaza toate evenimentele din lista de evenimente.
        """
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        try:
            lista_evenimente = self.__service_evenimente.get_all()
            for eveniment in lista_evenimente:
                print(eveniment)
        except RepoError as re:
            print(re)
    
    def __ui_help(self, params):
        """
            Afiseaza toate comenzile.
        """
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        print("Lista de comenzi:")
        print("Add_persoana, <id_persoana>, <nume>, <adresa>")
        print("Add_eveniment, <id_eveniment>, <data>, <timp>, <descriere>")
        print("Mod_persoana, <id_persoana>, <nume>, <adresa>")
        print("Mod_eveniment, <id_eveniment>, <data>, <timp>, <descriere>")
        print("Del_persoana, <id_persoana>")
        print("Del_eveniment, <id_eveniment>")
        print("Find_persoana, <id_persoana>")
        print("Find_eveniment, <id_eveniment>")
        print("Signup_persoana, <id_bilet>, <id_persoana>, <id_eveniment>")
        print("Rap_desc, <id_persoana>")
        print("Rap_data, <id_persoana>")
        print("Rap_pers")
        print("Rap_20")
        print("Print_persoane")
        print("Print_evenimente")
        print("Help")
        print("Exit")
        print()
    
    def generate_random_input(self):
        """
            Genereaza input pentru persoane si evenimente la intamplare.
        """
        while True:
            command = input(">>>")
            if command == "":
                continue
            if command == "Exit":
                return
            try:
                command = int(command)
                if command <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Input invalid!")
                
        lista_nume_persoane = ["Andrei", "Miron", "Daniel", "Darius", "Raluca", "Cosmin", "Andreea", "Carla", "Denisa"]
        lista_adrese_persoane = ["Spatarilor 11", "Ciresilor 57", "Avram Iancu 21", "Marinescu 44", "Popescu 81", "Gheorghe-Mihai 3"]
        
                
        for index in range(command):
            params = []
            id_persoana = random.randint(1, 100)
            nume = random.choice(lista_nume_persoane)
            adresa = random.choice(lista_adrese_persoane)
            params.append(id_persoana)
            params.append(nume)
            params.append(adresa)
            self.__ui_add_persoana(params)
        
        lista_date_evenimente = ["19.05.2025", "20.05.2024", "05.11.2025", "17.01.2026", "20.03.2024", "19.01.2023", "22.04.2023", "23.10.2025"]
        lista_timp_evenimente = ["13:00", "13:15", "15:45", "12:05", "19:45", "20:30", "23:30", "11:15", "07:30", "09:30", "16:20", "14:45", "22:15"]
        lista_descrieri_evenimente = ["Untold", "Electric Castle", "Opera", "Balet", "Colinde", "Rock concert", "Pop concert", "Jazz concert"]
        
        for index in range(command):
            params = []
            id_eveniment = random.randint(1000, 1100)
            data = random.choice(lista_date_evenimente)
            timp = random.choice(lista_timp_evenimente)
            descriere = random.choice(lista_descrieri_evenimente)
            params.append(id_eveniment)
            params.append(data)
            params.append(timp)
            params.append(descriere)
            self.__ui_add_eveniment(params)
            
    def run(self):
        """
            Ruleaza consola recursiv.
        """
        command = input(">>>")
        if command == "Exit":
            print("La revedere!")
            time.sleep(3)
            return
        elif command == "":
            return self.run()
        parts = command.split(",")
        for index in range(len(parts)):
            parts[index] = parts[index].strip()
        cmd = parts[0]
        params = parts[1:]
        if cmd in self.__comenzi:
            self.__comenzi[cmd](params)
        else:
            print("Comanda invalida!")
        return self.run()
        
            
        


