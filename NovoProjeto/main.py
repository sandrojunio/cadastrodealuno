from PyQt5 import uic, QtWidgets
from Db_CadastroAluno import Cadastro_Aluno

def menu():
    Home.Bt_CadastroAluno.clicked.connect(aluno)
    Home.Bt_CadastroAssunto.clicked.connect(assunto)
    Home.Bt_CadastroAtividade.clicked.connect(atividade)
    Home.Bt_CadastroDesempenho.clicked.connect(desempenho)
    Home.Bt_CadastroConsulta.clicked.connect(consulta)

    Aluno.Bt_CadastroAluno.clicked.connect(aluno)
    Aluno.Bt_CadastroAssunto.clicked.connect(assunto)
    Aluno.Bt_CadastroAtividade.clicked.connect(atividade)
    Aluno.Bt_CadastroDesempenho.clicked.connect(desempenho)
    Aluno.Bt_CadastroConsulta.clicked.connect(consulta)

    Assunto.Bt_CadastroAluno.clicked.connect(aluno)
    Assunto.Bt_CadastroAssunto.clicked.connect(assunto)
    Assunto.Bt_CadastroAtividade.clicked.connect(atividade)
    Assunto.Bt_CadastroDesempenho.clicked.connect(desempenho)
    Assunto.Bt_CadastroConsulta.clicked.connect(consulta)

    Atividade.Bt_CadastroAluno.clicked.connect(aluno)
    Atividade.Bt_CadastroAssunto.clicked.connect(assunto)
    Atividade.Bt_CadastroAtividade.clicked.connect(atividade)
    Atividade.Bt_CadastroDesempenho.clicked.connect(desempenho)
    Atividade.Bt_CadastroConsulta.clicked.connect(consulta)

    Consulta.Bt_CadastroAluno.clicked.connect(aluno)
    Consulta.Bt_CadastroAssunto.clicked.connect(assunto)
    Consulta.Bt_CadastroAtividade.clicked.connect(atividade)
    Consulta.Bt_CadastroDesempenho.clicked.connect(desempenho)
    Consulta.Bt_CadastroConsulta.clicked.connect(consulta)

def aluno():
    menu()
    Aluno.show()
    Home.close()
    Assunto.close()
    Atividade.close()
    Consulta.close()

    Aluno.nomeAluno.setPlaceholderText('Nome do aluno')
    Aluno.nomePai.setPlaceholderText('Nome do Pai')
    Aluno.nomeMae.setPlaceholderText('Nome da Mãe')
    Aluno.telefoneAluno.setPlaceholderText('(00)12345-1234')
    Aluno.emailAluno.setPlaceholderText('E-mail')
    Aluno.enderecoAluno.setPlaceholderText('Endereço')

    Aluno.Bt_Cadastrar.clicked.connect(btCadastrarAluno)
    Aluno.Bt_Limpar.clicked.connect(btLimparAluno)

def btCadastrarAluno(self):
    a = Cadastro_Aluno()
    a.nomeAluno = Aluno.nomeAluno.text()
    a.nomePai = Aluno.nomePai.text()
    a.nomeMae = Aluno.nomeMae.text()
    a.telefoneAluno = Aluno.telefoneAluno.text()
    a.emailAluno = Aluno.emailAluno.text()
    a.enderecoAluno = Aluno.enderecoAluno.text()

    a.insert(nomeAluno, nomePai, nomeMae, telefoneAluno, emailAluno, enderecoAluno)

def btLimparAluno():
    Aluno.nomeAluno.setText('')
    Aluno.nomePai.setText('')
    Aluno.nomeMae.setText('')
    Aluno.telefoneAluno.setText('')
    Aluno.emailAluno.setText('')
    Aluno.enderecoAluno.setText('')

    
def assunto():
    menu()
    Assunto.show()

    Home.close()
    Aluno.close()
    Atividade.close()
    Consulta.close()

def atividade():
    menu()
    Atividade.show()

    Home.close()
    Aluno.close()
    Assunto.close()
    Consulta.close()

def desempenho():
    menu()
    Assunto.show() # Está sem exibição para esse modulo

    Home.close()
    Aluno.close()
    Consulta.close()

def consulta():
    menu()
    Consulta.show()

    Home.close()
    Aluno.close()
    Assunto.close()

app = QtWidgets.QApplication([])
Home = uic.loadUi("Home.ui")
Aluno = uic.loadUi("Aluno.ui")
Assunto = uic.loadUi("Assunto.ui")
Atividade = uic.loadUi("Atividade.ui")
Consulta = uic.loadUi("Consulta.ui")
menu()

Home.show()
app.exec()
