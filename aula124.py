class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        if self.filmando:
            print('Você já está filmando')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True


    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.nome} não estava filmando...')
            return
        self.filmando = False
        print('A filmagem foi parada!')


    def fotografar(self):
        if self.filmando:
            print('Não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')


c1= Camera('Canon')
c2= Camera('Sony')

c1.parar_filmagem()
c1.filmar()
c1.filmar()
c1.parar_filmagem()
c1.fotografar()
