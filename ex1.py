def ex1(df):
    # Ex.1 - Qual mês teve o maior volume de vendas?
    sales_by_month = df.groupby('Month')[['Quantity Ordered', 'Total Sales']].sum()
    month_bigger_sales = sales_by_month['Total Sales'].idxmax()  # Retorna o índice do maior valor

    print(f"Mês com maior volume de vendas: {month_bigger_sales}")
