
class Pessoa:
    def __init__(self,id,nome,endereco):
        self.id=id
        self.nome=nome
        self.endereco=endereco
        
class Endereco:
    def __init__(self,rua,numero,cidade,estado,cep) :
        self.rua=rua
        self.numero=numero
        self.cidade=cidade
        self.estado=estado
        self.cep=cep

class Curso:
    def __init__(self,cod,nome):
        self.cod=cod
        self.nome=nome
class Disciplina:
    def __init__(self,nome,codigo,sala):
        self.nome=nome
        self.codigo=codigo
        self.sala=sala
class Professor(Pessoa):
    def __init__(self, id,nome, endereco):
        super().__init__(id,nome,endereco)
        
        
class Sala():
    def __init__(self,numero,capacidade):
        self.numero=numero
        self.capacidade=capacidade
        
        
class Aluno(Pessoa):
    def __init__(self, id, nome, endereco,curso):
        super().__init__(id, nome, endereco)
        self.curso=curso
        
class Servidor(Pessoa):
    def __init__(self, id, nome, cargo,departamento):
        super().__init__(id, nome,None)
        self.cargo=cargo
        self.departamento=departamento
        
class Diretor (Servidor): # Pessoa
    #def __init__(self, id, nome, endereco):  super().__init__(id, nome, endereco)
    
    def __init__(self, id, nome, cargo, departamento):
        super().__init__(id, nome, cargo, departamento)
        
class Coordenador(Servidor):# Pessoa
    #def __init__(self, id, nome, endereco):
      #  super().__init__(id, nome, endereco)
        # Servidor.__init__(id,nome,cargo)
    def __init__(self, id, nome, cargo, departamento,qual_Curso):
        super().__init__(id, nome, cargo, departamento)
        self.qual_curso=qual_Curso
        


# Criando instâncias de cada classe
endereco_pessoa = Endereco("Rua A", 123, "Serra talhada", "Pernambuco", "56903320-000")
pessoa = Pessoa(1, "João", endereco_pessoa)

curso = Curso(1, "BSI")
disciplina = Disciplina("Matemática discreta", 101, 15)

professor = Professor(2, "Maria", endereco_pessoa)

aluno = Aluno(3, "Geronimo S.N.", endereco_pessoa, curso)

servidor = Servidor(4, "Carlos", "Analista", "TI")

diretor = Diretor(5, "Ana", "Diretor", "Administração")

coordenador = Coordenador(6, "Júlia", "Coordenador", "Ensino", "BSI")

# Imprimindo informações de cada classe
print("Pessoa:")
print("ID:", pessoa.id)
print("Nome:", pessoa.nome)
print("Endereço:", pessoa.endereco.rua, pessoa.endereco.numero, pessoa.endereco.cidade, pessoa.endereco.estado, pessoa.endereco.cep)
print()

print("Curso:")
print("Código:", curso.cod)
print("Nome:", curso.nome)
print()

print("Disciplina:")
print("Nome:", disciplina.nome)
print("Código:", disciplina.codigo)
print("Sala:", disciplina.sala)
print()

print("Professor:")
print("ID:", professor.id)
print("Nome:", professor.nome)
print()

print("Aluno:")
print("ID:", aluno.id)
print("Nome:", aluno.nome)
print("Curso:", aluno.curso.nome)
print()

print("Servidor:")
print("ID:", servidor.id)
print("Nome:", servidor.nome)
print("Cargo:", servidor.cargo)
print("Departamento:", servidor.departamento)
print()

print("Diretor:")
print("ID:", diretor.id)
print("Nome:", diretor.nome)
print("Cargo:", diretor.cargo)
print("Departamento:", diretor.departamento)
print()

print("Coordenador:")
print("ID:", coordenador.id)
print("Nome:", coordenador.nome)
print("Cargo:", coordenador.cargo)
print("Departamento:", coordenador.departamento)
print("Curso:", coordenador.qual_curso)    
            