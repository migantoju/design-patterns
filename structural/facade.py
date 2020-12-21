"""
    *Facade Pattern*

Proporciona una interfaz unificada más simple a un sistema complejo.
Proporciona una forma más sencilla de acceder a los métodos de los sistemas
subyacentes al proporcionar un único punto de entrada.

Oculta la complejidad de los sitemas y provee una interfaz al cliente
con la cual puede acceder al sistema/sistemas.

*PROS*
- 
*CONS*
- Cambios en métodos, los métodos están atados a la capa Facade, esto quiere
  decir que cualquier cambio en los métodos, también se deberá cambiar en la
  capa facade, lo cual no es favorable.
"""
class CPU:
    def freeze(self):
        print("freezing cpu....")

    def stuff(self):
        print("making cpu stuff....")


class Memory:
    def load(self):
        print("making memory stuff...")


class SSD:
    def stuff(self):
        print("making ssd's stuff....")


class ComputerFacade:

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()

    def start(self):
        self.cpu.freeze()
        self.memory.load()
        self.ssd.stuff()
        self.cpu.stuff()


def main():
    computer_facade = ComputerFacade()
    computer_facade.start()

if __name__ == "__main__":
    main()



