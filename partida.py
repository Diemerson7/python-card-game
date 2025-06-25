class Partida:
    def __init__(self, jogador1, jogador2):
        self.turno = 1
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador1

    def iniciar(self):
        print(f"Iniciando a partida entre {self.jogador1.nome} e {self.jogador2.nome}. \n")
        print(f"{self.jogador_atual.nome} começa! \n")
        
        while True: 
            self.informacoes1
            self.informacoes2
            
            print(f"É a vez do {self.jogador_atual.nome}. \n")
            print(f"1 - Usar uma carta")
            print(f"2 - Passar a vez")
            print(f"3 - Atacar")
            
            escolha = input()
            escolha = int(escolha)
            print(f"O jogador escolheu a opção {escolha}. \n")
            
            if escolha == 1: 
                print(f"O jogador escolheu usar uma carta. \n")
                self.jogador_atual.ver_cartas()
                escolha_carta = 
                
            if escolha == 2:
                print(f"O jogador escolheu passar a vez. \n")
                
            if escolha == 3:
                print(f"O jogador escolheu atacar. \n")
            
                        
                        
    def trocar_turno(self):
        self.turno += 1
        self.trocar_jogador()
        print(f"Turno {self.turno}: Agora é o {self.jogador_atual.nome}.")
        
        if self.jogador1.vida_atual <= 0 or self.jogador2.vida_atual <= 0:
            self.acabar()
            
    def informacoes1(self):
        print(f" {self.jogador1} \n")
        print(f" Vida: {self.jogador1.vida_atual}/{self.jogador1.vida_maxima} ")
        print(f" Escudo: {self.jogador1.defesa} ")
        print(f" Ataque: {self.jogador1.ataque} ")
        print(f" Energia: {self.jogador1.energia}/{self.jogador1.energia_maxima} /n/n ")
            
    def informacoes2(self):
        print(f" {self.jogador2} \n")
        print(f" Vida: {self.jogador2.vida_atual}/{self.jogador2.vida_maxima} ")
        print(f" Escudo: {self.jogador2.defesa} ")
        print(f" Ataque: {self.jogador2.ataque} ")
        print(f" Energia: {self.jogador2.energia}/{self.jogador2.energia_maxima} /n/n ")            
            
    def trocar_jogador(self):
        if self.jogador == self.jogador1:
            self.jogador_atual = self.jogador2
        else:
            self.jogador_atual = self.jogador1
            
    def acabar(self):
        vencedor = self.jogador1 if self.jogador1.vida_atual > 0 else self.jogador2
        print(f"Fim de jogo! {vencedor.nome} venceu.")