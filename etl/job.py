from etl.extract import extract
from etl.transform import transform
from etl.load import load


def run():
    print("Running Exoplanet ETL...")

    extract("data/planets.csv")
    transform()
    load()
