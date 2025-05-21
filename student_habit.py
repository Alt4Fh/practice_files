import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    import seaborn as sns

    df = pd.read_csv('student_habits_performance.csv')
    return df, matplotlib, np, pd, plt, sns


@app.cell
def _(df):
    df.shape
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
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.drop(columns='student_id', inplace=True)
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(10,6))
    plt.title('outliers'.upper())
    sns.boxenplot(x='parental_education_level', y='exam_score', data=df, hue='gender')
    plt.legend(bbox_to_anchor = (1,1))
    return


@app.cell
def _(df, matplotlib, plt, sns):
    def _():
        matplotlib.rcParams.update({'font.size': 20})

        fig, axes = plt.subplots(5,2, figsize=(16,16))
        plt.subplots_adjust(wspace=0.2, hspace=0.5)
        names = list(df.columns)
        for i, ax in enumerate(iterable=axes.flatten()):
            sns.histplot(ax=ax, data=df[names[i]], kde=True, bins=20)
            ax.set_ylabel('')
        fig.suptitle('Outliers')
        return plt.show()


    _()
    return


@app.cell
def _(df, plt, sns):
    #### heat map

    plt.figure(figsize=(10,8))
    sns.set_context(context='poster', font_scale=0.3)
    sns.heatmap(data=df.select_dtypes(include=['number']).corr().round(2), cmap='vlag', annot=True, vmin=-1, vmax=1)
    return


@app.cell
def _(df, np):
    ## removing rdundent upper part

    matrix = df.select_dtypes(include=['number']).corr().round(2)
    ## 1 make a mask 

    mask = np.triu(np.ones_like(matrix, dtype=bool))
    return mask, matrix


@app.cell
def _(mask):
    mask
    return


@app.cell
def _(mask, matrix, sns):
    sns.heatmap(data=matrix, cmap='vlag', annot=True, vmin=-1, vmax=1, mask=mask)
    return


@app.cell
def _():
    ## linear regression

    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import GridSearchCV, train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    return (
        LinearRegression,
        StandardScaler,
        mean_squared_error,
        r2_score,
        train_test_split,
    )


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell
def _(df):
    ### fill missing values of 'parental_education_level'

    df['parental_education_level'] = df['parental_education_level'].fillna(df['parental_education_level'].mode()[0])
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    ## select categorical columns

    cat_col = list(df.select_dtypes(include='object').columns)

    cat_col
    return (cat_col,)


@app.cell
def _(cat_col, df, plt, sns):
    ## histogram for cat colums


    fig, axes = plt.subplots(len(cat_col)//2, 2, figsize=(16, 16))
    fig.subplots_adjust(hspace=0.5, wspace=0.3)

    for i, ax, in enumerate(iterable=axes.flatten()):
        sns.histplot(df[cat_col[i]], ax=ax, bins=5, binwidth=0.1, kde=True, edgecolor='black')
        plt.title(f'Distribution of {cat_col[i]}')
        ax.set_ylabel('')
        ax.grid()
    plt.tight_layout()
    plt.show()
        # 
    return


@app.cell
def _(df):
    num_col = list(df.select_dtypes(include='number'))
    num_col
    return (num_col,)


@app.cell
def _(df, num_col, plt, sns):
    def _():
        ### histogram for numerical colums

        fig, axes = plt.subplots(len(num_col)//2, 2, figsize=(16,16))
        fig.subplots_adjust(hspace=0.5, wspace=0.2)
        for i, ax in enumerate(iterable=axes.flatten()):
            sns.histplot(ax=ax, data=df[num_col[i]], bins=20)
            ax.set_title(f'Distribution of {num_col[i]}')
            sns.set(font_scale=1.5)
            ax.set_ylabel('')
            ax.set_xlabel('')


        plt.show()
    _()
    return


@app.cell
def _(cat_col):
    cat_col
    return


@app.cell
def _(num_col):
    num_col
    return


@app.cell
def _(cat_col, df):
    ## converting cat columns to categorical type

    df[cat_col] = df[cat_col].astype(dtype='category')

    return


@app.cell
def _(df):
    ## label encoding diet_quality, "parental_education_level", internet_quality
    df['dq_e'] = df['diet_quality'].cat.codes
    df['pel_e'] = df["parental_education_level"].cat.codes
    df['iq_e'] = df['internet_quality'].cat.codes
    return


@app.cell
def _(df, pd):
    dummies = pd.get_dummies(df[["gender", "part_time_job", "extracurricular_participation"]], drop_first=True)
    dummies.head()
    return (dummies,)


@app.cell
def _(df, dummies, pd):
    df2 = pd.concat([df, dummies], axis=1)
    return (df2,)


@app.cell
def _(df2):
    df2.head()
    return


@app.cell
def _(df2, np, plt, sns):
    def _():
        corr = df2.select_dtypes(include=['number', 'bool']).corr().round(2)
        mask = np.triu(np.ones_like(corr))
        plt.figure(figsize=(16,16))
        sns.heatmap(corr, annot=True, vmin=-1, vmax=1, mask=mask)
        sns.set(font_scale=0.5)
        return plt.show()


    _()
    return


@app.cell
def _(df2):
    df2.head()
    return


@app.cell
def _(df2):
    df2.drop('study_hours_per_day', axis=1, inplace=True)
    return


@app.cell
def _(df2):
    df2.drop(['gender',
              'part_time_job',
              'diet_quality',
              'parental_education_level',
              'internet_quality',
              'extracurricular_participation'], axis=1, inplace=True)
    return


@app.cell
def _(df2):
    X = df2.drop('exam_score', axis=1)
    Y = df2['exam_score']

    X.shape, Y.shape
    return X, Y


@app.cell
def _(
    LinearRegression,
    StandardScaler,
    X,
    Y,
    mean_squared_error,
    r2_score,
    train_test_split,
):
    from sklearn.linear_model import  Ridge, Lasso
    from sklearn.ensemble import RandomForestRegressor


    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled.shape


    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    X_train, X_test, Y_train, Y_test


    lr_model = LinearRegression()
    lr_model.fit(X_train, Y_train)
    lr_model.score(X_test, Y_test)




    models = {
        "Linear": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.1),
        "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
    }


    for name, model in models.items():
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        print(f"{name} → R²: {r2_score(Y_test, Y_pred):.3f}, RMSE: {mean_squared_error(Y_test, Y_pred):.2f}")
    
    return


if __name__ == "__main__":
    app.run()
