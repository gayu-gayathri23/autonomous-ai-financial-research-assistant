import streamlit as st
import yfinance as yf

from textblob import TextBlob
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# OpenAI Client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Streamlit Title
st.title("Autonomous AI Financial Research Assistant")

# User Input
stock_symbol = st.text_input(
    "Enter Stock Symbol",
    "AAPL"
)

# Download Stock Data
if stock_symbol:

    stock_data = yf.download(
        stock_symbol,
        period='1y',
        auto_adjust=True
    )

    # Fix Multi-level Columns
    if hasattr(stock_data.columns, "levels"):
        stock_data.columns = stock_data.columns.get_level_values(0)

    # Stock Data
    st.subheader("Stock Data")

    st.write(stock_data.tail())
    
    if stock_data.empty:
        st.error("No stock data found.")
        st.stop()
     

    # Stock Metrics
    st.subheader("Stock Metrics")

    current_price = stock_data['Close'].iloc[-1]

    highest_price = stock_data['High'].max()

    lowest_price = stock_data['Low'].min()

    average_volume = stock_data['Volume'].mean()

    col1, col2 = st.columns(2)

    col1.metric(
        "Current Price",
        f"${current_price:.2f}"
    )

    col2.metric(
        "Highest Price",
        f"${highest_price:.2f}"
    )

    col1.metric(
        "Lowest Price",
        f"${lowest_price:.2f}"
    )

    col2.metric(
        "Average Volume",
        f"{average_volume:,.0f}"
    )

    # Closing Price Chart
    st.subheader("Closing Price Chart")

    st.line_chart(
        stock_data['Close']
    )

    # Example Financial News
    news = f"{stock_symbol} stock showing strong market momentum"

    # Sentiment Analysis
    analysis = TextBlob(news)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"

    elif polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    # Display Sentiment
    st.subheader("Market Sentiment")

    st.write(sentiment)

    # AI Investment Insight
    st.subheader("AI Investment Insight")

    prompt = f"""
You are a financial AI assistant.

Analyze the current stock performance of {stock_symbol} based on recent market trends.

Current market sentiment: {sentiment}

Give:
1. Short-term outlook
2. Long-term outlook
3. Investment risk
4. Final recommendation

IMPORTANT:
- Do not mention old years like 2023 or outdated information.
- Focus only on current and recent market conditions.
- Keep the response professional and concise.
"""


    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_insight = response.choices[0].message.content

    st.success(ai_insight)