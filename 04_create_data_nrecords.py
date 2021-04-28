import sqlite3

conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Criando uma lista de dados
lista = [
    ('Vinicius', '28', '444444444444', 'Viniciusdojava@gmail.com', '1234-5678', 'Rio de Janeiro',
     'RJ', '1992-01-01'),
    ('Renata', '150', ' 555555555555', 'RenatadoFront@gmail.com', '11-1234-6600', 'Florianopólis',
     'SC', '01-01-1800'),
    ('FabioProfessorTopzeira', '48', '666666666666', 'Fabiotocadordeviola@gmail.com', '1245-5667', 'Sao Paulo',
     'SP', '1976-06-19')
]

# Inserindo dados na tabela
cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)

conn.commit()

print("Dados inseridos com sucesso!")

conn.close()
