from vnstock import *
import pandas as pd
import requests
from pandas import json_normalize
from datetime import datetime, timedelta
import time
from io import BytesIO

headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'X-Fiin-Key': 'KEY',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Fiin-User-ID': 'ID',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'X-Fiin-Seed': 'SEED',
        'sec-ch-ua-platform': 'Windows',
        'Origin': 'https://iboard.ssi.com.vn',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://iboard.ssi.com.vn/',
        'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7'
        }


r = api_request()

def listing_companies_test():
    url = 'https://fiin-core.ssi.com.vn/Master/GetListOrganization?language=vi'
    r = api_request_test(url)
    print(r)
    df = pd.DataFrame(r['items']).drop(columns=['organCode', 'icbCode', 'organTypeCode', 'comTypeCode']).rename(columns={'comGroupCode': 'group_code', 'organName': 'company_name', 'organShortName':'company_short_name'})
    return df

def api_request_test(url, headers=headers):
    print("api_request_test")
    r = requests.get(url, headers).json()
    return r

def ticker_overview_test(symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{}/overview'.format(symbol)).json()
    df = json_normalize(data)
    return df

def get_latest_indices_test(headers=headers):
    """
    Retrieve the latest indices values
    """
    url = "https://fiin-market.ssi.com.vn/MarketInDepth/GetLatestIndices?language=vi&pageSize=999999&status=1"
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json_normalize(response.json()['items'])
    return result


if __name__  == "__main__":
    try:
        latest_index = get_latest_indices_test()
        print(latest_index)
        print(type(latest_index))
    except Exception as e:
        print(e)

    tcb = ticker_overview_test("TCB")
    hsv = ticker_overview_test("HSV")
    print(tcb.values.tolist())
    print(type(tcb))
    print("* "*10)
    print(hsv.values.tolist())
    print(type(hsv))