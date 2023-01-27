import pandas as pd
import os


class CarsData:
    def __init__(self, data_folder_path: str) -> None:
        self._data_folder_path = data_folder_path

    """     def Cars_dataframe() -> pd.DataFrame:
            cars_list = []
            cars_df = pd.read_csv('./carsdata/used_car_dataset.csv')
            cars_df = cars_df[['publication_datetime', 'publication_history', 'location',
        'provider', 'manufacturer', 'model', 'note', 'price_sek',
            'entry_year', 'fuel', 'mileage_km', 'transmission',
        'type_of_drive', 'horse_power', 'engine_size_ccm', 'top_speed_km_h',
        'emission_class', 'co2_emission_g/km',
        'fuel_consumption_mixed_l_100km', 'fuel_consumption_highway_l_100km',
        'electric_range_km','car_type']]
            
            cars_list.append(cars_df)
            
            return cars_list """

    def cars_dataframe(self, cars: str) -> list:
        cars_list = []

        for df_ending in ["_car_dataset.csv"]:
            path = os.path.join(self._data_folder_path, cars + df_ending)
            car_df = pd.read_csv(path)
            car_df = car_df[
                [
                    "publication_datetime",
                    "publication_history",
                    "location",
                    "provider",
                    "manufacturer",
                    "model",
                    "note",
                    "price_sek",
                    "entry_year",
                    "fuel",
                    "mileage_km",
                    "transmission",
                    "type_of_drive",
                    "horse_power",
                    "engine_size_ccm",
                    "top_speed_km_h",
                    "emission_class",
                    "co2_emission_g/km",
                    "fuel_consumption_mixed_l_100km",
                    "fuel_consumption_highway_l_100km",
                    "electric_range_km",
                    "car_type",
                ]
            ]

            cars_list.append(car_df)
            return cars_list
