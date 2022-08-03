#Estacionamento

class Veiculo:
    def __init__(self, tipo, placa):
        self.tipo = tipo
        self.placa = placa
        self.estacionado = False
 
    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

    def __str__(self) -> str:
        return f'O veículo é um {self.tipo}, de placa {self.placa} e é {self.estacionado} que está estacionado'

class Carro(Veiculo):
    def __init__(self, tipo, placa):
        super().__init__(tipo, placa)

    def status_estacionamento(self):
        print(f'O veículo é um {self.tipo}, de placa {self.placa} e é {self.estacionado} que está estacionado')

class Moto(Veiculo):
    def __init__(self, tipo, placa):
        super().__init__(tipo, placa)

    def status_estacionamento(self):
        print(f'O veículo é um {self.tipo}, de placa {self.placa} e é {self.estacionado} que está estacionado')

carro1 = Carro('Carro', 'AAA0000')
carro1.estacionar()
carro1.status_estacionamento()

# moto1 = Moto('Moto', 'BBB0000')
# moto1.sair_da_vaga()
# moto1.status_estacionamento()


class Vaga:
    def __init__(self, id, tipo, placa):
        self.id = id #random
        self.tipo = tipo
        self.livre = True
        self.placa = placa

    def ocupar(self):
        self.livre = False

    def desocupar(self):
        self.livre = True

    def status_vaga(self):
        if self.livre == True :
            print(f'A vaga de id {self.id}, é do tipo {self.tipo} e está livre')
        elif self.livre == False:
            print(f'A vaga de id {self.id}, é do tipo {self.tipo}, está ocupada e o veículo tem placa {self.placa}')

vaga1 = Vaga ('789','Carro','AAA0000')
vaga1.ocupar()
vaga1.status_vaga()  

class Estacionamento:
    def __init__(self):
        self.vagas_de_carro = 5
        self.vagas_de_moto = 5
        self.carro_para_vaga = 0
        self.moto_para_vaga = 0
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_somente_moto = 5
        self.total_vagas_livres_global = 10

    def estacionar_carro(self):
        if self.carro_para_vaga < self.vagas_de_carro:
            self.carro_para_vaga += 1
        else:
            print(f'Não há mais vagas para carros no estacionamento')

    def estacionar_moto(self):
        if self.moto_para_vaga < self.vagas_de_moto:
            self.moto_para_vaga += 1
        elif self.moto_para_vaga < self.total_vagas_livres_global:
            self.moto_para_vaga += 1
        else:
            print('Não existe mais nenhuma vaga no estacionamento')


    def remover_carro(self):
        self.carro_para_vaga -= 1

    def remover_moto(self):
        self.moto_para_vaga -= 1

    def estado_do_estacionamento(self):
        self.total_vagas_livres_carro = self.vagas_de_carro - self.carro_para_vaga
        self.total_vagas_livres_somente_moto = self.vagas_de_moto - self.moto_para_vaga #colocar if
        self.total_vagas_livres_global = (self.vagas_de_carro + self.vagas_de_moto) - (self.carro_para_vaga + self.moto_para_vaga)
        print(f'O estacionamento possui {self.total_vagas_livres_global} vagas totais, sendo que delas, {self.total_vagas_livres_somente_moto} são vagas onde somente motos estacionam e {self.total_vagas_livres_carro} são vagas livres preferencialmente para carros')

estacionamento1 = Estacionamento()
estacionamento1.estado_do_estacionamento()









