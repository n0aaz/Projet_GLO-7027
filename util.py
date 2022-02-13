def get_column_names():
    """
    Returns a list of column names
    """
    return df.columns.tolist()


def get_column_value_counts(column_name):
    """
    Returns a df with the value counts of a column
    """
    return df[column_name].value_counts()


def plot_column_values(column_name):
    """
    Plots a column values
    """
    df[column_name].value_counts().plot(kind='bar')
    plt.title(f"Distribution des réponses de la question {column_name}")
    plt.show()


def get_unique_values_per_column(min_unique_threshold=None, max_unique_threshold=None):
    """
    Returns a list of unique values per column with optional minimum threshold
    """
    unique_values = df.nunique()

    if min_unique_threshold:
        unique_values = unique_values[unique_values > min_unique_threshold]
    elif max_unique_threshold:
        unique_values = unique_values[unique_values < max_unique_threshold]

    return unique_values


def get_columns_per_value_keyword(keyword):
    """
    Returns a list of columns with a value containing the keyword
    """
    return df.columns[df.apply(lambda x: keyword in x.values, axis=0)].tolist()


def get_samples_per_column(N=5):
    """
    Returns a sample of non-NaN answers per column if they exist
    """
    samples_per_column = {}
    for column in df.columns:
        non_nan_values = df[column][~df[column].isna()]

        if len(non_nan_values) > N:
            samples_per_column[column] = non_nan_values.sample(N).tolist()

    return samples_per_column


def get_not_na_bool_answers(df, question_of_interest):
    """
    Returns a boolean array of the answers to the question of interest
    """
    return df[question_of_interest].notna()
