from Tests.tests import Tests
from Validator.validator_persoana import ValidatorPersoana
from Validator.validator_eveniment import ValidatorEveniment
from Persistenta.repo_persoane import RepoPersoane, FileRepoPersoane
from Persistenta.repo_evenimente import RepoEvenimente, FileRepoEvenimente
from Persistenta.repo_bilete import RepoBilete, FileRepoBilete
from Business.service_persoane import ServicePersoane
from Business.service_evenimente import ServiceEvenimente
from Business.service_bilete import ServiceBilete
from UI.consola import Consola

if __name__ == '__main__':
    """
        Functia main a programului.
    """
    teste = Tests()
    teste.run_all_tests()
    
    validator_persoana = ValidatorPersoana()
    validator_eveniment = ValidatorEveniment()
    
    file_path_persoane = "C:\\UBB_INFO\\Sem1\\FP\\Lab12\\persoane.txt"
    repo_persoane = FileRepoPersoane(file_path_persoane)
    file_path_evenimente = "C:\\UBB_INFO\\Sem1\\FP\\Lab12\\evenimente.txt"
    repo_evenimente = FileRepoEvenimente(file_path_evenimente)
    file_path_bilete = "C:\\UBB_INFO\\Sem1\\FP\\Lab12\\bileteDTO.txt"
    repo_bilete = FileRepoBilete(file_path_bilete)
    
    service_persoane = ServicePersoane(validator_persoana, repo_persoane)
    service_evenimente = ServiceEvenimente(validator_eveniment, repo_evenimente)
    service_bilete = ServiceBilete(repo_persoane, repo_evenimente, repo_bilete)
    
    ui = Consola(service_persoane, service_evenimente, service_bilete)
    #ui.generate_random_input()
    ui.run()
    
    