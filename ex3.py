def ex3(df):
    # Ex.3 - Qual foi o produto mais vendido?
    sales_by_product = df.groupby('Product')['Quantity Ordered'].sum()
    product_bigger_sales = sales_by_product.idxmax()
    print(f"Produto com maior número de vendas: {product_bigger_sales}")