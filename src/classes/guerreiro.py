from src.classes.heroi import Heroi
from src.classes.skill import Skill

class Guerreiro(Heroi):
        def __init__(self, nome, hp, mana, dano_base, dano_critico_base, qtd_pocoes_hp):
            super().__init__(nome, hp, mana, dano_base, dano_critico_base, qtd_pocoes_hp)

        def bencao_dos_deuses(self):
            pass


