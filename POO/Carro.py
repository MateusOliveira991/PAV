class Carro:
    cilindrada: float
    combustível: str
    transmissao: str
    ano: int
    nome: str
    marca: str
    
    def __init__(self, cilindrada: float, combustivel: str, transmissao: str, ano: int, nome: str, marca:str) -> None:
        
        self.cilindrada = cilindrada
        self.combustivel = combustivel
        self.transmissao = transmissao
        self.ano = ano
        self.nome = nome
        self.marca = marca
    
    def acelera(self):
        pass

    def freia(self):
        pass
    

Carro1 = Carro(1.0, 'Flex', 'Manual', 2015, 'Onix', 'Fiat')


print(f"Carro: {Carro1.nome} Marca: {Carro1.marca} e ano :{Carro1.ano}")


