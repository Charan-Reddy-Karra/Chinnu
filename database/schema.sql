CREATE TABLE IF NOT EXISTS stocks (
    symbol TEXT PRIMARY KEY,
    exchange TEXT NOT NULL,
    company_name TEXT,
    sector TEXT,
    industry TEXT,
    market_cap REAL,
    active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_prices (
    symbol TEXT NOT NULL,
    trade_date DATE NOT NULL,

    open REAL,
    high REAL,
    low REAL,
    close REAL,

    volume INTEGER,
    delivery_pct REAL,

    source TEXT,

    PRIMARY KEY (symbol, trade_date)
);

CREATE TABLE IF NOT EXISTS scores (
    symbol TEXT NOT NULL,
    score_date DATE NOT NULL,

    structure_score REAL,
    rs_score REAL,
    quality_score REAL,
    sponsorship_score REAL,
    risk_score REAL,

    overall_score REAL,
    confidence REAL,

    PRIMARY KEY (symbol, score_date)
);

CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symbol TEXT NOT NULL,
    alert_date DATE NOT NULL,

    overall_score REAL,
    confidence REAL,

    entry_price REAL,
    stop_price REAL,

    status TEXT DEFAULT 'OPEN'
);

CREATE TABLE IF NOT EXISTS outcomes (
    alert_id INTEGER PRIMARY KEY,

    return_30d REAL,
    return_60d REAL,
    return_90d REAL,
    return_180d REAL,

    max_drawdown REAL,

    FOREIGN KEY(alert_id) REFERENCES alerts(id)
);

CREATE INDEX IF NOT EXISTS idx_prices_symbol
ON daily_prices(symbol);

CREATE INDEX IF NOT EXISTS idx_prices_date
ON daily_prices(trade_date);

CREATE INDEX IF NOT EXISTS idx_scores_symbol
ON scores(symbol);

CREATE INDEX IF NOT EXISTS idx_scores_date
ON scores(score_date);
