import os
import logging
import pandas as pd
import requests
from pandas import json_normalize
from datetime import datetime, timedelta
import time
from io import BytesIO
from common import headers

logger = logging
logger.basicConfig(filename='app.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')


## STOCK TRADING HISTORICAL DATA
def stock_historical_data_test(symbol="FPT", start_date="2023-01-01", end_date="2023-05-06"):
    """
    This function returns the stock historical daily data.
    Args:
        symbol (:obj:`str`, required): 3 digits name of the desired stock.
        start_date (:obj:`str`, required): the start date to get data (YYYY-mm-dd).
        end_date (:obj:`str`, required): the end date to get data (YYYY-mm-dd).
    Returns:
        :obj:`pandas.DataFrame`:
        | tradingDate | open | high | low | close | volume |
        | ----------- | ---- | ---- | --- | ----- | ------ |
        | YYYY-mm-dd  | xxxx | xxxx | xxx | xxxxx | xxxxxx |

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid.
    """
    fd = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
    td = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))
    data = requests.get('https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars-long-term?ticker={}&type=stock&resolution=D&from={}&to={}'.format(symbol, fd, td)).json()
    df = json_normalize(data['data'])
    df['tradingDate'] = pd.to_datetime(df.tradingDate.str.split("T", expand=True)[0])
    df.columns = df.columns.str.title()
    df.rename(columns={'Tradingdate':'TradingDate'}, inplace=True)
    return df


class Analysis():
    symbol = ""
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.data_overview = self.get_base_information(symbol)

    def get_base_information(self, symbol):
        data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{}/overview'.format(symbol)).json()
        df = json_normalize(data)
        return df

    def get_stock_symbol(self):
        return self.symbol

    def get_data_overview(self):
        return self.data_overview

    # COMPANY OVERVIEW
    def company_overview (self):
        """
        This function returns the company overview of a target stock symbol
        Args:
            symbol (:obj:`str`, required): 3 digits name of the desired stock.
        """
        data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{}/overview'.format(self.symbol)).json()
        df = json_normalize(data)
        return df

if __name__ == "__main__":
    Ana = Analysis("DIG")
    data = Ana.get_data_overview()
    column_name = data.columns.values.tolist()
    logger.info(f"data of the {Ana.get_stock_symbol()} is\n {data}")
    logger.info(f"{column_name}")
    column_name_company_overview = Ana.company_overview().columns.values.tolist()
    logger.info(f"company overview is\n {Ana.company_overview()}")
    logger.info(f"{column_name_company_overview}")

    history_fpt = stock_historical_data_test()
    logger.info(f"history of fpt\n{history_fpt}")
