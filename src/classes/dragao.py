from src.classes.personagem import Personagem
from src.classes.skill import Skill

class Dragao(Personagem):
    def __init__(self, nome, hp, mana, defesa, dano_base, dano_critico_base):
        super().__init__(nome, hp, mana, defesa, dano_base, dano_critico_base)

        cuspir_fogo = Skill('cuspir fogo', f'{self.nome} cospe uma enorme bola de fogo', 320)
        ataque_com_a_cauda = Skill('ataque com a cauda', f'{self.nome} faz um ataque rasteiro coma a cauda', 500)

        self.skills = [cuspir_fogo, ataque_com_a_cauda]

    def usar_cuspir_fogo(self):
        pass

    def usar_ataque_com_a_cauda(self):
        pass