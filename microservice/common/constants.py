import os
from enum import Enum
from .utils import get_git_root

REPO_DIR = get_git_root(__file__)
LOG = os.path.join(REPO_DIR, "log", "app{}.log")
MICROSERVICE = os.path.join(REPO_DIR, "microservice")
COMMON = os.path.join(MICROSERVICE, "Common")
POSTGRES = os.path.join(MICROSERVICE, "postgres_sql")
CONFIG_POSTGRES = os.path.join(POSTGRES, "Postgres.cfg")

class _StrEnum(str, Enum):
    __doc__ = '''In python 3.11 have class for constain include str and Enum'''

class PostGresql(_StrEnum):
    RULE = '''all column in table should be lower case'''
    FLOAT = 'float'
    VAR_CHAR_30 = 'varchar(30)'
    NOT_NULL = 'NOT NULL'
    CREATE_PRICE_BOARD_TABLE = f'''CREATE TABLE __TABLE_NAME__ (\
                                    cp {FLOAT} {NOT_NULL},\
                                    fv {FLOAT} {NOT_NULL},\
                                    mav {FLOAT} {NOT_NULL},\
                                    nstv {FLOAT} {NOT_NULL},\
                                    nstp {FLOAT} {NOT_NULL},\
                                    rsi {FLOAT} {NOT_NULL},\
                                    macdv {FLOAT} {NOT_NULL},\
                                    macdsignal {VAR_CHAR_30} {NOT_NULL},\
                                    tsignal {VAR_CHAR_30} {NOT_NULL},\
                                    avgsignal {VAR_CHAR_30} {NOT_NULL},\
                                    ma20 {FLOAT} {NOT_NULL},\
                                    ma50 {FLOAT} {NOT_NULL},\
                                    ma100 {FLOAT} {NOT_NULL},\
                                    session {FLOAT} {NOT_NULL},\
                                    mw3d {FLOAT} {NOT_NULL},\
                                    mw1m {FLOAT} {NOT_NULL},\
                                    mw3m {FLOAT} {NOT_NULL},\
                                    mw1y {FLOAT} {NOT_NULL},\
                                    rs3d {FLOAT} {NOT_NULL},\
                                    rs1m {FLOAT} {NOT_NULL},\
                                    rs3m {FLOAT} {NOT_NULL},\
                                    rs1y {FLOAT} {NOT_NULL},\
                                    rsavg {FLOAT} {NOT_NULL},\
                                    hp1m {FLOAT} {NOT_NULL},\
                                    hp3m {FLOAT} {NOT_NULL},\
                                    hp1y {FLOAT} {NOT_NULL},\
                                    lp1m {FLOAT} {NOT_NULL},\
                                    lp3m {FLOAT} {NOT_NULL},\
                                    lp1y {FLOAT} {NOT_NULL},\
                                    hp1yp {FLOAT} {NOT_NULL},\
                                    lp1yp {FLOAT} {NOT_NULL},\
                                    pe {FLOAT} {NOT_NULL},\
                                    pb {FLOAT} {NOT_NULL},\
                                    roe {FLOAT} {NOT_NULL},\
                                    oscore {FLOAT} {NOT_NULL},\
                                    av {FLOAT} {NOT_NULL},\
                                    bv {FLOAT} {NOT_NULL},\
                                    ev {FLOAT} {NOT_NULL},\
                                    hmp {FLOAT} {NOT_NULL},\
                                    mscore {FLOAT} {NOT_NULL},\
                                    delta1m {FLOAT} {NOT_NULL},\
                                    delta1y {FLOAT} {NOT_NULL},\
                                    vnipe {FLOAT} {NOT_NULL},\
                                    vnipb {FLOAT} {NOT_NULL},\
                                    vnid3d {FLOAT} {NOT_NULL},\
                                    vnid1m {FLOAT} {NOT_NULL},\
                                    vnid3m {FLOAT} {NOT_NULL},\
                                    vnid1y {FLOAT} {NOT_NULL});'''

    DROP_TABLE = """DROP table IF EXISTS __TABLE_NAME__ """

class StockIndex(_StrEnum):
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

