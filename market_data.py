"""
Module for fetching market indices data
"""
import yfinance as yf
from datetime import datetime
from config import INDICES
import warnings

# Suppress yfinance warnings
warnings.filterwarnings('ignore')


def get_market_overview():
    """
    Fetch current market data for major indices
    Returns a dictionary with index performance
    """
    market_data = {}

    print("Fetching market indices data...")

    for name, symbol in INDICES.items():
        try:
            # Configure ticker with user agent
            ticker = yf.Ticker(symbol)

            # Try to get historical data first
            hist = ticker.history(period='2d', timeout=10)

            if not hist.empty and len(hist) >= 1:
                current_price = hist['Close'].iloc[-1]
                previous_close = hist['Close'].iloc[-2] if len(hist) >= 2 else hist['Open'].iloc[0]
                change = current_price - previous_close
                change_percent = (change / previous_close) * 100 if previous_close else 0
            else:
                # Fallback to info data
                info = ticker.info
                if info:
                    current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
                    previous_close = info.get('previousClose', info.get('open', current_price))
                    change = current_price - previous_close if current_price else 0
                    change_percent = (change / previous_close) * 100 if previous_close else 0
                else:
                    raise ValueError("No data available")

            market_data[name] = {
                'symbol': symbol,
                'current_price': current_price,
                'previous_close': previous_close,
                'change': change,
                'change_percent': change_percent
            }
        except Exception as e:
            print(f"Error fetching data for {name}: {str(e)}")
            market_data[name] = None

    return market_data


def format_market_overview(market_data):
    """
    Format market overview data for display
    """
    output = []
    output.append("\n" + "="*60)
    output.append("MARKET OVERVIEW - " + datetime.now().strftime("%B %d, %Y"))
    output.append("="*60 + "\n")

    for name, data in market_data.items():
        if data:
            sign = "+" if data['change'] >= 0 else ""
            color_indicator = "🟢" if data['change'] >= 0 else "🔴"

            output.append(f"{name:12} {data['current_price']:>12,.2f}")
            output.append(f"             {color_indicator} {sign}{data['change']:>10,.2f} ({sign}{data['change_percent']:>6.2f}%)")
            output.append("")
        else:
            output.append(f"{name:12} [Data unavailable]")
            output.append("")

    return "\n".join(output)
