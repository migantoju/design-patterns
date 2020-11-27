"""
Decorator Pattern.
** También conocido como wrapper **

Es utilizado para que, dinámicamente se añada una nueva
funcionalidad a un objeto, sin cambiar la implementación
de éste. 
Es diferente a herencia porque la funcionalidad es añadida
solamente a un objeto en particular, no a la subclase entera.

Esta es como una envoltura, que envuelve al objeto y le añade 
la funcionalidad sin afectar los métodos que ya tenía.

"""

def italicize(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper


def bolder(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


@italicize
@bolder
def say_hi():
    return "Hi Urbvaners!"


def main():
    print(say_hi())


if __name__ == "__main__":
    main()

