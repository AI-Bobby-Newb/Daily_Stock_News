"""
Module for fetching important market news
"""
import yfinance as yf
from datetime import datetime, timedelta
from config import NEWS_KEYWORDS, ALL_TICKERS
import random


def fetch_market_news():
    """
    Fetch important market news from various sources
    Returns list of news articles
    """
    print("Fetching latest market news...")

    all_news = []

    # Get news from major market tickers
    major_tickers = ['^GSPC', '^DJI', '^IXIC']  # S&P 500, DOW, NASDAQ

    for ticker_symbol in major_tickers:
        try:
            ticker = yf.Ticker(ticker_symbol)
            news = ticker.news
            if news:
                all_news.extend(news)
        except Exception as e:
            pass

    # Get news from top stocks (sample to avoid rate limiting)
    sample_tickers = random.sample(ALL_TICKERS, min(20, len(ALL_TICKERS)))

    for symbol in sample_tickers:
        try:
            ticker = yf.Ticker(symbol)
            news = ticker.news
            if news:
                all_news.extend(news)
        except Exception as e:
            pass

    # Remove duplicates based on title
    unique_news = {}
    for article in all_news:
        title = article.get('title', '')
        if title and title not in unique_news:
            unique_news[title] = article

    news_list = list(unique_news.values())

    # Sort by publish time (most recent first)
    news_list.sort(key=lambda x: x.get('providerPublishTime', 0), reverse=True)

    print(f"Found {len(news_list)} news articles\n")

    return news_list


def filter_important_news(news_list, max_articles=10):
    """
    Filter news for important events based on keywords
    """
    important_news = []
    regular_news = []

    for article in news_list:
        title = article.get('title', '').lower()
        summary = article.get('summary', '').lower()
        combined = title + ' ' + summary

        # Check if article contains important keywords
        is_important = any(keyword in combined for keyword in NEWS_KEYWORDS)

        if is_important:
            important_news.append(article)
        else:
            regular_news.append(article)

    # Combine important news first, then add regular news to reach max_articles
    filtered_news = important_news[:max_articles]
    if len(filtered_news) < max_articles:
        remaining = max_articles - len(filtered_news)
        filtered_news.extend(regular_news[:remaining])

    return filtered_news


def format_news(news_list):
    """
    Format news articles for display
    """
    output = []
    output.append("\n" + "="*60)
    output.append("IMPORTANT MARKET NEWS")
    output.append("="*60 + "\n")

    if not news_list:
        output.append("No news available at this time.\n")
        return "\n".join(output)

    for i, article in enumerate(news_list, 1):
        title = article.get('title', 'No title')
        publisher = article.get('publisher', 'Unknown')
        link = article.get('link', '')

        # Format publish time
        timestamp = article.get('providerPublishTime')
        if timestamp:
            publish_time = datetime.fromtimestamp(timestamp)
            time_str = publish_time.strftime("%b %d, %I:%M %p")
        else:
            time_str = "Unknown time"

        output.append(f"{i}. {title}")
        output.append(f"   Source: {publisher} | {time_str}")

        # Add related tickers if available
        related = article.get('relatedTickers', [])
        if related:
            tickers_str = ', '.join(related[:5])  # Show first 5 tickers
            output.append(f"   Related: {tickers_str}")

        if link:
            output.append(f"   Link: {link}")

        output.append("")

    return "\n".join(output)


def get_important_news(max_articles=10):
    """
    Main function to get and format important market news
    """
    news_list = fetch_market_news()
    filtered_news = filter_important_news(news_list, max_articles)
    return format_news(filtered_news)
