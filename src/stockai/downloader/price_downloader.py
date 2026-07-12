from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
from tqdm import tqdm

from stockai.market_data.yahoo_client import YahooFinanceClient
from stockai.watchlist.watchlist import Watchlist
from stockai.logger import logger


class PriceDownloader:

    def __init__(self, max_workers: int = 8):

        self.client = YahooFinanceClient()

        self.watchlist = Watchlist()

        self.max_workers = max_workers

    def _download_stock(self, ticker):

        try:

            quote = self.client.get_quote(ticker)

            logger.info(f"Downloaded {ticker}")

            return vars(quote)

        except Exception as ex:

            logger.error(f"{ticker}: {ex}")

            return None

    def download(self):

        tickers = self.watchlist.tickers()

        results = []

        with ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:

            futures = {

                executor.submit(
                    self._download_stock,
                    ticker
                ): ticker

                for ticker in tickers

            }

            for future in tqdm(

                    as_completed(futures),

                    total=len(futures),

                    desc="Downloading"

            ):

                data = future.result()

                if data:

                    results.append(data)

        return pd.DataFrame(results)