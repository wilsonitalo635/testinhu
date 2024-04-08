class Pessoa:
    def __init__(self, nome, matricula, sexo, idade):
        self.nome = nome
        self.matricula = matricula
        self.sexo = sexo
        self.idade = idade
if __name__ == "__main__":
    pessoa1 = Pessoa("Wilson","090909","M","18")
    print(pessoa1.nome)
    print(pessoa1.matricula)
    print(pessoa1.sexo)
    print(pessoa1.idade)
    pessoa2 = Pessoa("Josiva","0303030","M","42")
    print(pessoa2.nome)
    print(pessoa2.matricula)
    print(pessoa2.sexo)
    print(pessoa2.idade)
    pessoa3 = Pessoa("Pedro","848484","M","17")
    print(pessoa3.nome)
    print(pessoa3.matricula)
    print(pessoa3.sexo)
    print(pessoa3.idade)