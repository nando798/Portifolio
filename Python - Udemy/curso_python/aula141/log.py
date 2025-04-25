#Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"


class Log:
    def _log(self, msg):
        raise NotImplementedError("Método log não implementado")

    def log_error(self, msg):
        return self._log(f"Error: {msg}")
            
    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogFileMixin(Log):
    def _log (self, msg):
        msg_format = (f"{msg}")
        print("salvando no log...", msg_format)
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_format)
            arquivo.write("\n")
        

class LogPrintMixin(Log):
    def _log (self, msg):
        # print(f"{msg}{__class__.__name__}")
        print(f"{msg}")



if __name__=="__main__":
     l = LogPrintMixin()
     l.log_error('qualquer coisa')
     l.log_success('Que legal')
     lp = LogPrintMixin()
     lp.log_error('qualquer coisa')
     lp.log_success('Que legal')
     lf = LogFileMixin()
     lf.log_error('qualquer coisa')
     lf.log_success('Que legal')
