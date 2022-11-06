# decoradores


def agregar_pan(f):
    def crear_hamburguesa(*args,**kwargs):
        _hamburguesa = f"{f(*args,**kwargs)} Pan"
        return _hamburguesa
    return crear_hamburguesa

def agregar_queso(f):
    def crear_hamburguesa(*args,**kwargs):
        _hamburguesa = f"{f(*args,**kwargs)} Queso"
        return _hamburguesa
    return crear_hamburguesa

def agregar_lechuga(f):
    def crear_hamburguesa(*args,**kwargs):
        _hamburguesa = f"{f(*args,**kwargs)} Lechuga"
        return _hamburguesa
    return crear_hamburguesa


def agregar_tomate(f):
    def crear_hamburguesa(*args,**kwargs):
        _hamburguesa = f"{f(*args,**kwargs)} Tomate"
        return _hamburguesa
    return crear_hamburguesa
    

@agregar_pan
@agregar_queso
@agregar_lechuga
@agregar_tomate
def hamburguesa():
    return "Pan"




print(f"Mi hamburguesa contiene {hamburguesa()}")