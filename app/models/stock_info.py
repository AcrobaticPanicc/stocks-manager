import csv


class StockInfo:

    def __init__(self):
        self.tickers = list(self._load_all_tickers())
        self.logos = list(self._load_all_logos())

    @staticmethod
    def _load_all_tickers():
        with open('app/data/tickers.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i in csv_reader:
                yield dict(company=i[0], symbol=i[1])

    @staticmethod
    def _load_all_logos():
        with open('app/data/logo.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i in csv_reader:
                yield dict(company=i[0], logo=i[1])

    def get_full_name(self, stock_symbol):
        for stock in self.tickers:
            if stock['symbol'] == stock_symbol:
                return stock

    def get_logo_url(self, stock_symbol):
        for logo in self.logos:
            if logo['company'] == stock_symbol:
                return logo['logo']


'''
_load_all_tickers
{'company': 'American Electric Technologies, Inc.', 'symbol': 'AETI'}
_load_all_logos
{'company': 'BIIB', 'logo': ' https://logo.clearbit.com/biogen.com'}
'''
