import os
def clean_directory():
    for year in range(1950,2023):
        os.remove(f"./doc_{year}.html")
    print("CLEANED")