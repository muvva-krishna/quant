import pandas as pd

companies_info = {
    'Adanient':pd.read_csv("./database/ADANIENT.NS.csv"),
    'Axis bank':pd.read_csv("./database/AXISBANK.NS.csv"),
    'Airtel':pd.read_csv("./database/BHARTIARTL.NS.csv"),
    'Cipla':pd.read_csv("./database/CIPLA.NS.csv"),
    'Hindustan Uniliver':pd.read_csv("./database/HINDUNILVR.NS.csv"),
    'Infosys':pd.read_csv("./database/INFY.NS.csv"),
    'ITC':pd.read_csv("./database/ITC.NS.csv"),
    'Maruti':pd.read_csv("./database/MARUTI.NS.csv"),
    'SBI':pd.read_csv("./database/SBIN.NS.csv"),
    'Sun pharma':pd.read_csv("./database/SUNPHARMA.NS.csv"),
    'Tata Steel':pd.read_csv("./database/TATASTEEL.NS.csv"),
    'Wipro':pd.read_csv("./database/WIPRO.NS.csv"),
    'Hindalco':pd.read_csv("./database/HINDALCO.NS.csv")
}

def sma_movement(data):

    sma_start = data['Close'].iloc[49:100].rolling(50).mean().iloc[-1]
    sma_end = data['Close'].iloc[195:245].rolling(50).mean().iloc[-1]
    
    if (sma_start != 0):
        movement_percentage = ((sma_end - sma_start) / sma_start) * 100
        return movement_percentage
    else:
        return 0

sma_percentages = {}

for company_name, company_data in companies_info.items():
    movement_percentage = sma_movement(company_data)

    if (movement_percentage!=0):
        sma_percentages[company_name] = movement_percentage

sorted_sma_percentages = dict(sorted(sma_percentages.items(), key=lambda x:x[1], reverse=True))
i = 1
for company_name, sma_percentage in sorted_sma_percentages.items():
    print(f"{i}) {company_name}:{sma_percentage}%")
    i += 1
