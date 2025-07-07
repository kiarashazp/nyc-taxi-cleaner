# Project Title: Clean & Analyze NYC Taxi Trip Data

## Context:
This application is a CLI tool that receives, cleans, and summarizes raw taxi trip data stored in CSV and JSON formats.

Rows with the following common problems are simulated
• Missing values (null, empty strings)
• Inconsistent data (e.g. payment_type as "credit card", "Credit Card", "CREDIT CARD")
• Invalid inputs (e.g. negative trip_distance or fare_amount)

## Get output:
$ python datacleaner.py --input nyc_taxi_sample.csv --summary

## Sample statistics:
Total rows: 5
Valid rows after cleaning: 3
Numeric columns:
- trip_distance: mean=4.3, min=3.5, max=5.2
- Fare amount: mean=15.2, min=12.5, max=18.0
Category columns:
- Payment type:
- Credit card: 2
- Cash: 1