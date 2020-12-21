"""
    *Singleton Pattern*

Este patrón es implementado comunmente en lugares donde se requiere un control
sobre el acceso a recursos compartidos, como una conexión a base de datos. De
esta manera nos aseguramos de que una clase sera utilizada unicamente para crear
una sola instancia y proveer un solo punto de acceso global.

*PROS*
- La creación de una sola instancia, nos permite el acceso al mismo objeto
  en multiples puntos de nuestra app, sin tener miedo a que se sobreescriba en
  algún punto del programa.
"""
class Person:
    __instance = None

    def __init__(self):
        if Person.__instance is None:
            Person.__instance = self
        else:
            raise Exception("you can't create more than one instance for class Person")

    @staticmethod
    def get_instance():
        if not Person.__instance:
            Person()
        return Person.__instance


def main():
    person1 = Person()
    print(person1)

    copy_person1 = person1.get_instance()
    print(copy_person1)
    
    new_person1 = Person()
    print(new_person1)

if __name__ == "__main__":
    main()


