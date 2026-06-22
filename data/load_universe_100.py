from database.db import get_connection

symbols = [
'RELIANCE','TCS','HDFCBANK','ICICIBANK','INFY','SBIN','BHARTIARTL',
'LT','ITC','HINDUNILVR','AXISBANK','BAJFINANCE','KOTAKBANK',
'SUNPHARMA','MARUTI','TITAN','ULTRACEMCO','ASIANPAINT','NTPC',
'POWERGRID','ADANIENT','ADANIPORTS','ADANIGREEN','WIPRO','TECHM',
'HCLTECH','ONGC','COALINDIA','TATAMOTORS','M&M','BEL','HAL',
'DLF','LODHA','GODREJPROP','INDHOTEL','IRCTC','BSE','MCX',
'POLYCAB','DIXON','PERSISTENT','LTIM','NAUKRI','PIDILITIND',
'ABB','SIEMENS','CUMMINSIND','BOSCHLTD','CGPOWER','APLAPOLLO',
'SHREECEM','AMBUJACEM','ACC','TRENT','DMART','VBL','COLPAL',
'BRITANNIA','NESTLEIND','TATACONSUM','INDIGO','ZYDUSLIFE',
'DRREDDY','CIPLA','TORNTPHARM','MANKIND','AUROPHARMA',
'BANKBARODA','PNB','CANBK','UNIONBANK','INDUSINDBK',
'CHOLAFIN','SHRIRAMFIN','RECLTD','PFC','SRF',
'DEEPAKNTR','PIIND','AARTIIND','COROMANDEL','UPL',
'OBEROIRLTY','PRESTIGE','PHOENIXLTD','JSWSTEEL',
'TATASTEEL','HINDALCO','JINDALSTEL','SAIL','VEDL',
'IOC','BPCL','HAVELLS','CGCL','MOTHERSON',
'KPITTECH','COFORGE'
]

conn = get_connection()

conn.execute("DELETE FROM universe")

for s in symbols:

    conn.execute(
        """
        INSERT INTO universe
        (
            symbol,
            priority,
            active
        )
        VALUES (?,1,1)
        """,
        (s,)
    )

conn.commit()

count = conn.execute(
    """
    SELECT COUNT(*)
    FROM universe
    """
).fetchone()[0]

print("Universe:", count)

conn.close()
