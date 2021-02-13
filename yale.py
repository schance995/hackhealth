import requests
from bs4 import BeautifulSoup
import pandas as pd

r_SWL = requests.get("https://covid19.yale.edu/yale-statistics/yale-covid-19-statistics-data-tables#yale-new-cases-data")

root_SWL = BeautifulSoup(r_SWL.content)

table_SWL = pd.read_html(root_SWL.find("table").prettify())

print(table_SWL)
