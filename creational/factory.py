"""
Factory Method Pattern.

Define una interfaz o clase abstracta para crear un objeto pero,
permite a las subclases decidir cual clase instanciar. En otras
palabras, las subclases son responsables de crear instancias de las
clases.

Esta fabrica produce objetos, sin la necesidad de crear la clase exacta
del objeto que se creará. Para lograr esto, los objetos se crean llamando
a un método `factory` en lugar de llamar un a un método constructor.

Nuestra método factory crea y retorna instancias.

"""

from abc import ABC, abstractmethod


class Adapter(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()


class DjangoAdapter(Adapter):
    def execute(self):
        print("Adapter de Django")


class KafkaAdapter(Adapter):
    def execute(self):
        print("Adapter de Kafka")


class MongoAdapter(Adapter):
    def execute(self):
        print("Adapter de Mongo")


def adapter_factory(name: str) -> Adapter:
    try:
        _dict = {
            "django": DjangoAdapter,
            "kafka": KafkaAdapter,
            "mongo": MongoAdapter
        }
        return _dict[name]()
    except KeyError as e:
        raise Exception(str(e))

def main():
    name = "django"

    adapter = adapter_factory(name)
    
    adapter.execute()


if __name__ == "__main__":
    main()

