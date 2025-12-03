from threading import Thread
from threading import Lock
from time import sleep

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread("Thread 1", 12)
t1.start()

t2 = MeuThread("Thread 2", 3)
t2.start

t3 = MeuThread("Thread 3", 5)
t3.start()

for i in range(20):
    print(i)
    sleep(1)



def Vai_demorar(tempo, texto=str):
    try:
        sleep(tempo)
        print(texto)
    except Exception as e:
        print("Erro na thread", {e})


try:
    t1 = Thread(target=Vai_demorar, args=(2, "Olá mundo!"))
    t1.start()
    t1.join()
except Exception as e:
    print("Falha ao iniciar a thread", {e})

print("thread finalizada...")
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        with self.lock:
            if self.estoque < quantidade:
                print(f"Não temos ingressos disponíveis")
                self.lock.release()
                return

        sleep(1)  # Simula o tempo de processamento da compra
        self.estoque -= quantidade
        if self.estoque <= 0:
            print(f" Você comprou {quantidade} ingresso(s), estoque esgotado.")
        else:
            print(
                f" Você comprou {quantidade} ingresso(s), ainda temos {self.estoque} em estoque."
            )


if __name__ == "__main__":
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t1 = Thread(target=ingressos.comprar, args=(1,))
        t1.start()
        t1.join()
        sleep(0.1)
        if ingressos.estoque <= 0:
            print("Estoque esgotado — finalizando.")
            break
