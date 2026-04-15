# função que cria conta
def criar_conta(id, titular, saldo, limite, status):
    conta = {"id": id, "titular": titular, "saldo": saldo, "limite": limite, "status": status}
    return conta


# função que cria o depositar, o sacar e ver o extrato
def deposita(conta, valor): 
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é de {}".format(conta["saldo"]))
