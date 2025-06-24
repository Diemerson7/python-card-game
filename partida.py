class Partida:
    def __init__(self, jogador1, jogador2):
        self.turno = 1
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador1

    def iniciar(self):
        print(f"Iniciando a partida entre {self.jogador1.nome} e {self.jogador2.nome}.")
        print(f"{self.jogador_atual.nome} começa!")
        
    def trocar_turno(self):
        self.turno += 1
        self.trocar_jogador()
        print(f"Turno {self.turno}: Agora é o {self.jogador_atual.nome}.")
        
        if self.jogador1.vida_atual <= 0 or self.jogador2.vida_atual <=0:
            self.acabar()
            
    def trocar_jogador(self):
        if self.jogador == self.jogador1:
            self.jogador_atual = self.jogador2
        else:
            self.jogador_atual = self.jogador1
            
    def acabar(self):
        vencedor = self.jogador1 if self.jogador1.vida_atual > 0 else self.jogador2
        print(f"Fim de jogo! {vencedor.nome} venceu.")