def ex2(df):
    # Ex.2 - Qual cidade teve o maior número de vendas?
    df['City'] = df['Purchase Address'].apply(lambda x: x.split()[1])
    sales_by_city = df.groupby('City')['Quantity Ordered'].sum()
    city_bigger_sales = sales_by_city.idxmax()
    print(f"Cidade com maior número de vendas {city_bigger_sales}")