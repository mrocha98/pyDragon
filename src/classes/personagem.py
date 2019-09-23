class Personagem:
    def __init__(self, nome, hp, mana, dano_base, dano_critico_base):
        self.nome = nome
        self._hp = hp
        self._mana = mana
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