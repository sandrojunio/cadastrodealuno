import sqlite3
from ConexaoBanco import Conexao

class Cadastro_Aluno:

    def insert(self, nomeAluno, nomePai, nomeMae, telefoneAluno, emailAluno, enderecoAluno):
        
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
        
        try:

            sql = 'INSERT INTO Aluno (nomeAluno, nomePai, nomeMae, telefoneAluno, emailAluno, enderecoAluno) VALUES (?, ?, ?, ? ,? ,?)'

            cursor.execute(sql, (nomeAluno, nomePai, nomeMae, telefoneAluno,    emailAluno, enderecoAluno))
        
            conexao.commit()
            cursor.close()
            conexao.close()

            return "Cadastrado com sucesso!"
        except:
            return "Erro ao inserir aluno!"


