

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    df = pd.read_csv('superstore1.csv', low_memory=False)
    return df, pd


@app.cell
def _(df):
    df.head(5)
    #df.drop(columns=['Ship Date.1'], inplace=True)
    return


@app.cell
def _(df):
    ## drop where all columns are nan
    df.dropna(how='all', inplace=True)
    return


@app.cell
def _(df):
    # chack if any order date has nan value
    df['Order Date'].isna().any()
    return


@app.cell
def _(df):
    def date_clean(date_str):
        if not isinstance(date_str, str):
            return date_str
        '''
        1. apened zero if month is less than 10th
        2. convert to format of dd/mm/yyyy from mm/dd/yyyy
        3. check if any month less than 10th have leadin 0 if not
           add leading zero
        4. join with -
        '''
        if '/' in date_str:
            date_str = date_str.strip()
            try:
                month, day, year = date_str.split('/')
                day = f"{int(day):02d}"
                month = f"{int(month):02d}"
                return f"{day}-{month}-{year}"
            except Exception:
                return date_str  # Or return None, or raise
        return date_str

    order_date =  df['Order Date'].apply(date_clean)
    return (order_date,)


@app.cell
def _(df, order_date, pd):
    df['Order Date'] = pd.to_datetime(order_date, format="mixed")
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    ### check if there is any missing values
    df.isna().any()
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    ## converting category column to categorical type column for fast data process
    df['Category'] = df['Category'].astype('category')
    return


@app.cell
def _(df):
    ## converting sub-category column to categorical type column for fast data process
    df['Sub-Category'] = df['Sub-Category'].astype('category')
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    # check for any duplilcatess

    df.duplicated().any()
    return


@app.cell
def _(df):
    df.agg(total_sales = ('Sales', 'sum'), total_profit = ('Profit', 'sum'), avg_discount = ('Discount', 'mean'))
    return


@app.cell
def _(df):
    ## top 5 states by total sales
    df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
    return


@app.cell
def _(df):
    ## bottom 5 state by profit

    df.groupby('State')['Profit'].sum().sort_values(ascending=True).head(5)
    return


@app.cell
def _(df):
    # profitc margin by state

    df_state_summary = df.groupby('State', as_index=False).agg({'Profit': 'sum', 'Sales': 'sum'})
    return (df_state_summary,)


@app.cell
def _(df_state_summary):
    df_state_summary['profit_margin'] = (df_state_summary["Profit"] / df_state_summary['Sales']) * 100
    return


@app.cell
def _(df_state_summary):
    df_state_summary
    return


@app.cell
def _(df):
    df_cat = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})
    return (df_cat,)


@app.cell
def _(df_cat):
    df_cat['profit_margin'] = (df_cat['Profit'] / df_cat['Sales'])*100
    return


@app.cell
def _(df_cat):
    df_cat.loc[df_cat['profit_margin'] == df_cat['profit_margin'].max()]
    return


@app.cell
def _(df):
    average_delivery_time = (df['Ship Date'] - df['Order Date']).sum() / df.count()
    return (average_delivery_time,)


@app.cell
def _(average_delivery_time):
    average_delivery_time
    return


@app.cell
def _(df):
    ## all the orders where profit is negative

    df.loc[df['Profit'] < 0 ]
    return


@app.cell
def _(df):
    ## top 10 orders with highest sales
    df.sort_values('Sales', ascending=False)['Order ID'].head(10)

    return


@app.cell
def _(df):
    ## find order placed in dec 2017
    df.loc[df['Order Date'].between('2017-12-01', '2017-12-31') ]

    return


@app.cell
def _(df):
    df['profit_ratio'] = df['Profit'] / df['Sales']
    return


@app.cell
def _(df):
    ## 'Segment' and 'Region' combination have highest sales
    rs_max_sales = df.groupby(['Segment', 'Region'])['Sales'].sum().sort_values(ascending=False).head(1)
    rs_max_sales
    return


@app.cell
def _(df):
    df.groupby('Product ID').agg(avg_profit=('Profit', 'mean'))
    return


@app.cell
def _(df):
    ##Identify products with high sales but low profit
    highest_sales_threshold = df['Sales'].quantile(0.75) ### top 25% of the sales
    lowest_profit_threshold = df['Profit'].quantile(0.25) #### below 25% of profit
    high_sales_low_profit = df[(df['Sales'] >= highest_sales_threshold) & (df['Profit'] <= lowest_profit_threshold)]
    high_sales_low_profit[['Product Name', 'Sales', 'Profit']]
    return


@app.cell
def _(df, pd):
    monthly_sales = df.groupby(pd.Grouper(key='Order Date', freq='ME'))['Sales'].sum().reset_index()
    return (monthly_sales,)


@app.cell
def _(monthly_sales):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales['Order Date'], monthly_sales['Sales'], marker='o', linestyle='-')
    plt.title('Monthly Sales Trend')
    plt.xlabel("Months")
    plt.ylabel('Total Sales')
    plt.grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return (plt,)


@app.cell
def _(df, plt):
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Sales'])
    plt.title('Sales by category')
    plt.xlabel('Product Categories')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='-', alpha=0.7)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
