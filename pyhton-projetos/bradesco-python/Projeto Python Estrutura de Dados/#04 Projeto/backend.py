# Criando os comandos do Banco de Dados
import sqlite3 as sql

class TransactionObject():
    database = 'clientes.db'
    conn = None
    cur = None
    connected = False

    def connect(self):
        '''Conecta ao banco de dados'''
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        '''Desconecta do banco de dados'''
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        '''Executa uma consulta SQL'''
        if self.connected:
            if parms is None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
        
    def fetchall(self):
        '''Retorna todos os resultados da consulta'''
        return TransactionObject.cur.fetchall()
    
    def persist(self):
        '''Confirma as alterações no banco de dados'''
        if self.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

class DatabaseManager:
    def __enter__(self):
        self.trans = TransactionObject()
        self.trans.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.trans.disconnect()

    def execute(self, query, params=()):
        self.trans.execute(query, params)
        return self.trans.fetchall()

    def persist(self):
        self.trans.persist()

def initDB():
    with DatabaseManager() as db:
        db.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)')
        db.persist()

def insert(nome, sobrenome, email, cpf):
    with DatabaseManager() as db:
        db.execute('INSERT INTO clientes VALUES(NULL, ?,?,?,?)', (nome, sobrenome, email, cpf))
        db.persist()

def view():
    with DatabaseManager() as db:
        return db.execute('SELECT * FROM clientes')

def search(nome='', sobrenome='', email='', cpf=''):
    with DatabaseManager() as db:
        return db.execute('SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?', (nome, sobrenome, email, cpf))

def delete(id):
    with DatabaseManager() as db:
        db.execute('DELETE FROM clientes WHERE id=?', (id,))
        db.persist()

def update(id, nome, sobrenome, email, cpf):
    with DatabaseManager() as db:
        db.execute('UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?', (nome, sobrenome, email, cpf, id))
        db.persist()

initDB()
