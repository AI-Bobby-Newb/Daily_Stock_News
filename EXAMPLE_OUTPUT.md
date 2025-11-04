# Example Output

This document shows example output from the Daily Stock News application.

## Full Report Example

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


Scanning 150 stocks for gainers and losers...
This may take a minute...

Progress: 10/150 stocks scanned...
Progress: 20/150 stocks scanned...
...
Progress: 150/150 stocks scanned...
Successfully scanned 145 stocks

============================================================
TOP 5 GAINERS
============================================================

1. NVDA   - NVIDIA Corporation
   Price:  $   450.23  Change:   +45.67 (+11.28%)
   Volume:     125,450,000

2. AMD    - Advanced Micro Devices, Inc.
   Price:  $   185.90  Change:   +15.23 ( +8.92%)
   Volume:      89,230,000

3. TSLA   - Tesla, Inc.
   Price:  $   245.67  Change:   +18.45 ( +8.12%)
   Volume:     156,780,000

4. META   - Meta Platforms, Inc.
   Price:  $   342.50  Change:   +22.10 ( +6.90%)
   Volume:      45,670,000

5. NFLX   - Netflix, Inc.
   Price:  $   456.78  Change:   +25.34 ( +5.87%)
   Volume:      12,340,000


============================================================
TOP 5 LOSERS
============================================================

1. INTC   - Intel Corporation
   Price:  $    32.45  Change:    -3.45 ( -9.62%)
   Volume:      98,450,000

2. BA     - The Boeing Company
   Price:  $   187.23  Change:  -15.67 ( -7.72%)
   Volume:      23,450,000

3. WBA    - Walgreens Boots Alliance, Inc.
   Price:  $    23.45  Change:   -1.67 ( -6.65%)
   Volume:      15,670,000

4. VZ     - Verizon Communications Inc.
   Price:  $    38.90  Change:   -2.34 ( -5.67%)
   Volume:      34,560,000

5. IBM    - International Business Machines Corporation
   Price:  $   145.67  Change:   -7.89 ( -5.14%)
   Volume:      18,900,000


Fetching latest market news...
Found 47 news articles

============================================================
IMPORTANT MARKET NEWS
============================================================

1. NVIDIA Announces Breakthrough AI Chip, Stock Soars
   Source: Reuters | Nov 04, 02:15 PM
   Related: NVDA, AMD, INTC
   Link: https://finance.yahoo.com/news/...

2. Federal Reserve Signals Potential Rate Cut Next Quarter
   Source: Bloomberg | Nov 04, 01:30 PM
   Related: ^GSPC, ^DJI, ^IXIC
   Link: https://finance.yahoo.com/news/...

3. Tesla Reports Record Q3 Earnings, Beats Analyst Expectations
   Source: CNBC | Nov 04, 12:45 PM
   Related: TSLA
   Link: https://finance.yahoo.com/news/...

4. Microsoft and OpenAI Expand Partnership with $10B Deal
   Source: Wall Street Journal | Nov 04, 11:20 AM
   Related: MSFT, GOOGL, META
   Link: https://finance.yahoo.com/news/...

5. FDA Approves Breakthrough Cancer Drug from Merck
   Source: Associated Press | Nov 04, 10:00 AM
   Related: MRK, PFE, JNJ
   Link: https://finance.yahoo.com/news/...

6. Amazon Announces Major Acquisition of Robotics Company
   Source: TechCrunch | Nov 04, 09:15 AM
   Related: AMZN
   Link: https://finance.yahoo.com/news/...

7. Intel Faces Analyst Downgrade Amid Chip Market Concerns
   Source: Barron's | Nov 04, 08:30 AM
   Related: INTC, NVDA, AMD
   Link: https://finance.yahoo.com/news/...

8. Oil Prices Surge on Middle East Supply Concerns
   Source: Reuters | Nov 04, 08:00 AM
   Related: XOM, CVX
   Link: https://finance.yahoo.com/news/...

9. Apple Announces New Product Launch Event for Next Month
   Source: The Verge | Nov 04, 07:45 AM
   Related: AAPL
   Link: https://finance.yahoo.com/news/...

10. Banking Sector Shows Strength as JPMorgan Raises Guidance
    Source: Financial Times | Nov 04, 07:00 AM
    Related: JPM, BAC, WFC, GS
    Link: https://finance.yahoo.com/news/...

============================================================
Report completed successfully!
============================================================
```

## Quick Mode Example

Using `python main.py --quick`:

```
============================================================
               DAILY STOCK MARKET REPORT
               November 04, 2025 - 02:30 PM
============================================================
Fetching market indices data...

============================================================
MARKET OVERVIEW - November 04, 2025
============================================================

NASDAQ        14,321.45
             🟢    +123.45 ( +0.87%)

S&P 500        4,567.89
             🟢     +45.67 ( +1.01%)

DOW           35,678.90
             🔴     -78.90 ( -0.22%)
```

## News Only Example

Using `python main.py --news-only`:

```
============================================================
               DAILY STOCK MARKET REPORT
               November 04, 2025 - 02:30 PM
============================================================
Fetching latest market news...
Found 47 news articles

============================================================
IMPORTANT MARKET NEWS
============================================================

1. NVIDIA Announces Breakthrough AI Chip, Stock Soars
   Source: Reuters | Nov 04, 02:15 PM
   Related: NVDA, AMD, INTC
   Link: https://finance.yahoo.com/news/...

2. Federal Reserve Signals Potential Rate Cut Next Quarter
   Source: Bloomberg | Nov 04, 01:30 PM
   Related: ^GSPC, ^DJI, ^IXIC
   Link: https://finance.yahoo.com/news/...

...
```
