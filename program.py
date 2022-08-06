import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt
import statistics as sts

dataset = pd.read_csv("data\\Churn.csv", sep=";")
print(f'{dataset.shape}\n')
print(f'{dataset.head()}\n')
dataset.columns = ["Id", "Score", "Estado", "Genero", "Idade",
                "Patrimonio", "Saldo", "Produtos", "TemCartaoCredito", "Ativo", "Salario", "Saiu"]
print(f'{dataset.head()}\n')
print(f'{dataset.columns}\n')


#Verificando e corrigindo a ocorrencia de valores nulos#

#Identificando#
print(f'{dataset.isnull().sum()}\n')
dataset.isnull().sum().plot.bar().set_title("Valores nulos por colunas")
plt.tight_layout()
plt.show()

#Corrigindo #
group = dataset.groupby(["Genero"]).size()
print(f'{group}\n')
moda = "Masculino"
dataset["Genero"].fillna(moda, inplace=True)

print('{dataset["Salario"].describe()}\n')
median = sts.median(dataset["Salario"])
dataset["Salario"].fillna(median, inplace=True)

#Verificando#
dataset.isnull().sum().plot.bar().set_title("Valores nulos por colunas após correção")
plt.tight_layout()
plt.show()

#Identificando e corrigindo valores duplicados na coluna id#

print(f'{dataset.duplicated().sum()}\n')
print(f'{dataset[dataset["Id"].duplicated(keep=False)]}\n')
dataset.drop_duplicates(subset="Id", keep="first", inplace=True)
print(f'{dataset[dataset["Id"].duplicated(keep=False)]}\n')


#Procurando e corrigindo outliers e valores invalidos em cada uma das colunas.#

group = dataset.groupby(["Estado"]).size()
print(f'{group}\n')
group.plot.bar(color = "blue")
plt.show()

moda = "RS"
dataset.loc[dataset["Estado"].isin(['RS', 'SC', 'PR']) == False, "Estado"] = moda

group = dataset.groupby(["Estado"]).size()
group.plot.bar(color = "blue").set_title("Coluna Estado após correção")
plt.show()


print(f'{dataset["Salario"].describe()}\n')
plt.figure(1)
plt.subplot(2, 1, 1)
srn.boxplot(x=dataset["Salario"])
plt.subplot(2, 1, 2)
srn.histplot(x=dataset["Salario"])
plt.tight_layout()
plt.show()

dev = sts.stdev(dataset["Salario"]) * 2
print(f'{dev}\n')
print(f'{dataset.loc[dataset["Salario"] >= dev]}\n')
median = sts.median(dataset["Salario"])
print(f'{median}\n')
dataset.loc[dataset["Salario"] >= dev, "Salario"] = median

srn.boxplot(x=dataset["Salario"]).set_title("Coluna Salario após correçao")
plt.show()


group = dataset.groupby(["Genero"]).size()
print(f"{group}\n")
group.plot.bar().set_title("Gênero")
plt.tight_layout()
plt.show()

dataset.loc[dataset["Genero"] == "M", "Genero"] = "Masculino"
dataset.loc[dataset["Genero"].isin(["F", "Fem"]), "Genero" ] = "Feminino"

group = dataset.groupby(["Genero"]).size()
print(f"{group}\n")
group.plot.bar().set_title("Coluna Gênero após correção")
plt.tight_layout()
plt.show()


print(f'{dataset["Score"].describe()}\n')
plt.figure(1)
plt.subplot(2, 1, 1)
srn.histplot(x = dataset["Score"])
plt.subplot(2, 1, 2)
srn.boxplot(x = dataset["Score"])
plt.tight_layout()
plt.show()


print(f'{dataset["Idade"].describe()}\n')
print(f'{dataset.loc[(dataset["Idade"] > 120) | (dataset["Idade"] < 0)]}\n')
plt.figure(1)
plt.subplot(2, 1, 1)
srn.histplot(x= dataset["Idade"])
plt.subplot(2, 1, 2)
srn.boxplot(x= dataset["Idade"])
plt.tight_layout()
plt.show()

median = sts.median(dataset["Idade"])
print(f'{median}\n')
dataset.loc[(dataset["Idade"] > 120) | (dataset["Idade"] <= 0), "Idade"] = median

print(f'{dataset.loc[(dataset["Idade"] > 120) | (dataset["Idade"] < 0)]}\n')
srn.boxplot(x = dataset["Idade"]).set_title("Coluna Idade após correção")
plt.show()


print(f'{dataset["Patrimonio"].describe()}\n')
srn.boxplot(x= dataset["Patrimonio"])
plt.show()


print(f'{dataset["Saldo"].describe()}\n')
srn.boxplot(x=dataset["Saldo"])
plt.show()
srn.displot(x=dataset["Saldo"])
plt.show()


print(f'{dataset["Produtos"].describe()}\n')
srn.boxplot(x=dataset["Produtos"], color="blue")
plt.show()


group = dataset.groupby(["TemCartaoCredito"]).size()
print(f'{group}\n')
group.plot.bar()
plt.show()


print(f'{dataset["Ativo"].head()}\n')
group = dataset.groupby(["Ativo"]).size()
print(f'{group}\n')
group.plot.bar()
plt.show()


group = dataset.groupby(['Saiu']).size()
print(f'{group}\n')
group.plot.bar()
plt.show()


print(f'{dataset.head()}\n')
print(dataset.shape)