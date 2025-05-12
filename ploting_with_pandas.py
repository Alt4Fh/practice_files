import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return np, pd, plt


@app.cell
def _(pd):
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Product_A': [100, 150, 200, 250, 300],
        'Product_B': [80, 120, 160, 200, 240]
    }

    df = pd.DataFrame(data)

    return (df,)


@app.cell
def _(df, plt):
    #Line plots are ideal for visualizing trends over time.
    df.plot(x='Year', y=['Product_A', 'Product_B'], kind='line', marker='o')
    plt.title('Line Plot')
    plt.show()
    return


@app.cell
def _(df, plt):
    #2. Bar Plot
    #Bar plots are useful for comparing quantities across different categories.

    df.set_index('Year')[['Product_A', 'Product_B']].plot(kind='bar')
    plt.title('Anual sales compation')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks(rotation=0)
    plt.show()
    return


@app.cell
def _(np):
    ##3. Histogram
    ## Histograms are great for understanding the distribution of a dataset.
    ##

    # simulate sales data

    np.random.default_rng(seed=42)

    sales_data = np.random.normal(200, 50, 1000)
    return (sales_data,)


@app.cell
def _(pd, sales_data):
    sales_df = pd.DataFrame({'sales_data': sales_data})
    return (sales_df,)


@app.cell
def _(sales_df):
    sales_df.plot(kind='hist', bins=30, edgecolor='black', alpha=0.7)
    return


@app.cell
def _(df, plt):
    ### 4. Box Plot
    ### Box plots provide a summary of a dataset's distribution, highlighting the median, quartiles, and potential outliers.

    df[['Product_A', 'Product_B']].plot(kind='box')
    plt.title("Sales distribution by product")
    plt.ylabel('Sales')
    plt.show()
    return


@app.cell
def _(np, pd, plt):
    #### box plot examples

    np.random.default_rng(seed=0)
    ages = np.random.normal(35, 10, 1000)
    ages_df = pd.DataFrame({'ages': ages})

    ages_df.plot(kind='hist', bins=20, edgecolor="red", alpha=0.7)
    plt.xlabel('Age')
    plt.ylabel('frequency')
    plt.title('Customer Age Distribution')

    return


@app.cell
def _(pd):
    ### pi chart portions of category within a whole 
    ## when you have fewer categories and wants to visualize the percentage 

    market_share = {'product_a': 30, 'product_b': 45, 'product_c': 25}
    market_share_df = pd.Series(market_share)
    market_share_df.plot(kind='pie', autopct="%1.1f%%", figsize=(6,6))
    return


@app.cell
def _(np, pd):
    # Scatter plot 
    # used to examine the relationship between two continuous variable. it show how one variable is affecting another

    np.random.default_rng(seed=42)
    ad_spend = np.random.uniform(5000, 50000, 100)
    sales = ad_spend * 0.05 + np.random.normal(500, 2000, 100)

    scatter_df = pd.DataFrame({'ads_spend': ad_spend, 'sales': sales})

    scatter_df.plot(kind='scatter', x='ads_spend', y='sales', alpha=0.7)
    return


@app.cell
def _(np, pd):
    #7. Heatmap
    #A heatmap is used to show the intensity of values in a matrix form. It’s useful for visualizing correlation matrices or any kind of 2D #data.

    import seaborn as sns

    # Simulating product sales data
    df_sales = pd.DataFrame({
        'Product_A': np.random.randint(100, 500, 50),
        'Product_B': np.random.randint(200, 600, 50),
        'Product_C': np.random.randint(150, 450, 50)
    })


    # correlation matrix
    # The correlation coefficient ranges from -1 to 1:

    #     1 means perfect positive correlation (as one value increases, the other increases in perfect sync).

    #    -1 means perfect negative correlation (as one value increases, the other decreases in perfect sync).

    #     0 means no correlation (no linear relationship between the variables).




    corr_matrix = df_sales.corr()

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.05)
    return (sns,)


@app.cell
def _(np, pd, sns):
    product_data = {
        'Product_A': np.random.normal(50000, 5000, 200),
        'Product_B': np.random.normal(55000, 7000, 200)
    }

    df_product = pd.DataFrame(data=product_data)
    sns.violinplot(data=df_product)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
