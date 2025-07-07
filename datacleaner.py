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
    data = data.dropna(subset=['passenger_count'])
    data = data[0 <= data['fare_amount']]
    data = data[0 <= data['trip_distance']]
    data['payment_type'] = data["payment_type"].apply(lambda x: str(x).lower())
    data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
    data['dropoff_datetime'] = pd.to_datetime(data['dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")
    return data


def summarize_data(data):
    return data


def main():
    path = "nyc_taxi_sample_100.json"
    data = read_data_from_path(input_path=path)
    cleaned_data = cleaning_data(data)
    final_data = summarize_data(cleaned_data)
    print(final_data)


# in_path = "nyc_taxi_sample_100.json"
# datas = read_data_from_path(input_path=in_path)
# clean = cleaning_data(datas)
# dff = clean.iterrows()
# for index, row in dff:
#     print(row['pickup_datetime'])
#     print(type(row['pickup_datetime']))
#

