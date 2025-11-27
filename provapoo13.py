class ContaBancaria:
    """
    Representa uma conta bancária simples.
    Demonstra o encapsulamento com atributos internos (_saldo).
    """
    def __init__(self, titular, saldo_inicial=0):
        # Atributos internos (convenção de "privado" em Python)
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        """Realiza um depósito, garantindo que o valor seja positivo."""
        if valor > 0:
            self._saldo += valor
            print(f"✅ Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("❌ Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Realiza um saque, verificando saldo e valor positivo."""
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"✅ Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("⚠️ Saldo insuficiente para realizar o saque.")
        else:
            print("❌ Erro: O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        """Exibe o saldo atual e o titular da conta."""
        print(f"\n--- Detalhes da Conta ---")
        print(f"Titular: {self._titular}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("-------------------------\n")

    # Método para obter o titular (útil para o menu de demonstração)
    def get_titular(self):
        return self._titular


def menu_bancario(conta):
    """Função principal que executa o menu interativo."""
    titular = conta.get_titular()
    print(f"\n==============================================")
    print(f"🏦 Bem-vindo(a) ao Banco Digital de {titular} 🏦")
    print(f"==============================================\n")
    
    while True:
        print("--- Menu de Operações ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Saldo")
        print("4. Sair")
        
        try:
            opcao = input("Escolha uma opção (1-4): ")
            
            if opcao == '1':
                valor = float(input("Digite o valor para depósito: R$"))
                conta.depositar(valor)
                
            elif opcao == '2':
                valor = float(input("Digite o valor para saque: R$"))
                conta.sacar(valor)
                
            elif opcao == '3':
                conta.exibir_saldo()
                
            elif opcao == '4':
                print(f"\n👋 Obrigado por usar o Banco Digital, {titular}. Volte sempre!")
                break
                
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 4.")
                
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número para a operação ou valor.")
        
        # Aguarda um enter para continuar, melhorando a leitura do console
        input("\nPressione ENTER para continuar...")


# --- Execução do Programa ---
# 1. Cria a conta
minha_conta = ContaBancaria("Lucas Cunha", 1000)

# 2. Inicia o menu
menu_bancario(minha_conta)