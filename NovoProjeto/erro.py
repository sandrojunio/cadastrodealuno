from PyQt5 import uic,QtWidgets

def aluno():
    cadastrodealuno.show()
    Home.close()
   
def assunto():
    cadastrodeassunto.show()
    Home.close()
    
def atividade():
    cadastrodeassunto.show()
    Home.close()
    
def desempenho():
    cadastrodeassunto.show()
    Home.close()
    
def consulta():
    cadastrodeassunto.show()
    Home.close()
    
    
    
      
app=QtWidgets.QApplication([])
Home=uic.loadUi("Home.ui")
cadastrodealuno=uic.loadUi("cadastrodealuno.ui")
cadastrodeassunto=uic.loadUi("cadastrodeassunto.ui")
Home.Aluno.clicked.connect(aluno)
Home.Assunto.clicked.connect(assunto)
Home.Atividade.clicked.connect(atividade)
Home.Desempenho.clicked.connect(desempenho)
Home.Consulta.clicked.connect(consulta)


Home.show()
app.exec()