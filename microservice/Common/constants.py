from enum import Enum

class StockIndex(str, Enum):
    __doc__ = """Index in stock, with each index perfom kind of infor within reflect market sentiment,
            investment decision will be based on all index,"""
    VOLUMN = 'Volumn'
    ROE = 'state2'
    PE = "Price to Earning Ratio (PER)"
    EPS = ""
    DPR = ""
    ROA = ""
    PB = ""
    BETA = ""
    MA = ""
    MACD = ""
    RSI = ""
    MFI = ""
    FIBONACCI = ""

class CompanyProperty(str, Enum):
    __doc__ = """Dividends are a sum of money paid regularly (typically quarterly or anually)
    by a company to its shareholders profits after fulfilling the tax obligation
    and deducting other expenses of that company."""
    TIME_DIVIDENDS = 360
    DIVIDENDS_QUARTERLY = "Typically quarterly"
    DIVIDENDS_ANUALLY = "Anually"

class MarketPsychology(str, Enum):
    __doc__= """The CBOE Volatility Index (VIX) is a real-time index
    that represents the market is expectations for the relative strength
    of near-term price changes of the S&P 500 Index (SPX)."""
    VIX = ""

class Tech:
    FPT = "FPT"