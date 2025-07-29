# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
parcelas = 60
data_emprestimo = datetime.strptime("20/12/2020", "%d/%m/%Y")
data_final = data_emprestimo + relativedelta(months=parcelas)

valor_parcela = valor_emprestimo / parcelas
data_atual = data_emprestimo + relativedelta(months=parcelas)

print(f"Data do empréstimo: {data_emprestimo.strftime('%d/%m/%Y')}")
print(f"Data final do empréstimo:{data_final.strftime('%d/%m/%Y')}")
print(f"valor de cada parcela: R$ {valor_parcela:,.2f}")
print("Datas de vencimento e valores das parcelas:")

for i in range(parcelas):
    data_vencimento = data_emprestimo + relativedelta(months=i)
    print(f"{i+1}): {data_vencimento.strftime('%d/%m/%Y')} - R$ {valor_parcela:,.2f}")

print(
    f"Você pegou um empréstimo de: R$ {valor_emprestimo:,.2f} para pagar em {parcelas}x de {valor_parcela:,.2f} cada."
)
print()
