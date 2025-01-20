import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
THRESHOLD = 3
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = os.environ.get("API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


def get_stock_data(stock_symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": STOCKS_API_KEY
    }
    res = requests.get(url="https://www.alphavantage.co/query", params=params)
    res.raise_for_status()
    daily_prices = list(res.json()["Time Series (Daily)"].values())
    today_close = float(daily_prices[0]["4. close"])
    yesterday_close = float(daily_prices[1]["4. close"])

    percentage_change = ((today_close - yesterday_close)/yesterday_close) * 100
    return percentage_change


def get_news(company_name, limit=3):
    params_news = {
        "q": company_name,
        "apiKey": NEWS_API_KEY
    }
    res_news = requests.get(url="https://newsapi.org/v2/everything", params=params_news)
    res_news.raise_for_status()
    news_data = res_news.json()["articles"][:limit]
    return news_data


def format_message(stock_symbol, percentage_change, articles):
    icon = "🔺" if percentage_change > 0 else "🔻"
    messages = [f"{stock_symbol}: {icon} {abs(percentage_change):.2f}%"]

    for article in articles:
        headline = article.get("title", "No title available")
        description = article.get("description", "No description available")
        messages.append(f"Headline: {headline}\nBrief: {description}")
    return messages


change_percent = get_stock_data(STOCK)
if abs(change_percent) >= THRESHOLD:
    news_articles = get_news(COMPANY_NAME)
    for message_body in format_message(STOCK, change_percent, news_articles):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_="+15074422434",
            to="+91xxxxxxxxx",
        )
