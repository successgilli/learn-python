
class Base:
    _registry: dict[str, type] = {}

    def __init_subclass__(cls):
        print('labala')
        Base._registry[cls.mimetype] = cls

class TextType(Base):
    mimetype = 'text'

    def do(self):
        print(f'I am {TextType.mimetype}')


print(Base._registry['text']().do())
