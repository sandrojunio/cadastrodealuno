from PyQt5 import uic,QtWidgets

def menu():
    Home.pushButton.clicked.connect(aluno)
    Home.pushButton_2.clicked.connect(assunto)
    Home.pushButton_3.clicked.connect(atividade)
    Home.pushButton_4.clicked.connect(desempenho)
    Home.pushButton_5.clicked.connect(consulta)
    
    cadastrodealuno.pushButton.clicked.connect(aluno)
    cadastrodealuno.pushButton_2.clicked.connect(assunto)
    cadastrodealuno.pushButton_3.clicked.connect(atividade)
    cadastrodealuno.pushButton_4.clicked.connect(desempenho)
    cadastrodealuno.pushButton_5.clicked.connect(consulta)
    
    cadastrodeassunto.pushButton.clicked.connect(aluno)
    cadastrodeassunto.pushButton_2.clicked.connect(assunto)
    cadastrodeassunto.pushButton_3.clicked.connect(atividade)
    cadastrodeassunto.pushButton_4.clicked.connect(desempenho)
    cadastrodeassunto.pushButton_5.clicked.connect(consulta)
    
    cadastrodeatividade.pushButton.clicked.connect(aluno)
    cadastrodeatividade.pushButton_2.clicked.connect(assunto)
    cadastrodeatividade.pushButton_3.clicked.connect(atividade)
    cadastrodeatividade.pushButton_4.clicked.connect(desempenho)
    cadastrodeatividade.pushButton_5.clicked.connect(consulta)
    
    cadastrodeconsulta.pushButton.clicked.connect(aluno)
    cadastrodeconsulta.pushButton_2.clicked.connect(assunto)
    cadastrodeconsulta.pushButton_3.clicked.connect(atividade)
    cadastrodeconsulta.pushButton_4.clicked.connect(desempenho)
    cadastrodeconsulta.pushButton_5.clicked.connect(consulta)

def aluno():
    menu()
    cadastrodealuno.show()
    Home.close()
    cadastrodeassunto.close()
    cadastrodeatividade.close()
    cadastrodeconsulta.close()
    
   
def assunto():
    menu()
    cadastrodeassunto.show()
    Home.close()
    cadastrodealuno.close()
    cadastrodeatividade.close()
    cadastrodeconsulta.close()
    
    
def atividade():
    menu()
    cadastrodeatividade.show()
    Home.close()
    cadastrodealuno.close()
    cadastrodeassunto.close()
    cadastrodeconsulta.close()
    
    
def desempenho():
    menu()
    cadastrodeassunto.show()
    Home.close()
    cadastrodealuno.close()
    cadastrodeassunto.close()
    cadastrodeconsulta.close()
    
    
def consulta():
    menu()
    cadastrodeconsulta.show()
    Home.close()
    cadastrodealuno.close()
    cadastrodeassunto.close()
    
    
    
    
    
    
      
app=QtWidgets.QApplication([])
Home=uic.loadUi("Home.ui")
cadastrodealuno=uic.loadUi("cadastrodealuno.ui")
cadastrodeassunto=uic.loadUi("cadastrodeassunto.ui")
cadastrodeconsulta=uic.loadUi("cadastrodeconsulta.ui")
cadastrodeatividade=uic.loadUi("cadastrodeatividade.ui")

menu()


Home.show()
app.exec()