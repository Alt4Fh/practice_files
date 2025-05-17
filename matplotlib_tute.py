import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ##🤖  Relational Plots: These show relationships between variables.

    ###👉  sns.scatterplot()

    ###👉  sns.lineplot()

    ###👉  sns.regplot()

    ##🤖  Categorical Plots: These show comparisons across categories.

    ###👉  sns.boxplot()

    ###👉  sns.violinplot()

    ###👉  sns.barplot()

    ##🤖  Distribution Plots: These show the distribution of a variable.

    ###👉  sns.histplot()

    ###👉  sns.kdeplot()

    ##🤖  Matrix Plots: These show correlations or pairwise relationships.

    ###👉  sns.heatmap()

    ###👉  sns.pairplot()
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Line chart shows how data changes over time, or in relation to other variable
    ## shows info as series of data points connected by straight lines
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import matplotlib.pyplot as plt
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [2200, 2800, 2600, 3100, 2900]

    plt.figure(figsize=(10,4))
    plt.plot(months, sales, marker='o', linestyle='-', color='blue')
    plt.title('Sales throughout the months')
    plt.xlabel('months')
    plt.ylabel('sales')
    plt.grid(True)
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Bar chart uses rectangular bar to show the value of different categories 
    ## Each bar --- one category
    ## Height or length of the bar  =  value 

    """
    )
    return


@app.cell(hide_code=True)
def _(plt):
    tests = ['Test A', 'Test B', 'Test C', 'Test D']
    values = [0.85, 0.90, 0.78, 0.88]

    plt.figure(figsize=(10,6))
    plt.bar(tests, values)
    plt.xlabel('Chemicals')
    plt.ylabel('values')
    plt.title("lab test values comparison")
    plt.ylim(0,1)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Histogram is bar chart that shows how often somthing happen - each bar represent range of numbers
    ## We use it wanna to see distribution of data
    """
    )
    return


@app.cell(hide_code=True)
def _(plt):
    import numpy as np
    price_changes = np.random.normal(loc=0, scale=1, size=100)

    plt.hist(price_changes, bins=30, color='green', edgecolor='red')
    plt.title('Stock Price Change Distribution')
    plt.xlabel('Change')
    plt.ylabel('Frequency')


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Pie chart  - - - -  Shows the part of the whole (percentage value)""")
    return


@app.cell(hide_code=True)
def _(plt):
    continents = ['Asia', 'Africa', 'Europe', 'Americas', 'Oceania']
    population_percent = [59.5, 17.2, 9.6, 13.0, 0.7]
    colors = ['purple', 'brown', 'pink', 'cyan', 'green']

    plt.pie(
        population_percent, 
        labels=continents, 
        autopct="%1.2f%%", 
        startangle=180, 
        colors=colors,
        explode=[0,0.1,0,0,0], #"Explodes" or separates slices outward to highlight them
        shadow=True,
        labeldistance=1.1 # distance of the labels from center which is default (0,0)
    )
    plt.axis('equal') ## makes both axises equal so chart is perfectly squred
    plt.show()
    return


@app.cell(hide_code=True)
def _(plt):
    ## Temp data over time multiple lines

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    city1 = [21, 23, 22, 24, 26, 27, 25]
    city2 = [19, 20, 21, 22, 21, 23, 22]

    plt.plot(days, city1, marker='o', label='City A' )
    plt.plot(days, city2, marker='s', label='City B')
    plt.xlabel('day')
    plt.ylabel('Tempreature (c)')
    plt.title('Weekly Tempreature comparions')
    plt.legend() ## shows city a and city b label with color and marker
    plt.grid(True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(plt):
    def _():
        ### sub plots --- compare sales trends of two products side by side

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        product_a = [2100, 2400, 2300, 2500, 2700]
        product_b = [1800, 1900, 2100, 2300, 2200]


        fig, axs = plt.subplots(1, 2, figsize=(12, 5)) ## 1 row and two columns


        axs[0].plot(months, product_a, color='blue', marker='o')
        axs[0].set_title("Product A Sales")
        axs[0].set_xlabel('Month')
        axs[0].set_ylabel('sales')

        axs[1].plot(months, product_b, color='cyan', marker='s')
        axs[1].set_title("Product B Sales")
        axs[1].set_xlabel('Month')
        plt.tight_layout()
        return axs[1].set_ylabel('sales')


    _()
    return


@app.cell(hide_code=True)
def _(plt):
    def _():
        # highlight the best sales month 
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        product_a = [2100, 2400, 2300, 2500, 2700]
        plt.plot(months, product_a, marker='o')
        plt.title('Product A Sales')
        plt.annotate('Peak',
                     xy=('May', 2700),
                     xytext=('Apr', 2800),
                     arrowprops=dict(facecolor='green', shrink=0.05),
                     fontsize=12,
                     color='darkgreen')
        return plt.show()


    _()
    return


@app.cell(hide_code=True)
def _(plt):
    import mplcursors
    def _():
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        product_a = [2100, 2400, 2300, 2500, 2700]
        plt.plot(months, product_a, marker='o')
        curser = mplcursors.cursor(hover=True)
        curser.connect("add", lambda sel: sel.annotation.set_text(f"${product_a[sel.index]}"))
        plt.show()

    _()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Scatter Plot Shows the relationship or pattern between two variables""")
    return


@app.cell(hide_code=True)
def _(plt):
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 6, 7]

    plt.scatter(x, y, color='cyan')
    plt.title('Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Box plot (Box-and-Whisker)
    ## Used for showing distribution, median, and outliers
    ### Box show 50 % of middle data --- 25th percetntile to 75th percentile (Interquartile Range(IQR))
    ### line inside box ---- median
    ### The line extending from box --- whisker  --> shows range min to max
    ### data far away from other values  ----  outliers  --- usually outside of the whiskers
    """
    )
    return


@app.cell(hide_code=True)
def _(plt):
    data = [7, 15, 13, 18, 22, 24, 20, 19, 18, 30, 35, 28, 45]

    plt.boxplot(data)
    plt.title("Box Plot")
    plt.show()

    return


@app.cell
def _(mo):
    mo.md(r"""## Area Chart like line chart, but filled with colors""")
    return


@app.cell(hide_code=True)
def _(plt):
    xa = [1, 2, 3, 4, 5]
    ya = [1, 4, 2, 5, 3]

    plt.fill_between(xa, ya, color='skyblue', alpha=0.5)
    plt.plot(xa, ya)
    plt.title("Area Chart")
    plt.show()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## like bar chart but each column is devided into parts, parts represent sub-categories
    ## height total value of the category
    ##  --- parts shows how much sub categrory is contributed to total value o th category
    """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(plt):
    def _():
        # Data for sales
        months = ['January', 'February', 'March']
        apples = [50, 60, 70]
        bananas = [30, 40, 50]
        cherries = [20, 25, 30]

        # Plotting the stacked bar chart
        plt.bar(months, apples, label='Apples', color='red')
        plt.bar(months, bananas, bottom=apples, label='Bananas', color='yellow')
        plt.bar(months, cherries, bottom=[i+j for i,j in zip(apples, bananas)], label='Cherries', color='pink')

        # Adding labels and title
        plt.title('Fruit Sales Over 3 Months')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.legend()

        # Show the plot
        return plt.show()


    _()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### sns. + plot type + (parameters)
    sns.scatterplot() → scatter = data points

    sns.lineplot() → line = continuous data

    sns.histplot() → hist = histogram
    """
    )
    return


@app.cell
def _():
    import seaborn as sns
    import pandas as pd 

    df = pd.read_csv('https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv')
    return df, sns


@app.cell
def _(df):

    df.columns = df.columns.str.removesuffix('(cm)')
    df.columns = df.columns.str.strip()
    return


@app.cell
def _(df):
    df.columns = df.columns.str.replace(" ", "_")
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df, plt):
    df.hist(figsize=(15,8), bins=30)
    plt.suptitle('histogram of iris feature')
    plt.tight_layout()
    plt.show()
    return


app._unparsable_cell(
    r"""
    ## box plot for sepal length by Species--- target
    plt.figure(figsize=(8,6))
    sns.boxplot(]x='target', y='sepal_length', data=df)
    plt.title('Sepal Length by species')
    """,
    name="_"
)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df, plt, sns):
    ## boxplot for petal length by species

    plt.figure(figsize=(10,6))
    sns.boxenplot(x='target', y='petal_length', data=df)
    plt.title('Box Plot for Petal Length by species')
    return


if __name__ == "__main__":
    app.run()
