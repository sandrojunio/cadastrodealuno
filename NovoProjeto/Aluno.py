from Banco import Banco

class Aluno(object):
    def __init__(self, matriculaAluno=0, nomeAluno="", telefoneAluno="", emailAluno="", enderecoAluno="", nomePai="", nomeMae=""):
        self.info={}
        self.matriculaAluno = matriculaAluno
        self.nomeAluno = nomeAluno
        self.telefoneAluno = telefoneAluno
        self.emailAluno = emailAluno
        self.enderecoAluno = enderecoAluno
        self.nomePai = nomePai
        self.nomeMae = nomeMae

    def insertAluno(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("insert into aluno (nomeAluno, telefoneAluno, emailAluno,enderecoAluno, nomePai, nomeMae) values ('" + self.nomeAluno + "','" + self.telefoneAluno + "','" + self.emailAluno + "','" + self.enderecoAluno + "','" + self.nomePai + "','" + nomeMae + "')")

            banco.conexao.commit()
            c.close()

            return "Aluno cadastrado com sucesso!"
        except:
            return "Error: Erro no cadastro de aluno!"

    def updateAluno(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("update aluno set matriculaAluno= '" + self.matriculaAluno + "',nomeAluno= '" + self.nomeAluno + "',telefoneAluno= '" + self.telefoneAluno + "',emailAluno='" + "',enderecoAluno='" + self.nomePai + "'nomeMae='" + self.nomeMae + " ")

            banco.conexao.commit()
            c.close()

            return "Aluno atualizado com sucesso!"
        except:
            return "Error: Falha na alteração de usuário"

    def selectAluno(self, matricula):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute(
                "select * from empregados WHERE matricula=" + matricula + " ")

            for linha in c:
                self.matriculaAluno = linha[0]
                self.nomeAluno = linha[1]
                self.telefoneAluno = linha[2]
                self.emailAluno = linha[3]
                self.enderecoAluno = linha[4]
                self.nomePai = linha[5]
                self.nomeMae = linha[6]

            c.close()
        except:
            return "Error: Erro ao consultar registro"