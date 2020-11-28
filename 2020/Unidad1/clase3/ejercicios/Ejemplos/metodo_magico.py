class Processor:
    def __init__(self, name, status,):
        self.name = name
        self.status = status

    def run_script():
        print("nada")
    pass

class Manager:
    def __init__(self):
        # Puedo agregar a esta lista con '+'
        # y eliminar '-'
        # self.lista_procesos = list()
        self.dict_procesos = dict()

    def __add__(self, proceso: Processor):
        # self.lista_procesos.append(proceso)
        # {
        #   'proceso1': Processor('proceso1', 'waiting'),
        #   'proceso2': ...
        # }
        self.dict_procesos[proceso.name] = proceso

    def __sub__(self, proceso: Processor):
        # lista_proces -> Dict
        # for i, p in enumerate(self.lista_procesos):
            # if p.name == proceso.name:
                # self.lista_procesos.pop(i)
                # return
        del self.dict_procesos[proceso.name]

    # def __gt__(self, proceso: Processor):
    def __gt__(self, proceso: str)
        """Manager > "proceso1|running"
        """
        name, status = proceso.split("|")
        self.dict_procesos[name].status = status

        # proc = self.dict_procesos[proceso.name]
        # proc.status = proceso.status

    def __len__(self):
        return len(self.dict_procesos)








