# From Standard Lib
from csv import DictReader
from typing import Dict, List

# From External Lib
from orjson import dumps, OPT_INDENT_2
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    african_american_male: List = list()
    year: List = list()
    african_american_male_age: List = list()

    # Open and read the CSV from disk.
    # Download this dataset here: https://catalog.data.gov/dataset/nchs-death-rates-and-life-expectancy-at-birth
    with open('NCHS_-_Death_rates_and_life_expectancy_at_birth.csv') as csvfile:
        death_rate_csv: DictReader[str] = DictReader(csvfile)
        
        # Iterate over the death rate CSV.
        for row in  death_rate_csv:
            # Look for "Race" being "Black" and "Sex" being "Male"
            # Append these values to the african_american_male array.
            if (row["Race"] == "Black") and (row["Sex"] == "Male"):
                african_american_male.append(row)
                african_american_male_age.append(row["Average Life Expectancy (Years)"])
                year.append(row["Year"])
    
    # converts list of dicts to json string
    json: bytes = dumps(african_american_male, option=OPT_INDENT_2)

    # Decode the bytes and print.
    print(json.decode())
    # plot
    fig, ax = plt.subplots()
    ax.plot(year, african_american_male_age)
    plt.show()
    



if __name__ == '__main__':
    main()