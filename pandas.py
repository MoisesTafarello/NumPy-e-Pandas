import pandas as pd
import os

# Lista para armazenar os registros
dados = []

# Preços fixos dos produtos
precos = {
    "Notebook": 3000,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 1200
}

print("=== Sistema de Vendas ===")
print("Produtos disponíveis e preços:")
for produto, preco in precos.items():
    print(f"- {produto}: R${preco}")

while True:
    nome = input("\nDigite o nome do cliente (ou 'sair' para encerrar): ").strip().title()
    if nome.lower() == "sair":
        break
    
    produto = input("Digite o produto comprado: ").strip().title()
    if produto not in precos:
        print("Produto inválido! Escolha um dos produtos listados.")
        continue
    
    quantidade = int(input("Digite a quantidade comprada: "))
    
    preco_unitario = precos[produto]
    valor_total = preco_unitario * quantidade
    
    dados.append({
        "Cliente": nome,
        "Produto": produto,
        "Quantidade": quantidade,
        "Preço Unitário (R$)": preco_unitario,
        "Valor Total (R$)": valor_total
    })
    
    os.system("cls")
    df = pd.DataFrame(dados)
    print("\n=== Registro de Vendas ===")
    print(df.to_string(index=False))
    input("\nPressione Enter para continuar...")

print("\nPrograma encerrado!")
