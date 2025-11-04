"""
Module for scanning stocks and finding biggest gainers and losers
"""
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import ALL_TICKERS


def fetch_stock_data(symbol):
    """
    Fetch stock data for a single ticker
    Returns tuple of (symbol, data_dict) or (symbol, None) on error
    """
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period='2d')

        if len(hist) >= 2:
            current_price = hist['Close'].iloc[-1]
            previous_close = hist['Close'].iloc[-2]
            volume = hist['Volume'].iloc[-1]
            change = current_price - previous_close
            change_percent = (change / previous_close) * 100

            return symbol, {
                'symbol': symbol,
                'name': ticker.info.get('longName', symbol),
                'current_price': current_price,
                'previous_close': previous_close,
                'change': change,
                'change_percent': change_percent,
                'volume': volume
            }
        else:
            # Try getting data from info
            info = ticker.info
            current_price = info.get('currentPrice', info.get('regularMarketPrice'))
            previous_close = info.get('previousClose')

            if current_price and previous_close:
                change = current_price - previous_close
                change_percent = (change / previous_close) * 100

                return symbol, {
                    'symbol': symbol,
                    'name': info.get('longName', symbol),
                    'current_price': current_price,
                    'previous_close': previous_close,
                    'change': change,
                    'change_percent': change_percent,
                    'volume': info.get('volume', 0)
                }

        return symbol, None
    except Exception as e:
        # Silent fail for individual stocks
        return symbol, None


def scan_stocks(tickers=None):
    """
    Scan multiple stocks in parallel
    Returns list of stock data dictionaries
    """
    if tickers is None:
        tickers = ALL_TICKERS

    print(f"\nScanning {len(tickers)} stocks for gainers and losers...")
    print("This may take a minute...\n")

    stocks_data = []

    # Use ThreadPoolExecutor for parallel fetching
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_stock_data, ticker): ticker for ticker in tickers}

        completed = 0
        for future in as_completed(futures):
            completed += 1
            if completed % 10 == 0:
                print(f"Progress: {completed}/{len(tickers)} stocks scanned...")

            symbol, data = future.result()
            if data:
                stocks_data.append(data)

    print(f"Successfully scanned {len(stocks_data)} stocks\n")
    return stocks_data


def get_top_movers(stocks_data, count=5):
    """
    Get top gainers and losers from stock data
    Returns tuple of (gainers, losers)
    """
    # Sort by change percentage
    sorted_stocks = sorted(stocks_data, key=lambda x: x['change_percent'], reverse=True)

    gainers = sorted_stocks[:count]
    losers = sorted_stocks[-count:][::-1]  # Reverse to show worst first

    return gainers, losers


def format_movers(gainers, losers):
    """
    Format gainers and losers data for display
    """
    output = []

    # Top Gainers
    output.append("="*60)
    output.append("TOP 5 GAINERS")
    output.append("="*60 + "\n")

    for i, stock in enumerate(gainers, 1):
        output.append(f"{i}. {stock['symbol']:6} - {stock['name'][:40]}")
        output.append(f"   Price: ${stock['current_price']:>10,.2f}  "
                     f"Change: +{stock['change']:>8,.2f} (+{stock['change_percent']:>6.2f}%)")
        output.append(f"   Volume: {stock['volume']:>15,}")
        output.append("")

    # Top Losers
    output.append("\n" + "="*60)
    output.append("TOP 5 LOSERS")
    output.append("="*60 + "\n")

    for i, stock in enumerate(losers, 1):
        output.append(f"{i}. {stock['symbol']:6} - {stock['name'][:40]}")
        output.append(f"   Price: ${stock['current_price']:>10,.2f}  "
                     f"Change: {stock['change']:>8,.2f} ({stock['change_percent']:>6.2f}%)")
        output.append(f"   Volume: {stock['volume']:>15,}")
        output.append("")

    return "\n".join(output)
