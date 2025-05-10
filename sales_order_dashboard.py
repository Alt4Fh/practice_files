import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv('superstore.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    ## convert category to categorical data

    df['Category'] = df['Category'].astype('category')
    return


@app.cell
def _(df):
    df['Category'].dtype
    return


@app.cell
def _(df):
    ## convert column names to lower case for better accessing
    df.columns = df.columns.str.lower()
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    # rename colums repalce .  with _
    df.rename(columns={'order.id': 'order_id', 'customer.name' : 'customer_name', 'customer.id' : 'customer_id', 'product.id': 'product_id', 'product.name': 'product_name',  'row.id' : 'row_id', 'ship.date' : 'ship_date',  'ship.mode':  'ship_mode', 'shipping.cost': 'shipping_cost', 'sub.category': 'sub_category' }, inplace=True)

    return


@app.cell
def _(df):
    df.rename(columns={'order.priority': 'order_priority'}, inplace=True)
    return


@app.cell
def _(df):
    df.rename(columns={'order.date': 'order_date'}, inplace=True)

    return


@app.cell
def _():
    # easy way 
    # df.columns = df.columns.str.replace('.', '_')
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df["total_amount"] = (df['sales'] * df['quantity']) + df['shipping_cost']
    return


@app.cell
def _(df):
    df['total_profit'] = df['profit'] * df['quantity']
    return


@app.cell
def _(df, pd):
    ## converting order_date to datetime object

    df['order_date'] = pd.to_datetime(df['order_date'])
    return


@app.cell
def _(df, pd):
    ## converting ship_date to datetime object

    df['ship_date'] = pd.to_datetime(df['ship_date'])
    return


@app.cell
def _(df):
    ## converting ship mode to categorical data 

    df['ship_mode'] = df['ship_mode'].astype('category')
    return


@app.cell
def _(df):
    df['sub_category'] = df['sub_category'].astype('category')
    return


@app.cell
def _(df):
    # summary statictics

    total_sales = df['total_amount'].sum()
    total_orders = df['order_id'].nunique()
    total_customers = df['customer_id'].nunique()
    return total_customers, total_orders, total_sales


@app.cell
def _(df):
    sales_by_products = df.groupby('product_id')['total_amount'].sum().sort_values(ascending=False)
    return (sales_by_products,)


@app.cell
def _(df):
    #order overtime

    df['month'] = df['order_date'].dt.to_period('M')
    sales_by_month = df.sort_values( by="month", ascending=True).groupby('month')['total_amount'].sum()

    return (sales_by_month,)


@app.cell
def _(total_customers, total_orders, total_sales):
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Total Customers: {total_customers}")
    print("\nOrders by Status:")
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    return np, plt, sns


@app.cell
def _(sns):
    # setup plot style
    sns.set(style='whitegrid')

    return


@app.cell
def _(plt, sales_by_products):
    # 1. Sales by Product (Top 10)
    top_products = sales_by_products.head(10)
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Product ID')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.show()
    return


@app.cell
def _(plt, sales_by_month):
    # order over time
    plt.figure(figsize=(10,6))
    sales_by_month.plot(kind='line', marker='o', color='orange')
    plt.title('Sales ovet the month')
    plt.xlabel('Months')
    plt.ylabel('Total sales ($)')
    plt.xticks(rotation=45)
    plt.show()
    return


@app.cell
def _():
    import datetime as dt

    return


@app.cell
def _(df, pd):
    # Calculate the most recent date in the dataset
    current_date = df['order_date'].max() + pd.DateOffset(days=1)
    return (current_date,)


@app.cell
def _(current_date):
    current_date
    return


@app.cell
def _(current_date, df):
    # Calculate RFM metrics
    rfm_df = df.groupby('customer_id').agg(
        recency = ('order_date', lambda x: (current_date - x.max()).days),
        frequency = ('order_id', 'nunique'),
        monetry = ('total_amount', 'sum')
    ).reset_index()
    return (rfm_df,)


@app.cell
def _(rfm_df):
    rfm_df.head()
    return


@app.cell
def _(pd):
    def rfm_score(df):
        df['recency_score'] = pd.qcut(df['recency'], 5, labels=[5,4,3,2,1])
        df['frequency_score'] = pd.qcut(df['frequency'], 5, labels=[1,2,3,4,5])
        df['monetry_score'] = pd.qcut(df['monetry'], 5, labels=[1,2,3,4,5])
        df['rfm_score'] = df['recency_score'].astype(str) + df['frequency_score'].astype(str) + df['monetry_score'].astype(str)
        return df
    return (rfm_score,)


@app.cell
def _(rfm_df, rfm_score):
    rfm_df1 = rfm_score(rfm_df)
    return (rfm_df1,)


@app.cell
def _(rfm_df1):
    rfm_df1
    return


@app.cell
def _(np, pd):
    def segment_customers(df:pd.DataFrame):
        ## df is rfm_df
        conditions = [
            (df['rfm_score'] == '555'),
            (df['rfm_score'].str.startswith('5')),
            (df['rfm_score'].str.endswith('1')),
            (df['rfm_score'].str.startswith('1') & df['rfm_score'].str.endswith('1'))
        ]
        choices = ['champions', 'loayal customers', 'At Risk', 'New Customers']

        df['cusomer_segment'] = np.select(conditions, choices, default='other')
        return df
    return (segment_customers,)


@app.cell
def _(rfm_df1, segment_customers):
    rfm_df2 = segment_customers(rfm_df1)
    return (rfm_df2,)


@app.cell
def _(rfm_df2):
    rfm_df2.head()
    return


@app.cell
def _(df):
    ### sales by product

    product_sales = df.groupby(by='product_id').agg(total_sales=('sales', 'sum'), total_quantity = ('quantity', 'sum')).reset_index()
    return (product_sales,)


@app.cell
def _(product_sales):
    product_sales_sorted = product_sales.sort_values(by='total_sales', ascending=False)
    return (product_sales_sorted,)


@app.cell
def _(product_sales_sorted):
    ## top 10 products by sales
    top_10_products = product_sales_sorted.head(10)
    return (top_10_products,)


@app.cell
def _(plt, top_10_products):
    plt.figure(figsize=(10,6))
    plt.bar(top_10_products['product_id'], top_10_products['total_sales'], color='skyblue')
    plt.title('Top 10 product by total sales')
    plt.xlabel('Product ID')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.show()
    return


@app.cell
def _(df, pd):
    df['order_date'] = pd.to_datetime(df['order_date'])
    return


@app.cell
def _(df):
    df['month_year'] = df['order_date'].dt.to_period('M')
    return


@app.cell
def _(df):
    df['month_year'].dtype
    return


@app.cell
def _(df):
    df['product_id'] = df['product_id'].astype('category')
    return


@app.cell
def _(df):
    monthly_sales = df.groupby(by=[ 'product_id', 'month_year']).agg(monthly_sales = ('total_amount', 'sum')).reset_index()
    return (monthly_sales,)


@app.cell
def _(monthly_sales):
    monthly_sales.isna().any()
    return


@app.cell
def _(monthly_sales):
    monthly_sales['monthly_sales'].dtype
    return


@app.cell
def _(monthly_sales):
    monthly_sales.pivot_table(columns='month_year', index="product_id", values='monthly_sales')
    return


if __name__ == "__main__":
    app.run()
