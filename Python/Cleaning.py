
import pandas as pd
import os
os.chdir("E:\Ginu_StudyMaterials\Sem2\Dissertation")
property_prices = pd.read_csv("PPR-ALL.csv.csv", na_values =("N/A", "NA", "--", " "))
property_prices