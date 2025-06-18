from __future__ import annotations

class Personagem:  
    def __init__(self, nome):
        # Atributos
        self.nome =  nome
        self.vida_maxima = 100
        self.vida_atual = 100
        self.ataque = 30
        self.defesa = 40
        self.cartas = []
        self.energia = 100
        self.energia_maxima = 100
        
    def atacar(self, inimigo: Personagem, heroi: Personagem):
        dano = heroi.ataque
        dano = max(0,dano) # Pro dano não ser negativo
        inimigo.vida_atual -= dano
        print(f"{heroi.nome} atacou {inimigo.nome} causando {dano} de dano!")
 
    def usar_carta(personagem: Personagem, inimigo: Personagem, indice: int):
        # Verifica se o número digitado pelo jogador é válido
        if indice < 1 or indice > len(personagem.cartas):
           print(f"Carta Inválida.")
           return
       
        carta = personagem.cartas[indice - 1]
        
        # Reduz a energia a cada carta usada
        if personagem.energia < carta.energia_gasta:
            print(f"{personagem.nome} não tem energia suficiente para usar {carta.nome}.")
            return
        
        personagem.energia -= carta.energia_gasta
        print(f"{personagem.nome} usou a carta {carta.nome}")
        
        # Remove a carta após o uso
        personagem.cartas.pop(indice -1)
        print(f"A carta {carta.nome} foi descartada do deck. \n")
        
    def comprar_carta(self, inimigo: Personagem, heroi: Personagem):
        pass
    
    def levar_dano(self):
        pass
    
    def ver_cartas(self, personagem: Personagem):
        print(f"Cartas de {personagem.nome}:")
        if not personagem.cartas:
            print("Nenhuma carta no momento.")
        else:
            for i, carta in enumerate(personagem.cartas, 1):
                print(f"{i}. {carta.nome} - Custa {carta.energia_gasta} de energia\n {carta.descricao}")   
                    
    def curar_se(self):
        pass
                
    