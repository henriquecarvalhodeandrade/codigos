class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula

class Disciplina:
    def __init__(self, nome: str, codDisciplina: str):
        self.nome = nome
        self.codDisciplina = codDisciplina

class Turma:
    def __init__(self):
        self.alunos = []
        self.disciplina = None
        
class BDescola:
    def __init__(self, ):
        self.listaAlunos = []
        self.listaDisciplinas = []
        self.listaTurmas = []

    def cadastrarAluno(self, nome, matricula): 
        aluno = Aluno(nome, matricula)
        self.listaAlunos.append(aluno)
        print("--aluno cadastrado \n")

    def cadastrarDisciplina(self, nome, codDisciplina):
        disciplina = Disciplina(nome, codDisciplina)
        self.listaDisciplinas.append(disciplina)
        print("--disciplina cadastrada \n")

    def cadastrarTurma(self, aluno, disciplina): 
        turma = Turma(aluno, disciplina)
        self.listaTurmas.append(turma)
        print("--turma cadastrada \n")

    def mostrarTurmas(self, ):
        if self.listaTurmas == []:
            print('Turmas vazias \n')
            return
        
        for turma in self.listaTurmas:
            print(turma.disciplina, turma.alunos, "\n") 
            
    def adicionarAlunoEmTurma(self, aluno, turma):
        for turma in self.listaTurmas:
            turma.alunos.append(aluno)
            print("--aluno adicionado \n")

    def mostrarAlunos(self, ):
        if self.listaAlunos == []:
            print('Sem alunos \n')
            return
        
        for aluno in self.listaAlunos:
            print(aluno, "\n") 

    def mostrarDisciplinas(self, ): 
        if self.listaDisciplinas == []:
            print('Sem disciplinas \n')
            return
        
        for disciplina in self.listaDisciplinas:
            print(disciplina, "\n") 