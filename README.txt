README
feed_the_great_old_ones is the primary feeding mechanism of rlyeh.
download data, calculate price derivative data

init:
1 time per day at (16:00:05 PM CST)


main:

download data
    Things to gather
    OHLC, Date, Settle (If Different from close)
    Things to add/compute
    symbol, 30 Day Vol, 30 Day VVOL, hull MA, 9 day MA, 11 Day MA, 18 Day MA

and store it to sql, csv:
    mysql
    pandas.to_csv
    pandas.to_sql

upload sql to database(make it editable),
    database: feed_the_great_old_ones
    pword: viperv1
    table: dataframe (symbol)
    csv file_path:

Download portfolio data and weights, including initial investment
