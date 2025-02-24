import duckdb

csv_file = "/Users/kazuhisafukuda/dev/duckdb-minio/data/csv/amazon_stock_data/*.csv"


def peek():
    """
    最初の5行を取得する
    """
    conn = duckdb.connect()
    query = f"""
        SELECT 
            *
        FROM read_csv_auto('{csv_file}')
        LIMIT 5
    """
    return conn.sql(query).show()
