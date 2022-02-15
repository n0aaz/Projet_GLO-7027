import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_column_names(df):
    """
    Returns a list of column names
    """
    return df.columns.tolist()


def get_column_value_counts(df, column_name):
    """
    Returns a df with the value counts of a column
    """
    return df[column_name].value_counts()


def plot_column_values(df, column_name):
    """
    Plots a column values
    """
    df[column_name].value_counts().plot(kind='bar')
    plt.title(f"Distribution des réponses de la question {column_name}")
    plt.show()


def get_column_unique_answers(df, column_name):
    """
    Returns a list of unique answers to the column
    """
    return df[column_name].unique().tolist()


def get_unique_values_per_column(df, min_unique_threshold=None, max_unique_threshold=None):
    """
    Returns a list of unique values per column with optional minimum threshold
    """
    unique_values = df.nunique()

    if min_unique_threshold is not None:
        unique_values = unique_values[unique_values > min_unique_threshold]
    elif max_unique_threshold is not None:
        unique_values = unique_values[unique_values < max_unique_threshold]

    return unique_values


def get_columns_per_value_keyword(df, keyword):
    """
    Returns a list of columns with a value containing the keyword
    """
    return df.columns[df.apply(lambda x: keyword in x.values, axis=0)].tolist()


def get_samples_per_column(df, N=5):
    """
    Returns a sample of non-NaN answers per column if they exist
    """
    samples_per_column = {}
    for column in df.columns:
        non_nan_values = df[column][~df[column].isna()]

        if len(non_nan_values) > N:
            samples_per_column[column] = non_nan_values.sample(N).tolist()

    return samples_per_column


def get_normalized_ordinal_question_answers(df, answer_order_dic, question_of_interest, default_value=0.0, lower_bound=-1, upper_bound=1):
    answers = df[question_of_interest]
    unique_answers_sorted = answers.unique(
    )[answer_order_dic[question_of_interest]]
    answer_to_int = {answer: i for i,
                     answer in enumerate(unique_answers_sorted)}

    # Replace each answer with its corresponding integer
    answers_as_int = answers.map(answer_to_int)

    # Normalize the answers
    normalized_answers = normalize_answers(
        answers_as_int, lower_bound, upper_bound)

    # Replace NaN with default value
    normalized_answers = normalized_answers.fillna(default_value)

    return normalized_answers


def normalize_answers(answers, lower_bound=-1, upper_bound=1):
    # Normalize the answers between lower_bound and upper_bound
    normalized_answers = (answers - answers.min()) / (answers.max() -
                                                      answers.min()) * (upper_bound - lower_bound) + lower_bound

    return normalized_answers


def get_not_na_bool_answers(df, question_of_interest):
    """
    Returns a boolean array of the answers to the question of interest
    """
    return df[question_of_interest].notna()

def findMultipleQuestions(list,columns):
    """
    Permet de trouver toutes les questions ayant un nom partiellement présent
    dans la liste, utile pour les attributs qui s'étalent sur plusieurs colonnes
    exemple: 'pes19_taxes_' => 'pes19_taxes_1','pes19_taxes_2','pes19_taxes_3'
    """
    colList=[]
    for question in list:
        colList += [col for col in columns if question in col]  
    return colList