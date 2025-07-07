import pandas as pd


def read_data_from_path(input_path):
    if input_path.endswith('.csv'):
        df = pd.read_csv(input_path)
    elif input_path.endswith('.json'):
        df = pd.read_json(input_path)
    else:
        raise ValueError("please send correct path")
    return df


def cleaning_data(data):
    return data


def summarize_data(data):
    return data


def main():
    path = "nyc_taxi_sample_100.json"
    data = read_data_from_path(input_path=path)
    cleaned_data = cleaning_data(data)
    final_data = summarize_data(cleaned_data)
    print(final_data)
