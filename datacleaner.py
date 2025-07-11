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
    summary = {
        'total_trips': len(data),
        'average_fare': data['fare_amount'].mean(),
        'max_fare': data['fare_amount'].max(),
        'average_trip_distance': data['trip_distance'].mean(),
        'total_trip_distance': data['trip_distance'].sum(),
        'payment_type_counts': data['payment_type'].value_counts().to_dict(),
        'average_trip_duration_minutes': (
                    (data['dropoff_datetime'] - data['pickup_datetime']).dt.total_seconds() / 60).mean()
    }
    return summary


def main():
    path = "nyc_taxi_sample_100.json"
    data = read_data_from_path(input_path=path)
    cleaned_data = cleaning_data(data)
    final_data = summarize_data(cleaned_data)
    for key, value in final_data.items():
        new_format_key = str(key).replace('_', ' ')
        new_format_value = float(f"{value:2f}") if isinstance(value, float) else value
        print(f"{new_format_key}: {new_format_value}")


if __name__ == "__main__":
    main()
