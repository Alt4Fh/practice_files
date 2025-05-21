import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Part 2: Full Data Workflow A-Z""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Cleaning Data""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### First Inspection / Handling inconsistent Data""")
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(pd):
    titanic = pd.read_csv("./Course_Materials_ALL/Course_Materials_Part2/Video_Lecture_NBs/titanic.csv")
    return (titanic,)


@app.cell
def _(titanic):
    titanic.reset_index()
    return


@app.cell
def _(titanic):
    titanic.tail()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.describe()
    return


@app.cell
def _(titanic):
    titanic.describe(include ="O")
    return


@app.cell
def _(titanic):
    titanic.survived.unique()
    return


@app.cell
def _(titanic):
    titanic.survived.value_counts()
    return


@app.cell
def _(titanic):
    titanic["survived"] = titanic["survived"].replace(to_replace= ["yes", "no"], value = [1, 0]) # new (Pandas 3.x)
    return


@app.cell
def _(titanic):
    titanic.survived.value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(pd):
    summer = pd.read_csv("./Course_Materials_ALL/Course_Materials_Part2/Video_Lecture_NBs/summer_imp.csv")
    return (summer,)


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer.tail()
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell
def _():
    #summer.Athlete_Name
    return


@app.cell
def _(summer):
    summer.rename(columns = {"Athlete Name": "Athlete_Name"}, inplace = True)
    return


@app.cell
def _(summer):
    summer.head(20)
    return


@app.cell
def _(summer):
    summer.Medal.value_counts()
    return


@app.cell
def _():
    # summer.Medal.replace(to_replace= "Gold Medal", value = "Gold", inplace = True) # old
    return


@app.cell
def _(summer):
    summer["Medal"] = summer["Medal"].replace(to_replace= "Gold Medal", value = "Gold") # new (Pandas 3.x)
    return


@app.cell
def _(summer):
    summer.describe(include = "O")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### String Operations""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _():
    #pd.to_numeric(titanic.Fare)
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(summer):
    summer.head(20)
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell
def _(summer):
    summer.Athlete_Name = summer.Athlete_Name.str.title()
    return


@app.cell
def _(summer):
    summer.head(10)
    return


@app.cell
def _(summer):
    summer.loc[summer.Athlete_Name.str.contains("Hajos")]
    return


@app.cell
def _(summer):
    summer.iloc[0, 4]
    return


@app.cell
def _(summer):
    summer.Athlete_Name = summer.Athlete_Name.str.strip()
    return


@app.cell
def _(summer):
    summer.loc[summer.Athlete_Name == "Hajos, Alfred"]
    return


@app.cell
def _(summer):
    summer.loc[summer.Athlete_Name == "Phelps, Michael"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Changing DataType with astype() / pd.to_numeric""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic["fare"] = titanic.fare.astype("float")
    return


@app.cell
def _(titanic):
    titanic["survived"] = titanic.survived.astype("int")
    return


@app.cell
def _():
    #titanic["Age"] = titanic.Age.astype("float")
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Intro to NA Values""")
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(pd):
    sales = pd.read_csv("./Course_Materials_ALL/Course_Materials_Part2/Video_Lecture_NBs/sales.csv", index_col = 0)
    return (sales,)


@app.cell
def _(sales):
    sales
    return


@app.cell
def _(sales):
    sales.info()
    return


@app.cell
def _(sales):
    sales.loc["Steven", "Thu"]
    return


@app.cell
def _(sales):
    sales.iloc[1,1] = None
    return


@app.cell
def _(sales):
    sales
    return


@app.cell
def _(np, sales):
    sales.iloc[2,2] = np.nan
    return


@app.cell
def _(sales):
    sales
    return


@app.cell
def _(sales):
    sales.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head(10)
    return


@app.cell
def _(titanic):
    titanic.tail(10)
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.isna()
    return


@app.cell
def _(titanic):
    titanic.isna().sum(axis = 0)
    return


@app.cell
def _(titanic):
    titanic.isna().any(axis = 1)
    return


@app.cell
def _(titanic):
    titanic[titanic.isna().any(axis = 1)]
    return


@app.cell
def _(titanic):
    titanic.notna()
    return


@app.cell
def _(titanic):
    titanic.notna().sum(axis = 1)
    return


@app.cell
def _(titanic):
    titanic.notna().all(axis = 0)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import seaborn as sns
    return plt, sns


@app.cell
def _(plt, sns, titanic):
    plt.figure(figsize = (12,8))
    sns.heatmap(titanic.notna())
    plt.show()
    return


@app.cell
def _(titanic):
    titanic.age.value_counts(dropna = False)
    return


@app.cell
def _():
    # titanic.Age.replace(to_replace= "Missing Data", value = np.nan, inplace= True) # old
    return


@app.cell
def _(np, titanic):
    titanic["age"] = titanic["age"].replace(to_replace= "Missing Data", value = np.nan) # NEW (Pandas 3.x)
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.age = titanic.age.astype("float")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell
def _(summer):
    summer[summer.isna().any(axis = 1)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Removing Missing Values with dropna()""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic[titanic.embarked.isna()]
    return


@app.cell
def _(titanic):
    titanic.age.value_counts(dropna = False)
    return


@app.cell
def _(titanic):
    titanic.age.mean(skipna = True)
    return


@app.cell
def _(titanic):
    titanic.shape
    return


@app.cell
def _(titanic):
    titanic.dropna().shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 0, how = "any").shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 1, how = "any").shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 0, how = "all").shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 1, how = "all").shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 0, thresh = 8).shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 1, thresh = 500).shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 1, thresh = 500, inplace = True)
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.shape
    return


@app.cell
def _(titanic):
    titanic.dropna(axis = 0, subset = ["survived", "pclass",  "age"], how = "any").shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell
def _(summer):
    summer[summer.isna().any(axis = 1)]
    return


@app.cell
def _(summer):
    summer.dropna(inplace = True)
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Replacing Missing Values with fillna()""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head(10)
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.age.mean()
    return


@app.cell
def _(titanic):
    mean = round(titanic.age.mean(),1)
    mean
    return (mean,)


@app.cell
def _():
    # titanic.Age.fillna(mean, inplace = True) # old
    return


@app.cell
def _(mean, titanic):
    titanic["age"] = titanic["age"].fillna(mean) # NEW (Pandas 3.0)
    return


@app.cell
def _(titanic):
    titanic.head(6)
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Detection of Duplicates""")
    return


@app.cell
def _(pd):
    alphabet = pd.DataFrame(["a", "b", "c", "c", "d", "e", "f", "g", "g", "g"], columns = ["Alphabet"])
    return (alphabet,)


@app.cell
def _(alphabet):
    alphabet
    return


@app.cell
def _(alphabet):
    alphabet.duplicated(keep = "first")
    return


@app.cell
def _(alphabet):
    alphabet[alphabet.duplicated(keep = "first")]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.duplicated(keep = "first", subset = ["survived", "pclass"]).sum()
    return


@app.cell
def _(titanic):
    titanic[titanic.duplicated(keep = False)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olypmic Dataset""")
    return


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell
def _(summer):
    summer.duplicated(keep = "first").sum()
    return


@app.cell
def _(summer):
    summer[summer.duplicated(keep = False)]
    return


@app.cell
def _(summer):
    summer.loc[(summer.Sport == "Basketball") & (summer.Year == 2012)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Handling / Removing Duplicates""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.tail()
    return


@app.cell
def _(titanic):
    titanic.duplicated().sum()
    return


@app.cell
def _(titanic):
    titanic[titanic.duplicated()]
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.tail()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer[summer.duplicated(keep = False)]
    return


@app.cell
def _(summer):
    summer.drop(index = [2069, 12253, 15596, 21833, 28678], inplace = True)
    return


@app.cell
def _(summer):
    summer[summer.duplicated(keep = False)]
    return


@app.cell
def _(summer):
    summer.loc[16085:16110]
    return


@app.cell
def _(summer):
    summer.loc[29780:29795]
    return


@app.cell
def _(alphabet):
    alphabet[alphabet.duplicated(keep = False)]
    return


@app.cell
def _(alphabet):
    alphabet.drop_duplicates(inplace = True)
    return


@app.cell
def _(alphabet):
    alphabet
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### The ignore_index parameter (NEW in Pandas 1.0)""")
    return


@app.cell
def _(pd):
    alphabet_1 = pd.DataFrame(['a', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'g', 'g'], columns=['Alphabet'])
    return (alphabet_1,)


@app.cell
def _(alphabet_1):
    alphabet_1
    return


@app.cell
def _(alphabet_1):
    alphabet_1.drop_duplicates(ignore_index=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Detection of Outliers""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.describe()
    return


@app.cell
def _(plt, titanic):
    plt.figure(figsize = (12,6))
    titanic.boxplot("age")
    plt.show()
    return


@app.cell
def _(plt, titanic):
    plt.figure(figsize = (12,6))
    titanic.age.plot()
    plt.show()
    return


@app.cell
def _(titanic):
    titanic.age.sort_values(ascending = False)
    return


@app.cell
def _(titanic):
    titanic.loc[titanic.age > 70]
    return


@app.cell
def _(titanic):
    titanic.fare.sort_values(ascending = False)
    return


@app.cell
def _(plt, titanic):
    plt.figure(figsize = (12,6))
    titanic.fare.plot()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Handling / Removing Outliers""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.loc[titanic.age > 79]
    return


@app.cell
def _(titanic):
    index_outl  = titanic.loc[titanic.age > 79].index
    return (index_outl,)


@app.cell
def _(index_outl):
    index_outl
    return


@app.cell
def _(titanic):
    titanic.loc[titanic.Age > 79, "age"] = titanic.loc[titanic.age > 79, "age"]/10
    return


@app.cell
def _(index_outl, titanic):
    titanic.loc[index_outl]
    return


@app.cell
def _(titanic):
    titanic.loc[217, "Age"] = 42.0
    return


@app.cell
def _(plt, titanic):
    plt.figure(figsize = (12,6))
    titanic.age.plot()
    plt.show()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Categorical Data""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Titanic Dataset""")
    return


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _():
    #titanic.to_csv("titanic_clean.csv", index = False)
    return


@app.cell
def _(titanic):
    titanic.nunique()
    return


@app.cell
def _(titanic):
    titanic[["sex", "embarked"]].describe()
    return


@app.cell
def _(titanic):
    titanic.Gender = titanic.Gender.astype("category")
    return


@app.cell
def _(titanic):
    titanic.Emb = titanic.Emb.astype("category")
    return


@app.cell
def _(titanic):
    titanic.info()
    return


@app.cell
def _(titanic):
    titanic.Gender.dtype
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Olympic Dataset""")
    return


@app.cell
def _(summer):
    summer.head()
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell
def _():
    #summer.to_csv("summer_clean.csv", index = False)
    return


@app.cell
def _(summer):
    summer.describe(include = ["O"])
    return


@app.cell
def _(summer):
    summer.nunique()
    return


@app.cell
def _(summer):
    summer.City = summer.City.astype("category")
    return


@app.cell
def _(summer):
    summer.Sport = summer.Sport.astype("category")
    return


@app.cell
def _(summer):
    summer.Discipline = summer.Discipline.astype("category")
    return


@app.cell
def _(summer):
    summer.Country = summer.Country.astype("category")
    return


@app.cell
def _(summer):
    summer.Gender = summer.Gender.astype("category")
    return


@app.cell
def _(summer):
    summer.Medal = summer.Medal.astype("category")
    return


@app.cell
def _(summer):
    summer.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Pandas Version 1.0: NEW Dtypes and pd.NA""")
    return


@app.cell
def _(pd):
    titanic_1 = pd.read_csv('./Course_Materials_ALL/Course_Materials_Part2/Video_Lecture_NBs/titanic.csv')
    return (titanic_1,)


@app.cell
def _(titanic_1):
    titanic_1
    return


@app.cell
def _(titanic_1):
    titanic_1.info()
    return


@app.cell
def _(titanic_1):
    titanic_2 = titanic_1.convert_dtypes()
    return (titanic_2,)


@app.cell
def _(titanic_2):
    titanic_2
    return


@app.cell
def _(titanic_2):
    titanic_2.info()
    return


@app.cell
def _(titanic_2):
    titanic_2.iloc[0, -1]
    return


@app.cell
def _(titanic_2):
    type(titanic_2.iloc[0, -1])
    return


@app.cell
def _(pd):
    pd.NA
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
