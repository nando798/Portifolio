
"""
Classes abstratas - Abstract base class (abc)
ABCs são usadas como contratps para a definica o de novas clases.
Elas podem forçar outras classes a criarem métodos concretos.
Tambem podem ter metodos concretps por elas mesmas.
@abstractmethods são metodos que nao tem corpo
As regrass para classes abstratas com métodos abstratos é que elas
mão podem ser instanciadas diretamente.
Métodos abstratos devem ser implementados nas subclasses (@abstractmethods)
Uma classe abstrata em pythjon tem sua metaclasse sendo ABCMeta,
É possível criare @property @setter @classmethoid @staticmethose @methos 
como abstratos, para isso use @abstractmethod como decorator mais interno.
"""
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        raise NotImplementedError("Método log não implementado")

    def log_error(self, msg):
        return self._log(f"Error: {msg}")
            
    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogFileMixin(Log):
    def _log (self, msg):
        msg_format = (f"{msg}")
        print(msg_format)
        # with open(LOG_FILE, "a") as arquivo:
        #     arquivo.write(msg_format)
        #     arquivo.write("\n")

l = LogFileMixin()
l.log_error('qualquer coisa')