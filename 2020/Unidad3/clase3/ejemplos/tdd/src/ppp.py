
dict_ganadores = {
    'papel': 'piedra',
    'piedra': 'tijera',
    'tijera': 'papel',
}

def ejecucion(opcion1, opcion2):
    if dict_ganadores[opcion1] == opcion2:
        return opcion1

