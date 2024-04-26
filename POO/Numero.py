#crie uma classe Numero que deverá ter um atributo n do tipo float. 
# Nessa classe, implemente os métodos:
#float fatorial() que deverá retornar n!
#float potencial (int x) que deverá retornar a parte inteira n
# float parteDecimal() que deverá retornar  a parte decimal de n

class Numero:
    
    n: float
    
    def __init__(self, n: float) -> None:
        self.n = n
        
    def fatorial(self) -> float:
        fat = 1
        for i in range(1, int(self.n)+1):
            fat *= i
        return fat
    
    def potencial(self, x: int) -> float:
        return self.n ** x 
    
    def parteInteira(self) -> float:
        return int(self.n)
    
    def parteDecimal(self) -> float:
        return self.n % 1   
    
n1 = Numero(5.5)
print(n1.fatorial())