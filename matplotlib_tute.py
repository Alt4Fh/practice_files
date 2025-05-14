import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
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


@app.cell
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


@app.cell
def _(plt):
    import numpy as np
    price_changes = np.random.normal(loc=0, scale=1, size=100)

    plt.hist(price_changes, bins=30, color='green', edgecolor='red')
    plt.title('Stock Price Change Distribution')
    plt.xlabel('Change')
    plt.ylabel('Frequency')
    plt.show()

    return


@app.cell
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


@app.cell
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


@app.cell
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


@app.cell
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


@app.cell
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


if __name__ == "__main__":
    app.run()
