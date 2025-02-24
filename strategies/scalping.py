import pandas as pd
from config.config import STRATEGY_PARAMS

def calculate_rsi(df, period=14):
    """
    Calcula el RSI.
    """
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_atr(df, period=14):
    """
    Calcula el ATR.
    """
    high_low = df['high'] - df['low']
    high_close = abs(df['high'] - df['close'].shift())
    low_close = abs(df['low'] - df['close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(period).mean()

def generate_signal(df):
    """
    Genera señales de compra/venta basadas en RSI y ATR.
    """
    rsi = calculate_rsi(df, STRATEGY_PARAMS["rsi_period"])
    atr = calculate_atr(df, STRATEGY_PARAMS["atr_period"])
    
    if rsi.iloc[-1] < STRATEGY_PARAMS["oversold"]:
        return 'BUY', atr.iloc[-1]
    elif rsi.iloc[-1] > STRATEGY_PARAMS["overbought"]:
        return 'SELL', atr.iloc[-1]
    return None, None