# Daily Stock News

A Python CLI application that provides up-to-date stock market information including:
- Market indices performance (NASDAQ, S&P 500, DOW)
- Top 5 biggest gainers and losers
- Important market news (earnings, deals, acquisitions, etc.)

## Features

- **Market Overview**: Real-time performance of major indices
- **Top Movers**: Scan stocks to find the biggest gainers and losers of the day
- **Important News**: Curated news feed highlighting significant market events
- **Fast & Free**: Uses Yahoo Finance API (no API key required)
- **Flexible Modes**: Choose what information you want to see

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AI-Bobby-Newb/Daily_Stock_News.git
cd Daily_Stock_News
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Get the full daily market report:
```bash
python main.py
```

This will display:
1. Market indices overview (NASDAQ, S&P 500, DOW)
2. Top 5 gainers and losers
3. Important market news

### Command Line Options

**Quick mode** (only show market indices):
```bash
python main.py --quick
```

**Skip news** (faster execution):
```bash
python main.py --no-news
```

**Skip stock scanning** (faster execution):
```bash
python main.py --no-movers
```

**News only**:
```bash
python main.py --news-only
```

### Help

```bash
python main.py --help
```

## Sample Output

```
============================================================
               DAILY STOCK MARKET REPORT
               November 04, 2025 - 02:30 PM
============================================================

============================================================
MARKET OVERVIEW - November 04, 2025
============================================================

NASDAQ        14,321.45
             🟢    +123.45 ( +0.87%)

S&P 500        4,567.89
             🟢     +45.67 ( +1.01%)

DOW           35,678.90
             🔴     -78.90 ( -0.22%)

============================================================
TOP 5 GAINERS
============================================================

1. NVDA   - NVIDIA Corporation
   Price:  $   450.23  Change:   +45.67 ( +11.28%)
   Volume:     125,450,000

...
```

## How It Works

The application uses the `yfinance` library to fetch real-time stock data from Yahoo Finance. It:

1. Fetches current prices and changes for major market indices
2. Scans a curated list of popular stocks from NASDAQ, S&P 500, and DOW
3. Identifies the biggest percentage gainers and losers
4. Aggregates news from multiple sources and filters for important events

## Configuration

You can customize the stock lists and news keywords by editing `config.py`:
- `NASDAQ_TICKERS`: List of NASDAQ stocks to scan
- `SP500_TICKERS`: List of S&P 500 stocks to scan
- `DOW_TICKERS`: List of DOW stocks to scan
- `NEWS_KEYWORDS`: Keywords for filtering important news

## Requirements

- Python 3.7+
- Internet connection
- Dependencies listed in `requirements.txt`

## Limitations

- Stock scanning is limited to a curated list of popular stocks (not all stocks in each index)
- Data is fetched from Yahoo Finance and subject to their rate limits
- News availability depends on Yahoo Finance's news feed
- Market data may have a slight delay (typically 15-20 minutes)
- Some networks/environments may block Yahoo Finance access (403 errors)

## Installation Notes

If you encounter issues installing the `multitasking` dependency, you can manually install it:

```bash
# Download and extract
pip download multitasking --no-deps -d /tmp
cd /tmp
tar -xzf multitasking-*.tar.gz

# Copy to site-packages
cp -r multitasking-*/multitasking ~/.local/lib/python3.11/site-packages/

# Then install yfinance without deps
pip install yfinance --no-deps
```

Alternatively, install dependencies separately:
```bash
pip install pandas numpy beautifulsoup4 requests pytz frozendict peewee protobuf websockets curl_cffi platformdirs
pip install yfinance --no-deps
```

## License

MIT License - see LICENSE file for details

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer

This tool is for informational purposes only. It is not financial advice. Always do your own research before making investment decisions.
