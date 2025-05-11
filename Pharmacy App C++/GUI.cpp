#include "GUI.h"
#include "Validator.h"

GUI::GUI(Service& serv, ServiceReteta& serv_reteta) : service1{ serv }, service_reteta{ serv_reteta } {
    initGUI();
    loadData();
    initConnect();
}

void GUI::initConnect() {
    QObject::connect(btnExit, &QPushButton::clicked, [&]() {
        //qDebug() << "Exit button apasat!!!";
        QMessageBox::information(nullptr, "Info", "Buton exit apasat!");
        close();
        });

    QObject::connect(btnAdd, &QPushButton::clicked, [&]() {
        auto denumire = txtNume->text();
        std::string stdStrDenumire = denumire.toStdString();
        auto pret = txtPret->text();
        double dblPret = pret.toDouble();
        auto producator = txtProducator->text();
        std::string stdStrProducator = producator.toStdString();
        auto substanta = txtSubstanta->text();
        std::string stdStrSubstanta = substanta.toStdString();
        //qDebug() << "Nume" << denumire << "Tip" << tip << "Pret" << pret;
        try {
            service1.add(stdStrDenumire, dblPret, stdStrProducator, stdStrSubstanta);
            QMessageBox::information(nullptr, "Info", "Medicament adaugat cu success!");
        }
        catch (ValidatorException& v) {
            QString mesaj = QString::fromStdString(v.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        catch (RepoException& e) {
            QString mesaj = QString::fromStdString(e.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        loadData();
        });

    QObject::connect(btnDel, &QPushButton::clicked, [&]() {
        auto denumire = txtNume->text();
        std::string stdStrDenumire = denumire.toStdString();
        auto producator = txtProducator->text();
        std::string stdStrProducator = producator.toStdString();
        try {
            service1.del(stdStrDenumire, stdStrProducator);
            QMessageBox::information(nullptr, "Info", "Medicament sters cu success!");
        }
        catch (RepoException& e) {
            QString mesaj = QString::fromStdString(e.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        loadData();
        });

    QObject::connect(btnMod, &QPushButton::clicked, [&]() {
        auto denumire = txtNume->text();
        std::string stdStrDenumire = denumire.toStdString();
        auto pret = txtPret->text();
        double dblPret = pret.toDouble();
        auto producator = txtProducator->text();
        std::string stdStrProducator = producator.toStdString();
        auto substanta = txtSubstanta->text();
        std::string stdStrSubstanta = substanta.toStdString();
        auto denumireaux = txtNumeAux->text();
        std::string stdStrDenumireAux = denumireaux.toStdString();
        auto producatoraux = txtProdAux->text();
        std::string stdStrProdAux = producatoraux.toStdString();
        try {
            service1.upd(stdStrDenumireAux, stdStrProdAux, stdStrDenumire, dblPret, stdStrProducator, stdStrSubstanta);
            QMessageBox::information(nullptr, "Info", "Medicament modificat cu success!");
        }
        catch (ValidatorException& v) {
            QString mesaj = QString::fromStdString(v.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        catch (RepoException& e) {
            QString mesaj = QString::fromStdString(e.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        loadData();
        });

    QObject::connect(btnFnd, &QPushButton::clicked, [&]() {
        auto denumire = txtNume->text();
        std::string stdStrDenumire = denumire.toStdString();
        auto producator = txtProducator->text();
        std::string stdStrProducator = producator.toStdString();
        try {
            Medicament med = service1.fnd(stdStrDenumire, stdStrProducator);
            QMessageBox::information(nullptr, "Info", QString::fromStdString(med.getDenumire() + "\n" + std::to_string(med.getPret()) + "\n" + med.getProducator() + "\n" + med.getSubstanta()));
        }
        catch (RepoException& e) {
            QString mesaj = QString::fromStdString(e.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        loadData();
        });

    QObject::connect(btnFltP, &QPushButton::clicked, [&]() {
        auto pret = txtPret->text();
        double dblPret = pret.toDouble();
        vector<Medicament> filtrate = service1.filter([&](const Medicament& m1) {
            if (m1.getPret() < dblPret) return true;
            return false;
            });
        lst->clear();
        for (const auto& med : filtrate) {
            lst->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
        }
        });

    QObject::connect(btnFltS, &QPushButton::clicked, [&]() {
        auto substanta = txtSubstanta->text();
        std::string stdStrSubstanta = substanta.toStdString();
        vector<Medicament> filtrate = service1.filter([&](const Medicament& m1) {
            if (m1.getSubstanta() == substanta.toStdString()) return true;
            return false;
            });
        lst->clear();
        for (const auto& med : filtrate) {
            lst->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
        }
        });

    QObject::connect(btnSrtD, &QPushButton::clicked, [&]() {
        vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
            return m1.getDenumire() < m2.getDenumire();
            });
        lst->clear();
        for (const auto& med : sortate) {
            lst->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
        }
        });

    QObject::connect(btnSrtP, &QPushButton::clicked, [&]() {
        vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
            return m1.getProducator() < m2.getProducator();
            });
        lst->clear();
        for (const auto& med : sortate) {
            lst->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
        }
        });

    QObject::connect(btnSrtPr_S, &QPushButton::clicked, [&]() {
        vector<Medicament> sortate = service1.sorts([&](const Medicament& m1, const Medicament& m2) {
            if (m1.getSubstanta() != m2.getSubstanta()) return m1.getSubstanta() < m2.getSubstanta();
            return m1.getPret() < m2.getPret();
            });
        lst->clear();
        for (const auto& med : sortate) {
            lst->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
        }
        });

    QObject::connect(btnClearR, &QPushButton::clicked, [&]() {
        service_reteta.clear();
        lst2->clear();
        });

    QObject::connect(btnWriteR, &QPushButton::clicked, [&]() {
        auto denumire = txtNume->text();
        std::string stdStrDenumire = denumire.toStdString();
        auto producator = txtProducator->text();
        std::string stdStrProducator = producator.toStdString();
        try {
            service_reteta.write(stdStrDenumire, stdStrProducator);
            QMessageBox::information(nullptr, "Info", "Medicament scris cu success!");
        }
        catch (RepoException& e) {
            QString mesaj = QString::fromStdString(e.getMessage());
            QMessageBox::critical(nullptr, "Eroare", mesaj);
        }
        loadData();
        });

    QObject::connect(btnGenerateR, &QPushButton::clicked, [&]() {
        auto elem_nr = txtNumar->text();
        int intElem_nr = elem_nr.toInt();
        vector<string> denumiri, producatori, substante;
        vector<double> preturi;
        denumiri.push_back("Dulcolax");
        denumiri.push_back("Emetix");
        denumiri.push_back("Dulcosolvan");
        denumiri.push_back("GripActiv");
        preturi.push_back(19.99);
        preturi.push_back(21.99);
        preturi.push_back(32.33);
        producatori.push_back("CFR");
        producatori.push_back("SUA");
        substante.push_back("Speis");
        substante.push_back("Cacao");
        substante.push_back("Zahar");
        service_reteta.generate(intElem_nr, denumiri, preturi, producatori, substante);
        QMessageBox::information(nullptr, "Info", "Medicamentele s-au generat cu succes!");
        loadData();
        });

    QObject::connect(btnExportR, &QPushButton::clicked, [&]() {
        auto nume_fisier = txtFisier->text();
        std::string stdStrNume_Fisier = nume_fisier.toStdString();
        service_reteta.exports(stdStrNume_Fisier);
        QMessageBox::information(nullptr, "Info", "Reteta a fost exportata cu succes!");
        loadData();
        });
}

void GUI::loadData() {
    lst->clear();
    lst2->clear();
    vector<Medicament> Meds = service1.getAll();
    for (const auto& med : Meds) {
        lst->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
    }
    vector<Medicament> Reteta = service_reteta.get_all();
    for (const auto& med : Reteta) {
        lst2->addItem(QString::fromStdString(med.getDenumire() + " " + std::to_string(med.getPret()) + " " + med.getProducator() + " " + med.getSubstanta()));
    }
}

void GUI::initGUI() {
    QHBoxLayout* lyMain = new QHBoxLayout{};
    setLayout(lyMain);
    
    QVBoxLayout* lyLst = new QVBoxLayout;
    QLabel* label_meds = new QLabel{ "Medicamente" };
    lyLst->addWidget(label_meds);
    lyLst->addWidget(lst);
    lyMain->addLayout(lyLst);

    QVBoxLayout* lyLst2 = new QVBoxLayout;
    QLabel* label_reteta = new QLabel{ "Reteta" };
    lyLst2->addWidget(label_reteta);
    lyLst2->addWidget(lst2);
    lyMain->addLayout(lyLst2);
    
    auto stgLy = new QVBoxLayout;
    auto formLy = new QFormLayout{};

    formLy->addRow("Denumire", txtNume);
    formLy->addRow("Pret", txtPret);
    formLy->addRow("Producator", txtProducator);
    formLy->addRow("Substanta", txtSubstanta);
    formLy->addRow("DenumireAux", txtNumeAux);
    formLy->addRow("ProducatorAux", txtProdAux);
    formLy->addRow("Numar", txtNumar);
    formLy->addRow("Fisier", txtFisier);
    stgLy->addLayout(formLy);

    auto lyBtn = new QHBoxLayout{};
    lyBtn->addWidget(btnAdd);
    lyBtn->addWidget(btnDel);
    lyBtn->addWidget(btnMod);
    lyBtn->addWidget(btnFnd);
    lyBtn->addWidget(btnExit);
    stgLy->addLayout(lyBtn);

    auto lyBtn2 = new QHBoxLayout{};
    lyBtn2->addWidget(btnFltP);
    lyBtn2->addWidget(btnFltS);
    lyBtn2->addWidget(btnSrtD);
    lyBtn2->addWidget(btnSrtP);
    lyBtn2->addWidget(btnSrtPr_S);
    stgLy->addLayout(lyBtn2);

    auto lyBtn3 = new QHBoxLayout{};
    lyBtn3->addWidget(btnClearR);
    lyBtn3->addWidget(btnWriteR);
    lyBtn3->addWidget(btnGenerateR);
    lyBtn3->addWidget(btnExportR);
    stgLy->addLayout(lyBtn3);

    lyMain->addLayout(stgLy);
    show();
}
