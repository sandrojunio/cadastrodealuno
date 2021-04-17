import sqlite3

class Conexao():
    
    def conectar(self):
        conexao = None #Inserindo um objeto nulo
        db_path = 'GestaoAluno.db' #Nome do banco de dados

        try:
            conexao = sqlite3.connect(db_path)
        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar ao banco de dados {db_path}.")

        return conexao

    #Criando tabela de alunos
    def createTableAluno(self, conexao, cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Aluno (matricula INTEGER PRIMARY KEY AUTOINCREMENT, nomeAluno text NOT NULL, nomePai text, nomeMae varchar, telefoneAluno text NOT NULL, emailAluno text NOT NULL, enderecoAluno text NOT NULL)'
        cursor.execute(sql)
        conexao.commit()

    #Criando tabela de assunto
    def createTableAssunto(self, conexao, cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Assunto (codigoAssunto INTEGER PRIMARY KEY AUTOINCREMENT, nomeAssunto varchar NOT NULL)'
        cursor.execute(sql)
        conexao.commit()

    #Criando tabela de atividades
    def createTableAtividade(self, conexao, cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Atividade (codigoAtividade INTEGER PRIMARY KEY AUTOINCREMENT, nomeAtividade varchar NOT NULL, periodoInicio date NOT NULL, periodoFIM date NOT NULL)'
        cursor.execute(sql)
        conexao.commit()

    #Conexçao
    def  createTables(self):
        #Criando a conexão
        conexao = self.conectar()
        #Criando o cursor 
        cursor = conexao.cursor()

        #Passando a conexão e cursor para as funções de criar tabelas.
        self.createTableAluno(conexao, cursor)
        self.createTableAssunto(conexao, cursor)
        self.createTableAtividade(conexao, cursor)
    

        