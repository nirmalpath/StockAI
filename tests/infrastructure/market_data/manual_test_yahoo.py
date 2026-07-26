from stockai.infrastructure.market_data import YahooFinanceProvider

provider = YahooFinanceProvider()

quote = provider.get_quote("RELIANCE.NS")

print(quote)
