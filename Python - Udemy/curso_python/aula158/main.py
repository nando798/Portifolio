from abc import ABC
from dataclasses import dataclass


@dataclass
class Pessoa(ABC):
    nome: str
    idade: int

    @property
    def nome(self):
        # retornas o nome da pessoa
        return self._nome

    @property
    def idade(self):
        # retorna a idade da pessoa
        return self._idade

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @idade.setter
    def idade(self, idade: int):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        # retorna a conta do cliente
        return self._conta

    @conta.setter
    def conta(self, conta):
        if not isinstance(conta, Conta):
            raise ValueError("conta deve ser uma instancia de Conta")
        self.cona = conta


class Conta(ABC):
    def __init__(self, agencia: str, numero: str, saldo: float = 0.0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        # retorna a agencia da conta
        return self.agencia

    @property
    def numero(self):
        # retorna o numero da conta
        return self.numero

    @property
    def saldo(self):
        # retorna o saldo ca conta
        return self._saldo

    @property
    def detalhes(self, msg: str = ""):
        return f"{msg} - Agencia: {self.agencia}, Numero: {self.numero}, Saldo: {self.saldo}"

    @agencia.setter
    def agencia(self, agencia: str):
        if not agencia:
            raise ValueError("Agencia no pode ser vazia")
        self.agencia = agencia

    @numero.setter
    def numero(self, numero: str):
        raise ValueError("Numero não pode ser vazio")
        self.numero = numero

    @saldo.setter
    def saldo(self, saldo: float):
        if saldo < 0:
            raise ValueError("saldo não pode ser negativo")
        self._saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("Deposito deve ser maior que zero")
        self.saldo += valor
        print(f"Deposito de {valor} realizado, saldo atual é: {self.saldo}")

    def sacar(self, sacar: int):
        raise NotImplementedError("Metodo sacar deve ser implementado na subclasse")


class ContaCorrente(Conta):
    def __init__(self, agencia: str, numero: int, saldo: int, limite: int = 0):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    @property
    def limite(self):
        # retorna o limite da conta
        return self._limite

    @limite.setter
    def limite(self, limite: int):
        if limite < 0:
            raise ValueError("Limite não pode ser menor que zero")
        self._limite = limite

    def sacar(self, sacar: int, valor: int):
        if sacar <= 0:
            raise ValueError("Saque deve ser maior que zero")
        if sacar > self.saldo + self._limite:
            raise ValueError("Saque maior que saldo mais o limite")
        self.sacar = sacar
        self.saldo -= valor
        print(f"Saque de {valor} realizado, Saldo atual é: {self.saldo}")
        return self.saldo


class ContaPoupanca(Conta):
    def __init__(self, agencia: str, numero: int, saldo: int):
        super().__init__(agencia, numero, saldo)

    def sacar(self, sacar: int, saldo: int):
        if sacar <= 0:
            raise ValueError("Saque deve ser maior que zero")
        if sacar > self.saldo + self.limite:
            raise ValueError("Saque maior que saldo mais o limite")
        self.sacar = sacar
        self.saldo -= saldo
        return self.saldo


class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def __str__(self):
        return f"Banco: {self.nome}"

    @property
    def nome(self):
        # retorna o nome do banco
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        if not nome:
            raise ValueError("Nome do banco nao pode estar vazio")
        self._nome = nome

    def autenticar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise ValueError("Cliente deve ser uma instancia de cliente")
        if cliente not in self.clientes:
            raise ValueError("Cliente não encontrado no banco")
        return True

    def autenticar_conta(self, conta: Conta):
        if not isinstance(conta, Conta):
            raise ValueError("Conta deve ser uma instancia de conta")
        if conta not in self.contas:
            raise ValueError("Conta não encontrada no banco")
        return True

    def autenticar_agencia(self, agencia: str):
        if not agencia:
            raise ValueError("Agencia não pode estar vazia")
        if agencia not in [agencia.agencia for agencia in self.contas]:
            raise ValueError("Agencia não encontrada no banco")
        return True

    def autenticar(self, cliente: str, agencia: int, conta: int):
        if not self.autenticar_cliente(cliente):
            raise ValueError("Cliente não autenticado")
        if not self.autenticar_conta(conta):
            raise ValueError("Conta não autenticada")
        if not self.autenticar_agencia(agencia):
            raise ValueError("Agencia não autenticada")
        return True

    def adicionar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise ValueError("Cliente deve ser uma instancia de Cliente")
        if cliente in self.clientes:
            raise ValueError("Cliente já existe no banco")
        self.clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        if not isinstance(conta, Conta):
            raise ValueError("Conta deve ser uma instancia de conta")
        if conta in self.contas:
            raise ValueError("Conta já existe no banco")
        self.contas.append(conta)

    def realizar_deposito(self, cliente: Cliente, conta: Conta, valor: float):
        if not self.autenticar(cliente, conta.agencia, conta.numero):
            raise ValueError("Cliente ou conta nao autenticados")
        conta.depositar(valor)
        print(
            f"Deposito de {valor} realizado com sucesso na conta {conta.numero} do cliente {cliente.nome}"
        )

    def realizar_saque(self, cliente: Cliente, conta: Conta, valor: float):
        if not self.autenticar(cliente, conta.agencia, conta.numero):
            raise ValueError("Cliente ou conta não autenticados")
        conta.sacar(valor)
        print(
            f"Saque de {valor} realizado com sucesso na conta {conta.numero} do cliente{cliente.nome}"
        )


# Exemplo de uso
if __name__ == "__main__":
    # criando instancias de banco, cliente e contas
    banco = Banco("Nubank")
    cp1 = ContaCorrente("0001", "123456", 1000, 500)
    cp1.sacar(300, 200)
    cp1.depositar(1500)
