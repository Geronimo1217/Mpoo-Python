class Aluno:
    def __init__(self, matricula, nome, cpf, curso):
        self.matricula = matricula
        self.nome = nome
        self.__cpf = cpf
        self.curso = curso
        self.disciplinas_matriculadas = []

    def get_cpf(self):
        return self.__cpf

    def matricular(self, disciplina):
        self.disciplinas_matriculadas.append(disciplina)

    def desmatricular(self, disciplina):
        self.disciplinas_matriculadas.remove(disciplina)


class Curso:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.nome = nome
        self.disciplinas = []
        self.alunos_matriculados = []

    def get_codigo(self):
        return self.__codigo

    def imprimir_curso(self):
        for disciplina in self.disciplinas:
            print(f'Disciplinas do curso: {disciplina.nome}')

    def add_disciplinas(self, disciplinas):
        self.disciplinas.extend(disciplinas)

    def adicionar_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


class Disciplina:
    def __init__(self, id, nome, professor, sala):
        self.__id = id
        self.nome = nome
        self.professor = professor
        self.alunos_matriculados = []
        self.sala = sala

    def get_id(self):
        return self.__id

    def add_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)


class Professor:
    def __init__(self, matricula, nome):
        self._matricula = matricula
        self.nome = nome
        self.disciplinas = []

    def add_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def get_matricula(self):
        return self._matricula


class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.disciplina = None


curso1 = Curso(123, "Sistemas de Informação")
professor1 = Professor(567, "Prof. Geronimo S.N.")
sala1 = Sala(12, 40)
disciplina1 = Disciplina(7, "MPOO", professor1, sala1)
aluno1 = Aluno(1458900, "Geronimo ", "310.343.456-00", curso1)

curso1.add_disciplinas([disciplina1])
professor1.add_disciplina(disciplina1)
sala1.disciplina = disciplina1
print("=======<>  <>=======")
curso1.imprimir_curso()

print("=======<> ABA ALUNO <>=======")
print(f"Aluno: {aluno1.nome} | Curso: {curso1.nome}")
print()
print("=======<> ABA PROFESSOR <>=======")
print(f"Professor: {professor1.nome}")
print()
print("=======<> ABA DISCIPLINA <>=======")
print(f"Disciplina: {disciplina1.nome} | Professor: {disciplina1.professor.nome} | Sala: {disciplina1.sala.numero}")

