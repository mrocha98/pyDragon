from src.classes.personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, hp, mana, dano_base, dano_critico_base, qtd_pocoes_hp):
        super().__init__(nome, hp, mana, dano_base, dano_critico_base)
        self.qtd_pocoes_hp = qtd_pocoes_hp

    def __str__(self):
        heroi = super().__str__() + f'Poções de HP: {self.qtd_pocoes_hp}'
        heroi.replace('Personagem', 'Herói')
        return heroi
