The dataset contains the details of the COVID-19 vaccination of 61 countries from 2020-2021.The data was
collected from the Kaggle. There were 13 variables in the original dataset and 5750 observations. The data has the
vaccination count and also the rate of vaccination per population of the country. As a part of cleaning and for analysis
purpose I added 3 additional variables to the dataset. Finally, it had 16 variables and 5750 observations. The data is based
on daily vaccinations on different dates in the time period 2020 – 2021. The details of fully vaccinated people and total
vaccinations and the type vaccines used in each country are available in the dataset.

country - Nominal Categorical -  The country in which vaccination is given

iso_code - Nominal Categorical -  ISO_CODE of the country

date -  The date in which the  vaccinations are given.( All the dates are not included in the dataset)

total_vaccinations -  Discrete Numerical -  The total number of vaccinations given in the country

people_vaccinated - Discrete Numerical - Number of people vaccinated. It can be either single or both doses.

people_fully_vaccinated -  Discrete Numerical - Number of people who have received both doses of vaccines.

daily_vaccinations - Discrete Numerical - It is the number of vaccinations given on that date in a country.

total_vaccinations_per_hundred - Continuous Numerical - It is the ratio between the total number of vaccinations and the total population in that country.

people_vaccinated_per_hundred - Continuous Numerical - It is the ratio between the population immunized and the total population in that country.

people_fully_vaccinated_per_hundred - Continuous Numerical - It is the ratio between the population fully immunized and the total population in that country.

daily_vaccinations_per_million - Continuous Numerical - It is the ratio between the vaccination number and the total population in that country.

source_name - Nominal Categorical - The source name where this information is available.

year-  Discrete Numerical - The year in which the vaccination given

month - Ordinal Categorical - Month in which the vaccination is given

continent -  Nominal Categorical - The continent in which the country is in.

vaccines - Nominal Categorical - Name of the vaccines used in that country

