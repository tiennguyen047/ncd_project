import sys
import psycopg2

sys.path.insert(0, "/home/ziuteng/ncd_proj/ncd_project/microservice/")
from vn_stock import price_board_stock
from common import get_logger, read_config, embrace
from common.constants import CONFIG_POSTGRES, PostGresql, Tech

postgres_config = read_config(CONFIG_POSTGRES)
logger = get_logger()

@embrace
def execute_sql(sql:str, postgres_config:dict):
    """execute sql postgresql

    Args:
        sql (str): Structured Query Language
        postgres_config (dict): config of postgresql to connect database
    """
    try:
        connection = psycopg2.connect(database=postgres_config['postgresql']['db'],
                                        host=postgres_config['postgresql']['host'],
                                        user=postgres_config['postgresql']['user'],
                                        password=postgres_config['postgresql']['passwd'],
                                        port=postgres_config['postgresql']['port'])
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        logger.exception("Failed to execute {}".format(sql), error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            logger.info("PostgreSQL connection is closed")

@embrace
def drop_table(table_name:str):
    # drop table
    sql = '''DROP table IF EXISTS {} '''.format(table_name)
    logger.info("drop table {}".format(table_name))
    sql = PostGresql.DROP_TABLE.value.replace('__TABLE_NAME__', table_name)
    logger.info(sql)
    execute_sql(sql, postgres_config)

@embrace
def check_table_exists(table_name) -> bool:
    try:
        logger.info('Check_table_exists {}'.format(table_name))
        connection = psycopg2.connect(database=postgres_config['postgresql']['db'],
                                        host=postgres_config['postgresql']['host'],
                                        user=postgres_config['postgresql']['user'],
                                        password=postgres_config['postgresql']['passwd'],
                                        port=postgres_config['postgresql']['port'])
        cursor = connection.cursor()
        connection.autocommit = True
        sql = """SELECT EXISTS (\
        SELECT 1\
        FROM information_schema.tables\
        WHERE table_name = '{}'\
        ) AS table_existencep;""".format(table_name)
        logger.info(sql)
        cursor.execute(sql)
        ret = bool(cursor.fetchone()[0])
        connection.commit()
        if ret:
            logger.info("Table {} is exists".format(table_name))
        else:
            logger.info("Table {} is NOT exists".format(table_name))
    except (Exception, psycopg2.Error) as error:
        logger.error("Failed to insert record into mobile table", error)
        ret = False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            logger.info("PostgreSQL connection is closed")
        return ret

@embrace
def updateTable(mobileId: str, price):
    """update value in table

    Args:
        mobileId (str): table name
        price : value of field in table
    """
    try:
        connection = psycopg2.connect(database=postgres_config['postgresql']['db'],
                                        host=postgres_config['postgresql']['host'],
                                        user=postgres_config['postgresql']['user'],
                                        password=postgres_config['postgresql']['passwd'],
                                        port=postgres_config['postgresql']['port'])

        cursor = connection.cursor()

        logger.info("Table Before updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (mobileId,))
        record = cursor.fetchone()
        logger.info(record)

        # Update single record now
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.execute(sql_update_query, (price, mobileId))
        connection.commit()
        # count = cursor.rowcount

        logger.info("Table After updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (mobileId,))
        record = cursor.fetchone()
        logger.info(record)

    except (Exception, psycopg2.Error) as error:
        logger.exception("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            logger.info("PostgreSQL connection is closed")

@embrace
def import_data(columns:tuple, data:tuple, table_name:str):
    try:
        logger.info('data to insert\n{}'.format(data))
        postgres_insert_query = """ INSERT INTO {} ({}) VALUES ({})""".format(table_name,
                                                                              ",".join(columns),
                                                                              ", ".join(["%s"]*len(columns)))
        logger.info(postgres_insert_query)
        connection = psycopg2.connect(database=postgres_config['postgresql']['db'],
                                    host=postgres_config['postgresql']['host'],
                                    user=postgres_config['postgresql']['user'],
                                    password=postgres_config['postgresql']['passwd'],
                                    port=postgres_config['postgresql']['port'])
        cursor = connection.cursor()
        cursor.execute(postgres_insert_query, data)
        connection.commit()
        logger.info("Import data successfully")
    except (Exception, psycopg2.Error) as error:
        logger.exception("Failed to insert record into mobile table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            logger.info("PostgreSQL connection is closed")

@embrace
def create_table_price_board(table_name:str, postgres_config:dict):
    logger.info("create table {}".format(table_name))
    sql = PostGresql.CREATE_PRICE_BOARD_TABLE.value.replace('__TABLE_NAME__', table_name)
    logger.info(sql)
    execute_sql(sql, postgres_config)

if __name__ == "__main__":
    if not check_table_exists(table_name='fpt_price_board'):
        create_table_price_board('fpt_price_board', postgres_config)
    else:
        import_data(columns = ('cp', 'fv', 'mav', 'nstv', 'nstp', 'rsi', 'macdv', 'macdsignal',
                                'tsignal', 'avgsignal', 'ma20', 'ma50', 'ma100', 'session', 'mw3d',
                                'mw1m', 'mw3m', 'mw1y', 'rs3d', 'rs1m', 'rs3m', 'rs1y', 'rsavg', 'hp1m',
                                'hp3m', 'hp1y', 'lp1m', 'lp3m', 'lp1y', 'hp1yp', 'lp1yp', 'pe', 'pb',
                                'roe', 'oscore', 'av', 'bv', 'ev', 'hmp', 'mscore', 'delta1m',
                                'delta1y', 'vnipe', 'vnipb', 'vnid3d', 'vnid1m', 'vnid3m', 'vnid1y'),
                    data=tuple(price_board_stock(Tech.FPT)._values[0][1:]),
                    table_name='fpt_price_board')
