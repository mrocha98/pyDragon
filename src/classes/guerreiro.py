from src.classes.heroi import Heroi
from src.classes.skill import Skill

class Guerreiro(Heroi):
        def __init__(self, nome, hp, mana, defesa, dano_base, dano_critico_base, qtd_pocoes_hp):
            super().__init__(nome, hp, mana, defesa, dano_base, dano_critico_base, qtd_pocoes_hp)

            oracao = Skill('oração', f'{self.nome} faz uma oração aos Deuses, pedindo por uma cura', 400)
            espada_das_mil_laminas = Skill('espada das mil lâminas', f'{self.nome} ataca com uma espada lendária', 500)
            espada_demoniaca = Skill('espada demoníaca', f'{self.nome} ataca com uma espada amaldiçoada', 350)
            self.skills = [oracao, espada_das_mil_laminas, espada_demoniaca]

        def usar_oracao(self):
            pass

        def usar_espada_das_mil_laminas(self):
            pass

        def usar_espada_demoniaca(self):
            pass


