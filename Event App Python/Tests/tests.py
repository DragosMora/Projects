from Domain.persoana import Persoana
from Domain.eveniment import Eveniment
from Domain.biletDTO import BiletDTO
from Erori.erori import ValidationError, RepoError
from Validator.validator_persoana import ValidatorPersoana
from Validator.validator_eveniment import ValidatorEveniment
from Persistenta.repo_persoane import RepoPersoane, FileRepoPersoane
from Persistenta.repo_evenimente import RepoEvenimente, FileRepoEvenimente
from Persistenta.repo_bilete import RepoBilete, FileRepoBilete
from Business.service_persoane import ServicePersoane
from Business.service_evenimente import ServiceEvenimente
from Business.service_bilete import ServiceBilete

class Tests:
    def __init__(self):
        pass
    
    def __domain_persoana_tests(self):
        """
            Ruleaza testele pentru persoana din domain.
        """
        print("starting domain persoana tests...")
        self.__personID1 = 4512
        self.__nume1 = "Popovici Gabriel"
        self.__adresa1 = "Ciresarilor 142"
        persoana1 = Persoana(self.__personID1, self.__nume1, self.__adresa1)
        assert persoana1.get_person_id() == self.__personID1
        assert persoana1.get_nume() == self.__nume1
        assert persoana1.get_adresa() == self.__adresa1
        
        self.__nume2 = "Popovici Andrei"
        self.__adresa2 = "Ciresarilor 165"
        persoana1.set_nume(self.__nume2)
        persoana1.set_adresa(self.__adresa2)
        assert persoana1.get_nume() == self.__nume2
        assert persoana1.get_adresa() == self.__adresa2
        assert str(persoana1) != ""
        print("finished domain persoana tests...")
        
    def __domain_eveniment_tests(self):
        """
           Ruleaza testele pentru evenimentul din domain. 
        """
        print("starting domain eveniment tests...")
        self.__ID1 = 1251
        self.__data1 = "19.06.2024"
        self.__timp1 = "20:30"
        self.__descriere1 = "Super Show te asteapta la cel mai mare..."
        eveniment1 = Eveniment(self.__ID1, self.__data1, self.__timp1, self.__descriere1)
        assert eveniment1.get_id() == self.__ID1
        assert eveniment1.get_data() == self.__data1
        assert eveniment1.get_timp() == self.__timp1
        assert eveniment1.get_descriere() == self.__descriere1
        
        self.__data2 = "19.07.2024"
        self.__timp2 = "12:45"
        self.__descriere2 = "Super Show este cel mai mare eveniment..."
        eveniment1.set_data(self.__data2)
        eveniment1.set_timp(self.__timp2)
        eveniment1.set_descriere(self.__descriere2)
        assert eveniment1.get_data() == self.__data2
        assert eveniment1.get_timp() == self.__timp2
        assert eveniment1.get_descriere() == self.__descriere2
        assert str(eveniment1) != ""
        print("finished domain eveniment tests...")
        
    def __validator_persoana_tests(self):
        """
           Ruleaza testele pentru validarea unei persoane. 
        """
        print("starting validator persoana tests...")
        self.__personID_error = -125
        self.__nume_error = ""
        self.__adresa_error = ""
        persoana_error = Persoana(self.__personID_error, self.__nume_error, self.__adresa_error)
        validator = ValidatorPersoana()
        try:
            validator.validate(persoana_error)
            assert False
        except ValidationError as ve:
            assert "ID-ul persoanei este invalid!" in str(ve)
            assert "Numele persoanei este invalid!" in str(ve)
            assert "Adresa persoanei este invalida!" in str(ve)
        print("finished validator persoana tests...")
            
    def __validator_eveniment_tests(self):
        """
           Ruleaza testele pentru validarea unui eveniment.
        """
        print("starting validator eveniment tests...")
        self.__ID_error = -6
        self.__data_error = "42.05.2111"
        self.__timp_error = "douazeci:treizeci"
        self.__descriere_error = ""
        eveniment_error = Eveniment(self.__ID_error, self.__data_error, self.__timp_error, self.__descriere_error)
        validator = ValidatorEveniment()
        try:
            validator.validate(eveniment_error)
            assert False
        except ValidationError as ve:
            assert "ID-ul evenimentului este invalid!" in str(ve)
            assert "Data evenimentului este invalida!" in str(ve)
            assert "Timpul evenimentului nu este numeric!" in str(ve)
            assert "Descrierea evenimentului este invalida!" in str(ve)
        print("finished validator eveniment tests...")
        
    def __goleste_fisier(self, file_path):
        """
            Goleste fisierul de la locatia file_path.
            file_path = locatia fisierului
        """
        with open(file_path, "w") as f:
            f.write("")
        
    def __repo_persoane_tests(self):
        """
           Ruleaza testele pentru repo persoane.
        """
        print("starting repo persoane tests...")
        self.__personID3 = 512
        self.__nume3 = "Marian Ceausescu"
        self.__adresa3 = "Starwars Strasse Zwei"
        persoana3 = Persoana(self.__personID3, self.__nume3, self.__adresa3)
        validator = ValidatorPersoana()
        validator.validate(persoana3)
        
        file_path = "C:\\UBB_INFO\\Sem1\\FP\\Lab10\\Tests\\persoane_test.txt"
        self.__goleste_fisier(file_path)
        repo_persoane = FileRepoPersoane(file_path)
        assert len(repo_persoane) == 0
        try:
            lista = repo_persoane.get_all()
            assert False
        except RepoError as re:
            assert "Lista de persoane este goala!" in str(re)
        
        repo_persoane.add_persoana(persoana3)
        assert len(repo_persoane) == 1
        assert repo_persoane.get_all()[0] == str(persoana3)
        
        self.__personID5 = 5123
        self.__nume5 = "Andrei Vasile"
        self.__adresa5 = "Ciresarilor 117"
        persoana5 = Persoana(self.__personID5, self.__nume5, self.__adresa5)
        try:
            repo_persoane.modify_persoana(persoana5)
            assert False
        except RepoError as re:
            assert "Persoana nu exista!" in str(re)
        
        self.__personID6 = 512
        self.__nume6 = "Marian Ciobanescu"
        self.__adresa6 = "Starwars Strasse Drei"
        persoana6 = Persoana(self.__personID6, self.__nume6, self.__adresa6)
        try:
            repo_persoane.modify_persoana(persoana6)
            assert True
        except:
            assert False
        
        self.__personID8 = 618
        try:
            repo_persoane.del_persoana(self.__personID8)
            assert False
        except RepoError as re:
            assert "Persoana nu exista!" in str(re)
            
        assert len(repo_persoane) == 1
        repo_persoane.del_persoana(self.__personID6)
        assert len(repo_persoane) == 0
        
        try:
            repo_persoane.find_persoana(self.__personID6)
            assert False
        except RepoError as re:
            assert "Persoana nu exista!" in str(re)
        
        self.__personID9 = 6881
        self.__nume9 = "Anatoly Karpov"
        self.__adresa9 = "Russsssssia" 
        persoana9 = Persoana(self.__personID9, self.__nume9, self.__adresa9)
        repo_persoane.add_persoana(persoana9)
        assert len(repo_persoane) == 1
        persoana_cautata = repo_persoane.find_persoana(self.__personID9)
        assert persoana_cautata.get_person_id() == self.__personID9
        assert persoana_cautata.get_nume() == self.__nume9
        assert persoana_cautata.get_adresa() == self.__adresa9
        
        print("finished repo persoane tests...")
    
    def __repo_evenimente_tests(self):
        """
           Ruleaza testele pentru repo evenimente. 
        """
        print("starting repo evenimente tests...")
        self.__ID3 = 123
        self.__data3 = "19.05.2024"
        self.__timp3 = "14:15"
        self.__descriere3 = "MegaUltraShow va astapta la cel mai superb spectacol..."
        eveniment3 = Eveniment(self.__ID3, self.__data3, self.__timp3, self.__descriere3)
        validator = ValidatorEveniment()
        validator.validate(eveniment3)
        
        file_path = "C:\\UBB_INFO\\Sem1\\FP\\Lab10\\Tests\\evenimente_test.txt"
        self.__goleste_fisier(file_path)
        repo_evenimente = FileRepoEvenimente(file_path)
        assert len(repo_evenimente) == 0
        try:
            lista = repo_evenimente.get_all()
            assert False
        except RepoError as re:
            assert "Lista de evenimente este goala" in str(re)
        
        repo_evenimente.add_eveniment(eveniment3)
        assert len(repo_evenimente) == 1
        assert repo_evenimente.get_all()[0] == str(eveniment3)
        
        self.__ID5 = 12565
        self.__data5 = "05.02.2025"
        self.__timp5 = "18:00"
        self.__descriere5 = "UltraShow"
        eveniment5 = Eveniment(self.__ID5, self.__data5, self.__timp5, self.__descriere5)
        try:
            repo_evenimente.modify_eveniment(eveniment5)
            assert False
        except RepoError as re:
            assert "Evenimentul nu exista!" in str(re)
        
        self.__ID6 = 123
        self.__data6 = "15.04.2024"
        self.__timp6 = "20:45"
        self.__descriere6 = "NightShow"
        eveniment6 = Eveniment(self.__ID6, self.__data6, self.__timp6, self.__descriere6)
        try:
            repo_evenimente.modify_eveniment(eveniment6)
            assert True
        except:
            assert False
        
        self.__ID8 = 9812
        try:
            repo_evenimente.del_eveniment(self.__ID8)
            assert False
        except RepoError as re:
            assert "Evenimentul nu exista" in str(re)
            
        assert len(repo_evenimente) == 1
        repo_evenimente.del_eveniment(self.__ID3)
        assert len(repo_evenimente) == 0
        
        try:
            repo_evenimente.find_eveniment(self.__ID6)
            assert False
        except RepoError as re:
            assert "Evenimentul nu exista!" in str(re)
        
        self.__ID9 = 881
        self.__data9 = "11.11.2024"
        self.__timp9 = "09:15"
        self.__descriere9 = "HappyShow"
        eveniment9 = Eveniment(self.__ID9, self.__data9, self.__timp9, self.__descriere9)
        repo_evenimente.add_eveniment(eveniment9)
        assert len(repo_evenimente) == 1
        eveniment_cautat = repo_evenimente.find_eveniment(self.__ID9)
        assert eveniment_cautat.get_id() == self.__ID9
        assert eveniment_cautat.get_data() == self.__data9
        assert eveniment_cautat.get_timp() == self.__timp9
        assert eveniment_cautat.get_descriere() == self.__descriere9
    
        print("finished repo evenimente tests...")
    
    def __service_persoane_tests(self):
        """
            Ruleaza testele pentru service persoane.
        """
        print("starting service persoane tests...")
        validator_persoana = ValidatorPersoana()
        repo_persoane = RepoPersoane()
        service_persoane = ServicePersoane(validator_persoana, repo_persoane)
        self.__personID4 = 52
        self.__nume4 = "Anton Anton"
        self.__adresa4 = "Jack Daniels NO7"
        assert len(service_persoane) == 0
        service_persoane.add_persoana(self.__personID4, self.__nume4, self.__adresa4)
        assert len(service_persoane) == 1
        assert service_persoane.get_all()[0] == str(Persoana(self.__personID4, self.__nume4, self.__adresa4))
        
        self.__personID7 = 52
        self.__nume7 = "Anton Gheorghiu"
        self.__adresa7 = "Jack Daniels NO7"
        try:
            service_persoane.modify_persoana(self.__personID7, self.__nume7, self.__adresa7)
            assert True
        except:
            assert False
            
        assert len(service_persoane) == 1
        service_persoane.del_persoana(self.__personID4)
        assert len(service_persoane) == 0
        
        self.__personID10 = 6671
        self.__nume10 = "Marian Cioban"
        self.__adresa10 = "Plopilor 612c"
        service_persoane.add_persoana(self.__personID10, self.__nume10, self.__adresa10)
        persoana_gasita = service_persoane.find_persoana(self.__personID10)
        assert persoana_gasita.get_person_id() == self.__personID10
        assert persoana_gasita.get_nume() == self.__nume10
        assert persoana_gasita.get_adresa() == self.__adresa10
        
        print("finished service persoane tests...")
    
    def __service_evenimente_tests(self):
        """
           Ruleaza testele pentru service evenimente. 
        """
        print("starting service evenimente tests...")
        validator_eveniment = ValidatorEveniment()
        repo_evenimente = RepoEvenimente()
        service_evenimente = ServiceEvenimente(validator_eveniment, repo_evenimente)
        self.__ID4 = 6165
        self.__data4 = "11.02.2024"
        self.__timp4 = "18:45"
        self.__descriere4 = "Football Show va asteapta la cel mai mare spectacol dedicat fanilor de..."
        assert len(service_evenimente) == 0
        service_evenimente.add_eveniment(self.__ID4, self.__data4, self.__timp4, self.__descriere4)
        assert len(service_evenimente) == 1
        assert service_evenimente.get_all()[0] == str(Eveniment(self.__ID4, self.__data4, self.__timp4, self.__descriere4))
        
        self.__ID7 = 6165
        self.__data7 = "11.02.2025"
        self.__timp7 = "19:45"
        self.__descriere7 = "Soccer Show va asteapta..."
        try:
            service_evenimente.modify_eveniment(self.__ID7, self.__data7, self.__timp7, self.__descriere7)
            assert True
        except:
            assert False
        
        assert len(service_evenimente) == 1
        service_evenimente.del_eveniment(self.__ID4)
        assert len(service_evenimente) == 0
        
        self.__ID10 = 8512
        self.__data10 = "06.02.2025"
        self.__timp10 = "17:35"
        self.__descriere10 = "RockShow"
        service_evenimente.add_eveniment(self.__ID10, self.__data10, self.__timp10, self.__descriere10)
        eveniment_gasit = service_evenimente.find_eveniment(self.__ID10)
        assert eveniment_gasit.get_id() == self.__ID10
        assert eveniment_gasit.get_data() == self.__data10
        assert eveniment_gasit.get_timp() == self.__timp10
        assert eveniment_gasit.get_descriere() == self.__descriere10
        
        print("finished service evenimente tests...")
    
    def __domain_BiletDTO_tests(self):
        """
            Ruleaza testele pentru BiletDTO din domain.
        """
        print("starting domain BiletDTO tests...")
        self.__personID11 = 1004
        self.__nume11 = "Andrei Muresan"
        self.__adresa11 = "Teodor Mihali 48"
        persoana11 = Persoana(self.__personID11, self.__nume11, self.__adresa11)
        self.__ID11 = 1005
        self.__data11 = "15.10.2025"
        self.__timp11 = "17:45"
        self.__descriere11 = "MorningShow te asteapta la..."
        eveniment11 = Eveniment(self.__ID11, self.__data11, self.__timp11, self.__descriere11)
        
        self.__biletID1 = 5212
        bilet1 = BiletDTO(self.__biletID1, self.__personID11, self.__ID11)
        assert bilet1.get_bilet_id() == self.__biletID1
        assert bilet1.get_person_id() == self.__personID11
        assert bilet1.get_eveniment_id() == self.__ID11
        
        print("finished domain BiletDTO tests...")
        
    def __repo_bilete_tests(self):
        """
            Ruleaza testele pentru repo bilete.
        """
        print("starting repo bilete tests...")
        self.__personID12 = 1009
        self.__nume12 = "Andrei Muresan"
        self.__adresa12 = "Teodor Mihali 48"
        persoana12 = Persoana(self.__personID11, self.__nume11, self.__adresa11)
        self.__ID12 = 1011
        self.__data12 = "15.10.2025"
        self.__timp12 = "17:45"
        self.__descriere12 = "MorningShow te asteapta la..."
        eveniment12 = Eveniment(self.__ID11, self.__data11, self.__timp11, self.__descriere11)
        
        self.__biletID2 = 5213
        bilet2 = BiletDTO(self.__biletID2, self.__personID12, self.__ID12)
        
        self.__biletID3 = 5213
        bilet3 = BiletDTO(self.__biletID3, self.__personID12, self.__ID12)
        
        file_path = "C:\\UBB_INFO\\Sem1\\FP\\Lab10\\Tests\\bileteDTO_test.txt"
        self.__goleste_fisier(file_path)
        repo_bilete = FileRepoBilete(file_path)
        assert len(repo_bilete) == 0
        repo_bilete.add_bilet(bilet2)
        assert len(repo_bilete) == 1
        
        try:
            repo_bilete.add_bilet(bilet3)
            assert False
        except RepoError as re:
            assert "Bilet existent!" in str(re)
            
        lista_bilete = repo_bilete.get_all()
        assert len(lista_bilete) == 1
        
        print("finished repo bilete tests...")
    
    def __service_bilete_tests(self):
        """
            Ruleaza testele pentru service bilete.
        """
        print("starting service bilete tests...")
        self.__personID13 = 1145
        self.__nume13 = "Jolt Mateius"
        self.__adresa13 = "Beverly Hills 124a"
        persoana13 = Persoana(self.__personID13, self.__nume13, self.__adresa13)
        
        self.__ID13 = 1146
        self.__data13 = "16.07.2026"
        self.__timp13 = "13:45"
        self.__descriere13 = "RockShowSuper"
        eveniment13 = Eveniment(self.__ID13, self.__data13, self.__timp13, self.__descriere13)
        
        repo_persoane = RepoPersoane()
        repo_evenimente = RepoEvenimente()
        repo_bilete = RepoBilete()
        
        service_bilete = ServiceBilete(repo_persoane, repo_evenimente, repo_bilete)
        
        repo_persoane.add_persoana(persoana13)
        repo_evenimente.add_eveniment(eveniment13)
        
        self.__biletID4 = 8890
        
        self.__personID14 = 6799
        try:
            service_bilete.add_bilet(self.__biletID4, self.__personID14, self.__ID13)
            assert False
        except RepoError as re:
            assert "Persoana nu exista!" in str(re)
            
        self.__ID14 = 8002
        try:
            service_bilete.add_bilet(self.__biletID4, self.__personID13, self.__ID14)
            assert False
        except RepoError as re:
            assert "Evenimentul nu exista!" in str(re)
            
        assert len(service_bilete) == 0
        service_bilete.add_bilet(self.__biletID4, self.__personID13, self.__ID13)
        assert len(service_bilete) == 1
        
        self.__ID15 = 2299
        self.__data15 = "26.05.2026"
        self.__timp15 = "16:00"
        self.__descriere15 = "ARuggedShow este un mare show despre..."
        eveniment15 = Eveniment(self.__ID15, self.__data15, self.__timp15, self.__descriere15)
        
        self.__ID16 = 2817
        self.__data16 = "07.07.2025"
        self.__timp16 = "17:55"
        self.__descriere16 = "CleanShow este un show despre..."
        eveniment16 = Eveniment(self.__ID16, self.__data16, self.__timp16, self.__descriere16)
        
        repo_evenimente.add_eveniment(eveniment15)
        repo_evenimente.add_eveniment(eveniment16)
        assert len(repo_evenimente) == 3
        
        self.__biletID5 = 766
        service_bilete.add_bilet(self.__biletID5, self.__personID13, self.__ID15)
        
        self.__personID15 = 8999
        self.__nume15 = "Poporan Anton"
        self.__adresa15 = "Kolentina 90"
        persoana15 = Persoana(self.__personID15, self.__nume15, self.__adresa15)
        
        repo_persoane.add_persoana(persoana15)
        
        self.__biletID6 = 778
        
        service_bilete.add_bilet(self.__biletID6, self.__personID15, self.__ID16)
        
        lista_bilete = repo_bilete.get_all()
        assert len(lista_bilete) == 3
        
        lista1 = service_bilete.rap_desc(self.__personID13)
        assert len(lista1) == 2
        
        lista2 = service_bilete.rap_data(self.__personID13)
        assert len(lista1) == 2
        
        self.__biletID7 = 779
        service_bilete.add_bilet(self.__biletID7, self.__personID15, self.__ID15)
        
        inscrieri, lista3 = service_bilete.rap_pers()
        assert inscrieri == 2
        assert len(lista3) == 2
        
        lista4 = service_bilete.rap_20()
        assert lista4 == []
        
        print("finished service bilete tests...")
        
    def run_all_tests(self):
        """
           Ruleaza toate testele.
        """
        self.__domain_persoana_tests()
        self.__domain_eveniment_tests()
        
        self.__validator_persoana_tests()
        self.__validator_eveniment_tests()
        
        self.__repo_persoane_tests()
        self.__repo_evenimente_tests()
        
        self.__service_persoane_tests()
        self.__service_evenimente_tests()
        
        self.__domain_BiletDTO_tests()
        self.__repo_bilete_tests()
        self.__service_bilete_tests()


