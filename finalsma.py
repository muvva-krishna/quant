# Indicator : SMA  sorting out companies based on their largest SMA movements.


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

# Calculating the 50day simple moving averages for all companies (50day SMA)

Adanient_data['Adanient_SMA50'] =  Adanient_data['Close'].rolling(50).mean()
Axisbank_data['Axisbank_SMA50'] =  Axisbank_data['Close'].rolling(50).mean()
airtel_data ['airtel_SMA50']  =  airtel_data['Close'].rolling(50).mean()
Cipla_data ['Cipla_SMA50']   =  Cipla_data['Close'].rolling(50).mean()
hinduuniliver_data['hinduuniliver_SMA50'] = hinduuniliver_data['Close'].rolling(50).mean()
infosys_data['infosys_SMA50']   = infosys_data['Close'].rolling(50).mean()
itc_data['itc_SMA50']     = itc_data['Close'].rolling(50).mean()
maruti_data['maruti_SMA50']   = maruti_data['Close'].rolling(50).mean()
sbi_data['sbi_SMA50']    = sbi_data['Close'].rolling(50).mean()
sunpharma_data['sunpharma_SMA50'] = sunpharma_data['Close'].rolling(50).mean()
tatasteel_data['tatasteel_SMA50'] = tatasteel_data['Close'].rolling(50).mean()
wipro_data['wipro_SMA50']   = wipro_data['Close'].rolling(50).mean()
hindalco_data['hindalco_SMA50']  = hindalco_data['Close'].rolling(50).mean()

# Calculating the momentum of SMAs for each company

Adanient_data['Adanient_SMA50_movement'] =  Adanient_data['Close'].diff()
Axisbank_data['Axisbank_SMA50_movement'] = Axisbank_data['Close'].diff()
airtel_data ['airtel_SMA50_movement']  = airtel_data['Close'].diff()
Cipla_data ['Cipla_SMA50_movement']   =  Cipla_data['Close'].diff()
hinduuniliver_data['hinduuniliver_SMA50_movement'] = hinduuniliver_data['Close'].diff()
infosys_data['infosys_SMA50_movement'] = infosys_data['Close'].diff()
itc_data['itc_SMA50_movement']    = itc_data['Close'].diff()
maruti_data['maruti_SMA50_movement']   = maruti_data['Close'].diff()
sbi_data['sbi_SMA50_movement']    = sbi_data['Close'].diff()
sunpharma_data['sunpharma_SMA50_movement']  = sunpharma_data['Close'].diff()
tatasteel_data['tatasteel_SMA50_movement'] = tatasteel_data['Close'].diff()
wipro_data['wipro_SMA50_movement']   = wipro_data['Close'].diff()
hindalco_data['hindalco_SMA50_movement']  = hindalco_data['Close'].diff()


# For calculating the maximum movement
companies = ['adanient','axisbank','airtel','cipla','hinduuniliver','infosys','itc','maruti','sbi','sunpharma','tatasteel','wipro','hindalco']
max_movements = [ Adanient_data['Adanient_SMA50_movement'].max(),
            Axisbank_data['Axisbank_SMA50_movement'].max(),
            airtel_data ['airtel_SMA50_movement'].max(),
            Cipla_data ['Cipla_SMA50_movement'].max(),
            hinduuniliver_data['hinduuniliver_SMA50_movement'].max(),
            infosys_data['infosys_SMA50_movement'].max(),
            itc_data['itc_SMA50_movement'].max(),
            maruti_data['maruti_SMA50_movement'].max(),
            sbi_data['sbi_SMA50_movement'] .max(),
            sunpharma_data['sunpharma_SMA50_movement'].max(),
            tatasteel_data['tatasteel_SMA50_movement'].max(),
            wipro_data['wipro_SMA50_movement'].max(),
            hindalco_data['hindalco_SMA50_movement'].max()

                
]

company_movements =list(zip(companies,max_movements))
print(company_movements)

# companies in descending order based on the largest SMA movement
sorted_companies = sorted(company_movements,key=lambda x: x[1],reverse=True)

# Extracting the sorted companies
sorted_company = [company[0] for company in sorted_companies]

print("Companies in Descending Order of largest SMA Movement:")
i=1
for company_name in sorted_company:
    print(f'{i}. {company_name}')
    i+=1

# Plot the moving averages
plt.figure(figsize=(12,6))
plt.plot(Adanient_data['Adj Close'],label='Adanient Adj Close')
plt.plot(Axisbank_data['Adj Close'],label='Axisbank Adj Close')
plt.plot(airtel_data['Adj Close'], label='airtel Adj Close')
plt.plot(Cipla_data['Adj Close'], label='Cipla Adj Close')
plt.plot(hinduuniliver_data['Adj Close'], label='hinduuniliver Adj Close')
plt.plot(infosys_data['Adj Close'], label='infosys Adj Close')
plt.plot(itc_data['Adj Close'], label='itc Adj Close')
plt.plot(maruti_data['Adj Close'],label='maruti Adj Close')
plt.plot(sbi_data['Adj Close'], label='sbi Adj Close')
plt.plot(sunpharma_data['Adj Close'],label='sunpharma Adj Close')
plt.plot(tatasteel_data['Adj Close'], label='tatasteel Adj Close')
plt.plot(wipro_data['Adj Close'], label='wipro Adj Close')
plt.plot(hindalco_data['Adj Close'], label='hindalco Adj Close')


plt.title('Simple Moving average comparision')
plt.xlabel('Date')
plt.ylabel('stockPrice')
plt.legend()
plt.grid(True)
plt.show()
