import requests

def get_stock(stock):
    stock_dict = {
        "Apple Inc.": "AAPL",
        "Nvidia Corp": "NVDA",
        "Microsoft Corp": "MSFT",
        "Amazon.com Inc": "AMZN",
        "Meta Platforms, Inc. Class A": "META",
        "Alphabet Inc. Class A": "GOOGL",
        "Alphabet Inc. Class C": "GOOG",
        "Berkshire Hathaway Class B": "BRK.B",
        "Broadcom Inc.": "AVGO",
        "Tesla, Inc.": "TSLA",
        "Eli Lilly & Co.": "LLY",
        "Jpmorgan Chase & Co.": "JPM",
        "Unitedhealth Group Incorporated": "UNH",
        "Visa Inc.": "V",
        "Exxon Mobil Corporation": "XOM",
        "Mastercard Incorporated": "MA",
        "Procter & Gamble Company": "PG",
        "Costco Wholesale Corp": "COST",
        "Home Depot, Inc.": "HD",
        "Johnson & Johnson": "JNJ",
        "Abbvie Inc.": "ABBV",
        "Walmart Inc.": "WMT",
        "Netflix Inc": "NFLX",
        "Salesforce, Inc.": "CRM",
        "Bank of America Corporation": "BAC",
        "Oracle Corp": "ORCL",
        "Merck & Co., Inc.": "MRK",
        "Coca-Cola Company": "KO",
        "Chevron Corporation": "CVX",
        "Advanced Micro Devices": "AMD",
        "Pepsico, Inc.": "PEP",
        "Linde Plc": "LIN",
        "Cisco Systems, Inc.": "CSCO",
        "Wells Fargo & Co.": "WFC",
        "Accenture Plc": "ACN",
        "Adobe Inc.": "ADBE",
        "Thermo Fisher Scientific, Inc.": "TMO",
        "Mcdonalds Corporation": "MCD",
        "Philip Morris International Inc.": "PM",
        "Abbott Laboratories": "ABT",
        "Servicenow, Inc.": "NOW",
        "Ge Aerospace": "GE",
        "International Business Machines Corporation": "IBM",
        "Texas Instruments Incorporated": "TXN",
        "Qualcomm Inc": "QCOM",
        "Caterpillar Inc.": "CAT",
        "Intuitive Surgical Inc.": "ISRG",
        "Verizon Communications": "VZ",
        "Intuit Inc": "INTU",
        "The Walt Disney Company": "DIS"
    }

    stock_to_find = None

    for key, value in stock_dict.items():
        if key == stock:
            stock_to_find = value
            break
        elif value == stock:
            stock_to_find = value
            break

    if stock_to_find is None:
        raise ValueError("Please provide a stock within the top 50 NASDAQ stocks")

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_to_find}&interval=60min&apikey=demo'
    r = requests.get(url)
    return r.json()

