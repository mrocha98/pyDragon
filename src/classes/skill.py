class Skill:
    def __init__(self, nome, descricao, custo):
        self.nome = nome.title()
        self.descricao = descricao
        self.custo = custo

    def __str__(self):
        return f'{self.nome}:\n{self.descricao}\nCusto: {self.custo} de MANA'