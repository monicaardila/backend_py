import pandas as pd
data1 = "Tablas/data1.xlsx"
data2 = "Tablas/data2.xlsx"

df1=pd.read_excel(data1)
df2=pd.read_excel(data2)

#concatenar nombre y apellido 
df1.nombre = df1.nombre.str.cat(df1.apellido)
#La diferencia entre Ingresos y egresos
df2['diferencia'] = df2['ingresos'] - df2['egresos']
print("\nLa diferencia entre Ingresos y egresos:\n", df2)

values1 = df1[["nit","nombre"]]
values2 = df2[["nit","ingresos","egresos","diferencia"]]

#Suma total de los ingresos 
total_egresos = df2.egresos.sum()
print(total_egresos)
#values3 = total_egresos[["total_egresos"]]
#Suma total de los egresos
total_ingresos = df2.ingresos.sum()
print(total_ingresos)
#La diferencia entre Ingresos y egresos

#tamaño del nit
tamano_nit = df2.nit.count()
print(tamano_nit)

#Promedio Ingresos
promedio_ingresos=(total_egresos/tamano_nit)
print(promedio_ingresos)

#Promedio Egresos
promedio_egresos=(total_ingresos/tamano_nit)
print(promedio_egresos)

#Ingreso Máximo
ingresos_max = df2.ingresos.max()
print(ingresos_max)

#Ingreso  Mínimo
ingresos_min = df2.ingresos.min()  
print(ingresos_min)

#Egreso Máximo
egresos_max = df2.egresos.max()
print(egresos_max)

#Egreso Mínimo
egresos_min = df2.egresos.min()
print(egresos_min)
#inner de las tablas
inner_join_df = pd.merge(values1,values2, on='nit',how='inner')
#tabla = (inner_join_df,values3)
df_3 = pd.DataFrame({"Total Egresos": [total_egresos]})
df_4 = pd.DataFrame({"Total Ingresos": [total_ingresos]})
df_5 = pd.DataFrame({"Promedio Ingresos": [promedio_ingresos]})
df_6 = pd.DataFrame({"Promedio Engresos": [promedio_egresos]})
df_7 = pd.DataFrame({"Ingresos Maximo": [ingresos_max]})
df_8 = pd.DataFrame({"Ingresos Minimo": [ingresos_min]})
df_9 = pd.DataFrame({"Egresos Maximo": [egresos_max]})
df_10 = pd.DataFrame({"Egresos Minimo": [egresos_min]})
x=pd.concat([inner_join_df,df_3,df_4,df_5,df_6,df_7,df_8,df_9,df_10], axis=1)
x.to_csv("Tablas/prueba.csv")