import pandas as pd
import numpy as np
import ta

def add_technical_indicators(data):
    # Calculate Relative Strength Index (RSI)
    data['RSI'] = ta.momentum.rsi(data['SP500'], window=14).round(2)

    # Calculate Bollinger Bands
    bb = ta.volatility.BollingerBands(data['SP500'], window=20, window_dev=2)
    data['BB_Upper_Distance'] = ((bb.bollinger_hband() - data['SP500']) / bb.bollinger_hband()).round(4)
    data['BB_Lower_Distance'] = ((data['SP500'] - bb.bollinger_lband()) / bb.bollinger_lband()).round(4)

    return data