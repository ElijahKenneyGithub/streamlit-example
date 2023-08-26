import streamlit as st
import pandas as pd 
import yfinance as yf 


st.title = "Stock Price App"
st.write("This is a stock price app")


# Input for company symbol
company_symbol = st.text_input("Enter the Company Symbol (e.g., AAPL for Apple):")

# Fetch financial data
if company_symbol:
    try:
        company = yf.Ticker(company_symbol)
        company_info = company.info
        st.subheader(f"Real-Time Financial Data for {company_info['longName']} ({company_symbol})")
        
        # Display general company information
        st.write(f"Industry: {company_info['industry']}")
        st.write(f"Market Cap: {company_info['marketCap']}")
        
        # Display financial metrics
        st.write("Financial Metrics:")
        financial_metrics = {
            'Previous Close': company_info['previousClose'],
            'Open': company_info['open'],
            'Day Range': f"{company_info['dayLow']} - {company_info['dayHigh']}",
            '52-Week Range': f"{company_info['fiftyTwoWeekLow']} - {company_info['fiftyTwoWeekHigh']}",
            'Volume': company_info['volume'],
            'Average Volume': company_info['averageVolume'],
        }
        st.write(pd.DataFrame.from_dict(financial_metrics, orient='index', columns=['Value']))
        
    except Exception as e:
        st.write("Error:", str(e))
