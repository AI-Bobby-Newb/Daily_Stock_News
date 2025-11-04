"""
Configuration and constants for the Daily Stock News application
"""

# Market indices symbols
INDICES = {
    'NASDAQ': '^IXIC',
    'S&P 500': '^GSPC',
    'DOW': '^DJI'
}

# Sample of popular stocks from each index for scanning
# In a production app, you'd fetch the complete constituent lists
NASDAQ_TICKERS = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'COST', 'ASML',
    'NFLX', 'AMD', 'ADBE', 'PEP', 'CSCO', 'INTC', 'CMCSA', 'TMUS', 'TXN', 'QCOM',
    'AMGN', 'HON', 'AMAT', 'INTU', 'SBUX', 'ISRG', 'BKNG', 'ADP', 'GILD', 'VRTX',
    'REGN', 'ADI', 'MDLZ', 'PYPL', 'LRCX', 'PANW', 'MU', 'SNPS', 'CDNS', 'MELI',
    'KLAC', 'CRWD', 'ABNB', 'MAR', 'MRVL', 'ORLY', 'CSX', 'FTNT', 'MNST', 'ADSK'
]

SP500_TICKERS = [
    'AAPL', 'MSFT', 'NVDA', 'AMZN', 'META', 'GOOGL', 'BRK.B', 'LLY', 'AVGO', 'JPM',
    'TSLA', 'V', 'WMT', 'UNH', 'XOM', 'MA', 'PG', 'COST', 'HD', 'JNJ',
    'NFLX', 'BAC', 'ABBV', 'CRM', 'KO', 'CVX', 'MRK', 'ORCL', 'AMD', 'PEP',
    'TMO', 'ADBE', 'WFC', 'ACN', 'LIN', 'MCD', 'CSCO', 'ABT', 'PM', 'IBM',
    'GE', 'INTU', 'TXN', 'ISRG', 'CAT', 'VZ', 'CMCSA', 'QCOM', 'DHR', 'AMGN'
]

DOW_TICKERS = [
    'AAPL', 'MSFT', 'UNH', 'GS', 'HD', 'CAT', 'MCD', 'AMGN', 'V', 'CRM',
    'BA', 'HON', 'IBM', 'TRV', 'JPM', 'AXP', 'PG', 'JNJ', 'CVX', 'WMT',
    'MMM', 'DIS', 'NKE', 'MRK', 'KO', 'CSCO', 'DOW', 'VZ', 'INTC', 'WBA'
]

# Combine all tickers for comprehensive scanning
ALL_TICKERS = list(set(NASDAQ_TICKERS + SP500_TICKERS + DOW_TICKERS))

# News keywords for filtering important events
NEWS_KEYWORDS = [
    'earnings', 'merger', 'acquisition', 'deal', 'FDA', 'approval',
    'partnership', 'buyout', 'revenue', 'profit', 'loss', 'guidance',
    'forecast', 'upgrade', 'downgrade', 'analyst', 'investigation',
    'lawsuit', 'settlement', 'bankruptcy', 'IPO', 'split', 'dividend'
]
