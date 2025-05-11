#pragma once
#include <QtWidgets/QApplication>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qwidget.h>
#include <qdebug.h>
#include <qmessagebox.h>
#include <vector>
#include <string>
#include "Service.h"
#include "ServiceReteta.h"

using std::vector;
using std::string;


class GUI : public QWidget {
private:
    Service& service1;
    ServiceReteta& service_reteta;

    QListWidget* lst = new QListWidget;
    QListWidget* lst2 = new QListWidget;
    QPushButton* btnExit = new QPushButton{ "&Exit" };
    QPushButton* btnAdd = new QPushButton{ "&Adauga" };
    QPushButton* btnDel = new QPushButton{ "&Sterge" };
    QPushButton* btnMod = new QPushButton{ "&Modifica" };
    QPushButton* btnFnd = new QPushButton{ "&Cauta" };
    QPushButton* btnFltP = new QPushButton{ "&FiltreazaPret" };
    QPushButton* btnFltS = new QPushButton{ "&FiltreazaSubst" };
    QPushButton* btnSrtD = new QPushButton{ "&SorteazaDenum" };
    QPushButton* btnSrtP = new QPushButton{ "&SorteazaProd" };
    QPushButton* btnSrtPr_S = new QPushButton{ "&SorteazaPret_Subst" };
    QPushButton* btnClearR = new QPushButton{ "&ClearReteta" };
    QPushButton* btnWriteR = new QPushButton{ "&ScrieReteta" };
    QPushButton* btnGenerateR = new QPushButton{ "&GenereazaReteta" };
    QPushButton* btnExportR = new QPushButton{ "&ExportReteta" };
    QLineEdit* txtNume = new QLineEdit;
    QLineEdit* txtPret = new QLineEdit;
    QLineEdit* txtProducator = new QLineEdit;
    QLineEdit* txtSubstanta = new QLineEdit;
    QLineEdit* txtNumeAux = new QLineEdit;
    QLineEdit* txtProdAux = new QLineEdit;
    QLineEdit* txtNumar = new QLineEdit;
    QLineEdit* txtFisier = new QLineEdit;
    
    /*
    Realizeaza conexiunile buton-actiune.
    */
    void initConnect();

    /*
    Incarca datele in vector.
    */
    void loadData();

    /*
    Initializeaza GUI.
    */
    void initGUI();

public:
    /*
    Constructor GUI.
    serv = referinta la service.
    serv_reteta = referinta la service reteta.
    */
    GUI(Service& serv, ServiceReteta& serv_reteta);
};