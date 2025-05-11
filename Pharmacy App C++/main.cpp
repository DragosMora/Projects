#include "lab1011.h"
#include <stdlib.h>
#include <crtdbg.h>
#include "Medicament.h"
#include "Teste.h"
#include "Repo.h"
#include "UI.h"
#include "GUI.h"
//#include "MyString.h"
//#include "VectorDinamic.h"

/*
Functia main a programului.
*/
int main(int argc, char *argv[])
{
    Teste teste1;
    teste1.ruleaza_toate_testele();

    Repo repo;
    RepoReteta repo_reteta;
    Service service{ repo };
    ServiceReteta service_reteta{ repo_reteta, repo };

    QApplication a(argc, argv);
    GUI gui{ service, service_reteta };
    gui.show();
    return a.exec();
}
