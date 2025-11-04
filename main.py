#!/usr/bin/env python3
"""
Daily Stock News - Main Application
Get daily market overview, top gainers/losers, and important news
"""
import sys
import argparse
from datetime import datetime

from market_data import get_market_overview, format_market_overview
from stock_scanner import scan_stocks, get_top_movers, format_movers
from news_fetcher import get_important_news


def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print(" "*15 + "DAILY STOCK MARKET REPORT")
    print(" "*15 + datetime.now().strftime("%B %d, %Y - %I:%M %p"))
    print("="*60)


def main():
    """Main application function"""
    parser = argparse.ArgumentParser(
        description='Get daily stock market overview with gainers, losers, and news'
    )
    parser.add_argument(
        '--no-news',
        action='store_true',
        help='Skip fetching news (faster)'
    )
    parser.add_argument(
        '--no-movers',
        action='store_true',
        help='Skip scanning for gainers/losers (faster)'
    )
    parser.add_argument(
        '--quick',
        action='store_true',
        help='Quick mode: only show market indices'
    )
    parser.add_argument(
        '--news-only',
        action='store_true',
        help='Only fetch and display news'
    )

    args = parser.parse_args()

    print_header()

    try:
        # News only mode
        if args.news_only:
            print(get_important_news())
            return

        # Quick mode - only indices
        if args.quick:
            market_data = get_market_overview()
            print(format_market_overview(market_data))
            return

        # Full report
        # 1. Market Overview
        market_data = get_market_overview()
        print(format_market_overview(market_data))

        # 2. Top Movers
        if not args.no_movers:
            stocks_data = scan_stocks()
            gainers, losers = get_top_movers(stocks_data, count=5)
            print(format_movers(gainers, losers))

        # 3. Important News
        if not args.no_news:
            print(get_important_news(max_articles=10))

        print("\n" + "="*60)
        print("Report completed successfully!")
        print("="*60 + "\n")

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {str(e)}")
        print("Please check your internet connection and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
