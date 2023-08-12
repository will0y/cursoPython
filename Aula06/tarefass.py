class Listadetarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tare(self, tarefa):
        self.tarefas.append(tarefa)

    def exibir_tarefas(self):
        for i, tarefa in enumerate(self, tarefas, start ==1):
            print(f"(i). {tarefa}")

    