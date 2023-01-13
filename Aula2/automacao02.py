# Passo 1 - Importar a Base de Dados
import plotly.express as px
import pandas as pd
tabela = pd.read_csv(r"C:\Users\Dj Thor\Meus Projetos\Intensivao-Python\Aula 2\telecom_users.csv")
# Passo 2 - Visualizar a Base de Dados
# display(tabela)
print(tabela.info())
# Passo 3 - Tratamento de Dados
# Remover dados desnecessários
# Usar o método drop com os critérios nome da coluna e axis
# sendo axis=0 para eliminar linha e 1 para eliminar coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
# Remover os valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
print(tabela.info())
# Remover valores vazios
# Exclui as colunas em todos os valores são vazios 
tabela = tabela.dropna(how="all",axis=1) # how = all -> todos ou any -> para algum valor vazio
# Exclui as linha com pelo menos um valor são vazios
tabela = tabela.dropna(how="any",axis=0)
# Passo 4 - Análise inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True))
# Para formatar com casas decimais:
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
# Passo 5 - Análise Detalhada

# comparar cada coluna da base de dados com a coluna churn
# para instalar o plotly - biblioteca para gráficos
# pip install plotly
# Import plotly.express as px
# para edições nos gráficos : https://plotly.com/python/histograms/
# criar o gráfico
# cria o gráfico de acordo com a coluna especificado colorindo conforme o critério definido
# coluna="TipoContrato"
# grafico = px.histogram(tabela, x=coluna, color="Churn")
#exibe o gráfico
# grafico.show()
# para cada coluna da tabela, eu quero criar um gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
# Exibe o gráfico
    grafico.show()
