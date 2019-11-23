from main import oil, sp500,nsdq,gold,two_year,ten_year,dollar
from sqlalchemy import create_engine
import sqlite3
#engine = create_engine('mysql://root:viperv1@192.168.10.105/feed_the_great_old_ones')
engine = sqlite3.connect('feed_the_great_old_ones')
oil.to_sql('WTI_Front_Month',con = engine,if_exists= 'replace')
sp500.to_sql('SP500',con = engine, if_exists= 'replace')
nsdq.to_sql('NSDQ',con = engine ,if_exists= 'replace')
gold.to_sql('GOLD_Front_Month',con = engine,if_exists= 'replace')
two_year.to_sql('2YR',con = engine,if_exists= 'replace')
ten_year.to_sql('10YR',con = engine,if_exists= 'replace')
dollar.to_sql('USD',con = engine,if_exists= 'replace')
