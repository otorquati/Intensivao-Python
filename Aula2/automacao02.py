# Passo 1 - Importar a Base de Dados
import pandas as pd
tabela = pd.read_csv(r"../Aula2/telecom_users.csv")
# Passo 2 - Visualizar a Base de Dados
# display(tabela)
print(tabela)
# Passo 3 - Tratamento de Dados
# Remover dados desnecessários
# Usar o método drop com os critérios nome da coluna e axis
# sendo axis=0 para eliminar linha e 1 para eliminar coluna
# tabela = tabela.drop("Unmaned: 0", axis=1)
