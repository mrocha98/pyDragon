from random import randint

class Personagem:
    def __init__(self, nome, hp, mana, defesa, dano_base, dano_critico_base):
        self.nome = nome.title()
        self._hp = hp
        self._mana = mana
        self.defesa = defesa
        self.dano_base = dano_base
        self.dano_critico_base = dano_critico_base

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana):
        self._mana = mana

    def __str__(self):
        tab = '\t-\t'
        return f'Personagem: {self.nome.title()} {tab} HP: {self.hp} {tab} MANA: {self.mana} {tab} '

    def jogar_dado(self):
        print(f'Pressione <enter> para que {self.nome} jogue o dado...\n')
        input()
        sorteado = randint(1, 7)
        print(f'{self.nome} tirou {sorteado}!\n')
        input()
        return sorteado

    def atacar(self, alvo):
        pass
