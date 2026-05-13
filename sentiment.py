from textblob import TextBlob

def analyze_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"


# Example finance news
news = "Apple stock rises after strong earnings report"

result = analyze_sentiment(news)

print("\nNews Sentiment:")
print(result)