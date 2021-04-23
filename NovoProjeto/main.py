from PyQt5 import uic, QtWidgets
from Aluno import Cadastro_Aluno
from Assunto import Cadastro_Assunto
from Home import home_db

from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

def consultarTudo():
    a = home_db()
    sql = a.selectAluno()

    Home.tabela.setRowCount(len(sql))
    row = 0
    for i in sql:
        Home.tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(i[1]))
        Home.tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[0])))
        Home.tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(i[2]))
        Home.tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(i[3]))
        Home.tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(i[4]))
        Home.tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(i[5]))
        Home.tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(i[6]))
        row=row+1 


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

    Home.tabela.setColumnWidth(0,120)
    Home.tabela.setColumnWidth(1,125)
    Home.tabela.setColumnWidth(2,124)
    Home.tabela.setColumnWidth(3,125)
    Home.tabela.setColumnWidth(4,125)
    Home.tabela.setColumnWidth(5,200)
    Home.tabela.setColumnWidth(6,200)
    

    consultarTudo()

def aluno():
    menu()
    Aluno.show()

    Home.close()
    Assunto.close()
    Atividade.close()
    Consulta.close()

    #Mensagem no campo vazio Ex.: Nome do aluno
    Aluno.nomeAluno.setPlaceholderText('Nome do aluno')
    Aluno.nomePai.setPlaceholderText('Nome do Pai')
    Aluno.nomeMae.setPlaceholderText('Nome da Mãe')
    Aluno.telefoneAluno.setPlaceholderText('(00)9 2345-1234')
    Aluno.emailAluno.setPlaceholderText('E-mail')
    Aluno.enderecoAluno.setPlaceholderText('Endereço')

    #Chamando botões da view, e chamando funções de cadastro e limpar
    Aluno.Bt_Cadastrar.clicked.connect(btCadastrarAluno)
    Aluno.Bt_Limpar.clicked.connect(btLimparAluno) 

# Evento de cadastrar
def btCadastrarAluno(self):
    
    # Chamando a classe aluno
    a = Cadastro_Aluno()

    # Try, para avisar dos errinhos e.e
    try:

        #Atribuindo os valores dos campos para imputar no banco de dados
        a.nomeAluno = Aluno.nomeAluno.text()
        a.nomePai = Aluno.nomePai.text()
        a.nomeMae = Aluno.nomeMae.text()
        a.telefoneAluno = Aluno.telefoneAluno.text()
        a.emailAluno = Aluno.emailAluno.text()
        a.enderecoAluno = Aluno.enderecoAluno.text()

        # Executando a função de inserção no manco de dados.
        if (Aluno.nomeAluno.text() != "" and Aluno.telefoneAluno.text() != "" and Aluno.emailAluno.text() != "" and Aluno.enderecoAluno.text() != ""):
            a.insert(a.nomeAluno, a.nomePai, a.nomeMae, a.telefoneAluno, a.emailAluno, a.enderecoAluno)
            btLimparAluno()
            
            return Aluno.Lb_cadastrado.setText('Cadastrado com sucesso!')
        else:
            return Aluno.Lb_cadastrado.setText('ERRO: Preencha os campos obrigatórios')
    except:
        return Aluno.Lb_cadastrado.setText('Erro no cadastro, line 117!')

#Removendo o valores dos campos através do botão LIMPAR
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

    Assunto.Lb_Assunto.setPlaceholderText('Nome do assunto')

    Assunto.Bt_Cadastro.clicked.connect(btCadastrarAssunto)

# Evento de cadastrar
def btCadastrarAssunto(self):

    # Chamando a classe assunto
    assunto = Cadastro_Assunto()

    try:
        #Atribuindo os valores dos campos para imputar no banco de dados
        assunto.nomeAssunto = Assunto.Lb_Assunto.text()

        if (Assunto.Lb_Assunto.text() != ""):
            assunto.insert(assunto.nomeAssunto)
            btLimparAssunto()

            return Assunto.Lb_cadastrado.setText('Cadastrado com sucesso!')
        else:
            return Assunto.Lb_cadastrado.setText('ERRO: Preencha os campos obrigatórios')
    except:
        return Assunto.Lb_cadastrado.setText('Erro no cadastro, line 117!')

def btLimparAssunto():
    Assunto.Lb_Assunto.setText('')

def atividade():
    menu()
    Atividade.show()

    Home.close()
    Aluno.close()
    Assunto.close()
    Consulta.close()

def desempenho():
    menu()
    Home.show() # Está sem exibição para esse modulo

    Assunto.close()
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