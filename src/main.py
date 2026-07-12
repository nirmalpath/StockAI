from stockai.downloader.price_downloader import PriceDownloader

downloader = PriceDownloader()

df = downloader.download()

print(df.head())