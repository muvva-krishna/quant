import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading all the Excel data for all the companies into DataFrames
Adanient_data = pd.read_csv("./database/ADANIENT.NS.csv")
Axisbank_data = pd.read_csv("./database/AXISBANK.NS.csv")
airtel_data = pd.read_csv("./database/BHARTIARTL.NS.csv")
Cipla_data = pd.read_csv("./database/CIPLA.NS.csv")
hinduuniliver_data = pd.read_csv("./database/HINDUNILVR.NS.csv")
infosys_data = pd.read_csv("./database/INFY.NS.csv")
itc_data = pd.read_csv("./database/ITC.NS.csv")
maruti_data = pd.read_csv("./database/MARUTI.NS.csv")
sbi_data = pd.read_csv("./database/SBIN.NS.csv")
sunpharma_data = pd.read_csv("./database/SUNPHARMA.NS.csv")
tatasteel_data = pd.read_csv("./database/TATASTEEL.NS.csv")
wipro_data = pd.read_csv("./database/WIPRO.NS.csv")
hindalco_data = pd.read_csv("./database/HINDALCO.NS.csv")

# Calculating the stochastic oscillator for all the companies

def stochastic_kvalue(data):
    data['lowest'] = data['Low'].rolling(14).min()
    data['highest'] = data['High'].rolling(14).max()
    data['%K'] = ((data['Close'] - data['lowest']) / (data['highest'] - data['lowest']))* 100
    # calculating %D
    data['%D'] = data['%K'].rolling(3).mean() 

stochastic_kvalue(Adanient_data)
stochastic_kvalue(Axisbank_data)
stochastic_kvalue(airtel_data)
stochastic_kvalue(Cipla_data)
stochastic_kvalue(hinduuniliver_data)
stochastic_kvalue(infosys_data)
stochastic_kvalue(itc_data)
stochastic_kvalue(maruti_data)
stochastic_kvalue(sbi_data)
stochastic_kvalue(sunpharma_data)
stochastic_kvalue(tatasteel_data)
stochastic_kvalue(wipro_data)
stochastic_kvalue(hindalco_data)

def meanof_K(data, company_name):
    mean_value = data['%K'].mean()
    print(f'Mean of {company_name}: {mean_value}')
meanof_K(Adanient_data, 'Adani Enterprises')
meanof_K(Axisbank_data, 'Axis Bank')
meanof_K(airtel_data, 'Bharti Airtel')
meanof_K(Cipla_data, 'Cipla')
meanof_K(hinduuniliver_data, 'Hindustan Unilever')
meanof_K(infosys_data, 'Infosys')
meanof_K(itc_data, 'ITC')
meanof_K(maruti_data, 'Maruti Suzuki')
meanof_K(sbi_data, 'State Bank of India')
meanof_K(sunpharma_data, 'Sun Pharma')
meanof_K(tatasteel_data, 'Tata Steel')
meanof_K(wipro_data, 'Wipro')
meanof_K(hindalco_data, 'Hindalco Industries')

# companies in descending order based on the largest maran value of k
sorted_companies = sorted(company_name ,key=lambda x: x[1],reverse=True)

# Extracting the sorted companies
sorted_company = [company[0] for company in sorted_companies]

print("Companies in Descending Order of largest mean value of k")
i=1
for company_name in sorted_company:
    print(f'{i}. {company_name}')
    i+=1
