import json
import os
import sys
import time

import pandas as pd
import requests

sys.path.insert(0, "/home/ziuteng/ncd_proj/ncd_project/microservice/")
from common import save_data_frame_to_csv, get_logger, embrace
from common.constants import Tech
from pandas import json_normalize
from vn_stock.utlis import stock_headers

logger = get_logger()
csv_filename = "{}/vnstock.csv".format(os.path.dirname(__file__))
latest_indices_file = "{}/latest_indices.csv".format(os.path.dirname(__file__))
latest_indices_file_json = "{}/latest_indices.json".format(os.path.dirname(__file__))

# STOCK TRADING HISTORICAL DATA

def stock_historical_data_test(symbol="FPT", start_date="2023-05-06", end_date="2023-07-29"):
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
    data = requests.get(
        'https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars-long-term?ticker={}&type=stock&resolution=D&from={}&to={}'.format(symbol, fd, td)).json()
    df = json_normalize(data['data'])
    df['tradingDate'] = pd.to_datetime(
        df.tradingDate.str.split("T", expand=True)[0])
    df.columns = df.columns.str.title()
    df.rename(columns={'Tradingdate': 'TradingDate'}, inplace=True)
    return df

def get_latest_indices(headers=stock_headers):
    """
    Retrieve the latest indices values
    """
    url = "https://fiin-market.ssi.com.vn/MarketInDepth/GetLatestIndices?language=vi&pageSize=999999&status=1"
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    with open(latest_indices_file_json, 'w') as data:
        json.dump(response.json(), data, indent=4)

    result = json_normalize(response.json()['items'])
    return result


class Analysis():
    symbol = ""

    def __init__(self, symbol: str):
        self.symbol = symbol
        self.data_overview = self.get_base_information(symbol)

    def get_base_information(self, symbol):
        data = requests.get(
            'https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{}/overview'.format(symbol)).json()
        df = json_normalize(data)
        return df

    def get_stock_symbol(self):
        return self.symbol

    def get_data_overview(self):
        return self.data_overview

    # COMPANY OVERVIEW
    def company_overview(self):
        """
        This function returns the company overview of a target stock symbol
        Args:
            symbol (:obj:`str`, required): 3 digits name of the desired stock.
        """
        data = requests.get(
            'https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{}/overview'.format(self.symbol)).json()
        df = json_normalize(data)
        return df

    def get_PE(self):
        return 0

def test_symbol_dig_fpt():

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
    history_fpt.to_csv(csv_filename)
    get_latest_indices().to_csv(latest_indices_file)

def price_board_stock(symbol_ls):
    """
    This function returns the trading price board of a target stocks list.
    Args:
        symbol_ls (:obj:`str`, required): STRING list of symbols separated by "," without any space. Ex: "TCB,SSI,BID"
    """
    data = requests.get(
        'https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/second-tc-price?tickers={}'.format(symbol_ls)).json()
    df = json_normalize(data['data'])
    # drop columns named seq

    df.drop(columns=['seq'], inplace=True)
    df = df[['t', 'cp', 'fv', 'mav', 'nstv', 'nstp', 'rsi', 'macdv', 'macdsignal',
             'tsignal', 'avgsignal', 'ma20', 'ma50', 'ma100', 'session', 'mw3d',
             'mw1m', 'mw3m', 'mw1y', 'rs3d', 'rs1m', 'rs3m', 'rs1y', 'rsavg', 'hp1m',
             'hp3m', 'hp1y', 'lp1m', 'lp3m', 'lp1y', 'hp1yp', 'lp1yp', 'pe', 'pb',
             'roe', 'oscore', 'av', 'bv', 'ev', 'hmp', 'mscore', 'delta1m',
             'delta1y', 'vnipe', 'vnipb', 'vnid3d', 'vnid1m', 'vnid3m', 'vnid1y']]

    # df = df.rename(columns={'t': 'Ticket', 'cp': 'Price', 'fv': 'KLBD/TB5D', 'mav': 'T.độ GD', 'nstv': 'KLGD ròng(CM)',
    #                         'nstp': '%KLGD ròng (CM)', 'rsi': 'RSI', 'macdv': 'MACD Hist', 'macdsignal': 'MACD Signal',
    #                         'tsignal': 'Tín hiệu KT', 'avgsignal': 'Tín hiệu TB động', 'ma20': 'MA20', 'ma50': 'MA50',
    #                         'ma100': 'MA100', 'session': 'Session +/- ', 'mscore': 'Đ.góp VNINDEX', 'pe': 'P/E', 'pb': 'P/B',
    #                         'roe': 'ROE', 'oscore': 'TCRating', 'ev': 'TCBS định giá', 'mw3d': '% thay đổi giá 3D',
    #                         'mw1m': '% thay đổi giá 1M', 'mw3m': '% thay đổi giá 3M', 'mw1y': '% thay đổi giá 1Y',
    #                         'rs3d': 'RS 3D', 'rs1m': 'RS 1M', 'rs3m': 'RS 3M', 'rs1y': 'RS 1Y', 'rsavg': 'RS TB',
    #                         'hp1m': 'Đỉnh 1M', 'hp3m': 'Đỉnh 3M', 'hp1y': 'Đỉnh 1Y', 'lp1m': 'Đáy 1M', 'lp3m': 'Đáy 3M',
    #                         'lp1y': 'Đáy 1Y', 'hp1yp': '%Đỉnh 1Y', 'lp1yp': 'Low-Price-1Y', 'delta1m': 'Price-VNI-1M',
    #                         'delta1y': 'Price-VNI-1Y', 'bv': 'Khối lượng Dư mua', 'av': 'Khối lượng Dư bán',
    #                         'hmp': 'Khớp nhiều nhất', 'vnipe': 'VNINDEX P/E', 'vnipb': 'VNINDEX P/B'})

    # df = df.rename(columns={'t': 'Mã CP', 'cp': 'Giá', 'fv': 'KLBD/TB5D', 'mav': 'T.độ GD', 'nstv': 'KLGD ròng(CM)',
    #                         'nstp': '%KLGD ròng (CM)', 'rsi': 'RSI', 'macdv': 'MACD Hist', 'macdsignal': 'MACD Signal',
    #                         'tsignal': 'Tín hiệu KT', 'avgsignal': 'Tín hiệu TB động', 'ma20': 'MA20', 'ma50': 'MA50',
    #                         'ma100': 'MA100', 'session': 'Phiên +/- ', 'mscore': 'Đ.góp VNINDEX', 'pe': 'P/E', 'pb': 'P/B',
    #                         'roe': 'ROE', 'oscore': 'TCRating', 'ev': 'TCBS định giá', 'mw3d': '% thay đổi giá 3D',
    #                         'mw1m': '% thay đổi giá 1M', 'mw3m': '% thay đổi giá 3M', 'mw1y': '% thay đổi giá 1Y',
    #                         'rs3d': 'RS 3D', 'rs1m': 'RS 1M', 'rs3m': 'RS 3M', 'rs1y': 'RS 1Y', 'rsavg': 'RS TB',
    #                         'hp1m': 'Đỉnh 1M', 'hp3m': 'Đỉnh 3M', 'hp1y': 'Đỉnh 1Y', 'lp1m': 'Đáy 1M', 'lp3m': 'Đáy 3M',
    #                         'lp1y': 'Đáy 1Y', 'hp1yp': '%Đỉnh 1Y', 'lp1yp': '%Đáy 1Y', 'delta1m': '%Giá - %VNI (1M)',
    #                         'delta1y': '%Giá - %VNI (1Y)', 'bv': 'Khối lượng Dư mua', 'av': 'Khối lượng Dư bán',
    #                         'hmp': 'Khớp nhiều nhất', 'vnipe': 'VNINDEX P/E', 'vnipb': 'VNINDEX P/B'})
    return df

@embrace
def fpt():
    fpt = Analysis(Tech.FPT)
    save_data_frame_to_csv(fpt.company_overview(), os.path.join(
        os.path.dirname(__file__), "fpt.csv"))
    save_data_frame_to_csv(price_board_stock(Tech.FPT), os.path.join(
        os.path.dirname(__file__), "fpt_price_board.csv"))