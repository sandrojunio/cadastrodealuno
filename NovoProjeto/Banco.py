import sqlite3

class Banco():
    
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists aluno(
            matriculaAluno integer primary key autoincrement,
            nomeAluno text NOT NULL,
            telefoneAluno text NOT NULL,
            emailAluno text NOT NULL,
            enderecoAluno text NOT NULL,
            nomePai text,
            nomeMae text)""")

        c.execute("""create table if not exists assunto(
            codigoAssunto integer primary key autoincrement,
            nomeAssunto text NOT NULL)""")

        c.execute("""create table if not exists atividade(
            codigoAtividade integer primary key autoincrement,
            nomeAtividade text NOT NULL,
            periodoInicio text NOT NULL,
            periodoFim text NOT NULL,
            matriculaAluno_Id integer NOT NULL,
            codigoAssunto_Id integer NOT NULL,
            FOREIGN KEY (matriculaAluno_Id) REFERENCES aluno(matriculaAluno)
            FOREIGN KEY (codigoAssunto_Id) REFERENCES assunto(codigoAssunto))""")

        self.conexao.commit()
        c.close()

        