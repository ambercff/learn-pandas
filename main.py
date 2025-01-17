import pandas as pd
import matplotlib.pyplot as plt
import ex1
import ex2
import ex3

def create_csv():
    data = {
        'Order ID': [1, 2, 3, 4],
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Quantity Ordered': [1, 2, 1, 1],
        'Price Each': [1000, 20, 50, 200],
        'Order Date': ['2023-01-01', '2023-02-01', '2023-01-02', '2023-01-02'],
        'Purchase Address': ['123 Elm St', '456 Oak St', '789 Pine St', '101 Maple St']
    }

    # Criando o DataFrame
    df = pd.DataFrame(data)
    df.to_csv('sales_data.csv', index = False)
    print("DataFrame foi criado com sucesso!")

def read_csv():
        # 1. Leitura do csv
    df = pd.read_csv('sales_data.csv')

    # 2. Tratamento de dados
    df.dropna(inplace = True) # Utiliza-se o inplace para não criar outro arquivo, apenas substituir esse
    
    # 2.1 Convertendo os tipos
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
    df['Price Each'] = pd.to_numeric(df['Price Each'])
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # 3. Criar novas colunas, derivadas das colunas originais, a fim de alcançar o objetivo dos exercícios
    df['Month'] = df['Order Date'].dt.month
    df['Total Sales'] = df['Quantity Ordered'] * df['Price Each']

    return df

if __name__ == '__main__':
    create_csv()
    df = read_csv()

    ex1.ex1(df)
    ex2.ex2(df)
    ex3.ex3(df)