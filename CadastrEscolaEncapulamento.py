class Aluno:
    def __init__(self,matricula,nome,cpf,curso) :
        self.matricula=matricula
        self.nome=nome
        self.__cpf=cpf
        self.curso=curso
        self.diciplina_matriculadas=[]
        
    def get_cpf(self):
        return self.__cpf
    
    def matricular(self, disciplina):
        self.disciplinas_matriculadas.append(disciplina)

    def desmatricular(self, disciplina):
        self.disciplinas_matriculadas.remove(disciplina)
        
        
class Curso:
    def __init__(self,cod,nome) :
        self.__cod=cod
        self.nome=nome
        self.diciplinas=[]
        self.aluno_matriculados=[]
        
    def get_cod(self):
        return self.__cod
    
    def imprimirCurso(self):
        for diciplina in self.diciplinas:
            print(f'diciplinas {diciplina}')
        
    def add_diciplina(self,*diciplina):
        self.diciplinas.extend(diciplina)
    
            
    def adicionar_aluno(self,aluno):
        self.aluno_matriculados.append(aluno)
        
class Endereco:
    def __init__(self,rua, numero,bairro, cidade,estado) :
        self.rua=rua
        self.numero=numero
        self.bairro=bairro
        self.cidade=cidade
        self.estado=estado
        
class Disciplina:
    def __init__(self, id, nome, professor, sala):
        self.__id = id
        self.nome = nome
        self.professor = professor
        self.alunos_matriculados=[]  # dddddd
        self.sala = sala
    
    def get_id(self):
        return self.__id
    
    def add_aluno(self,aluno):  #dddddd
        self.alunos_matriculados.append(aluno)
        
class Professor():
    def __init__(self, matricula, nome):
        self._matricula = matricula
        self.nome = nome
        self.diciplinas=[]
        
    def add_diciplina(self, diciplina):
        self.diciplinas.append(diciplina)

    def get_id(self):
        return self._id
    
class Sala():
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.disciplina = None
        
curso1 = Curso(1, "Sistemas de Informação")



endereco1 = Endereco("Rua Fulano de Tal", 101, "Serra Talhada", "Pernambuco", "12345-678")
endereco2 = Endereco("Rua ABC", 123, "Triunfo", "Pernambuco", "87654-321")
professor1 = Professor(5, "Prof. Erisvaldo")
sala1 = Sala(12, 40)
disciplina1 = Disciplina(7, "MPOO", professor1, sala1)
aluno1 = Aluno(1, "Cleiton", curso1, endereco1)

print("=======<> ABA ALUNO <>=======")
print("Aluno:", aluno1.nome, "|", aluno1._id, "|", "| Curso:", curso1.nome, "| Endereço:", aluno1.endereco.rua, ",", aluno1.endereco.cidade, ",", aluno1.endereco.estado)
print()
print("=======<> ABA PROFESSOR <>=======")
print("Professor:", professor1.nome, "|", professor1._id, "|",  "| Endereço:", endereco2.rua, ",", endereco2.cidade, ",", endereco2.estado)
print()
print("=======<> ABA DISCIPLINA <>=======")
print("Disciplina:", disciplina1.nome,"|", disciplina1._id, "|", "| Professor:", disciplina1.professor.nome, "| Sala:", disciplina1.sala.numero)