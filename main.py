"""import time
import logging
import pandas as pd
from datetime import datetime
from connections.mt5_connection import connect_to_mt5, get_market_data
from connections.telegram_connection import send_telegram_message
from strategies.scalping import generate_signal
from config.env_vars import SYMBOL
from config.config import TIME_FRAMES

# Configuración de logs
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    if not connect_to_mt5():
        return
    
    # Mensaje de inicio
    data_1m = get_market_data(SYMBOL, TIME_FRAMES["M1"])
    current_price = data_1m['close'].iloc[-1]
    send_telegram_message(f"🚀 Bot Iniciado - {SYMBOL}\n📈 Precio Actual: {current_price}")
    
    while True:
        try:
            # Obtener datos de 1 minuto y 5 minutos
            data_1m = get_market_data(SYMBOL, TIME_FRAMES["M1"])
            data_5m = get_market_data(SYMBOL, TIME_FRAMES["M5"])
            
            # Generar señales
            signal_1m, atr_1m = generate_signal(data_1m)
            signal_5m, atr_5m = generate_signal(data_5m)
            
            # Enviar señales
            if signal_1m:
                message = f"🟢 Señal {signal_1m} (1M)\nPar: {SYMBOL}\nEntrada: {data_1m['close'].iloc[-1]}\nATR: {atr_1m}"
                send_telegram_message(message)
            
            if signal_5m:
                message = f"🔴 Señal {signal_5m} (5M)\nPar: {SYMBOL}\nEntrada: {data_5m['close'].iloc[-1]}\nATR: {atr_5m}"
                send_telegram_message(message)
            
            # Esperar 1 minuto antes de la siguiente iteración
            time.sleep(60 - datetime.now().second)
        
        except Exception as e:
            logging.error(f"Error general: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()

"""
#funciona bien 

import time
import logging
import pandas as pd
from datetime import datetime
from connections.mt5_connection import connect_to_mt5, get_market_data
from connections.telegram_connection import send_telegram_message
from strategies.scalping import generate_signal
from config.env_vars import SYMBOL
from config.config import TIME_FRAMES

# Configuración de logs
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_sl_tp(entry_price, atr, signal):
    
    #Calcula el Stop Loss (SL) y Take Profit (TP) basado en el ATR.
    
    if signal == 'BUY':
        sl = entry_price - atr * 1.5  # Stop Loss
        tp = entry_price + atr * 3    # Take Profit
    elif signal == 'SELL':
        sl = entry_price + atr * 1.5  # Stop Loss
        tp = entry_price - atr * 3    # Take Profit
    else:
        return None, None
    return sl, tp

def main():
    if not connect_to_mt5():
        return
    
    # Mensaje de inicio
    data_1m = get_market_data(SYMBOL, TIME_FRAMES["M1"])
    current_price = data_1m['close'].iloc[-1]
    send_telegram_message(f"🚀 Bot Iniciado - {SYMBOL}\n📈 Precio Actual: {current_price}")
    
    while True:
        try:
            # Obtener datos de 1 minuto y 5 minutos
            data_1m = get_market_data(SYMBOL, TIME_FRAMES["M1"])
            data_5m = get_market_data(SYMBOL, TIME_FRAMES["M5"])
            # Verificar datos
            print("Datos de 1 minuto:")
            print(data_1m.tail())  # Mostrar las últimas filas

            print("Datos de 5 minutos:")
            print(data_5m.tail())  # Mostrar las últimas filas
            
            # Generar señales
            signal_1m, atr_1m = generate_signal(data_1m)
            signal_5m, atr_5m = generate_signal(data_5m)
            
            # Enviar señales con SL y TP
            if signal_1m:
                entry_price_1m = data_1m['close'].iloc[-1]
                sl_1m, tp_1m = calculate_sl_tp(entry_price_1m, atr_1m, signal_1m)
                emoji = '🟢' if signal_1m == 'BUY' else '🔴'
                message = (
                    f"{emoji} Señal {signal_1m} (1M)\n"
                    f"Par: {SYMBOL}\n"
                    f"Entrada: {entry_price_1m:.5f}\n"
                    f"SL: {sl_1m:.5f}\n"
                    f"TP: {tp_1m:.5f}"
                )
                send_telegram_message(message)
            
            if signal_5m:
                entry_price_5m = data_5m['close'].iloc[-1]
                sl_5m, tp_5m = calculate_sl_tp(entry_price_5m, atr_5m, signal_5m)
                emoji = '🟢' if signal_5m == 'BUY' else '🔴'
                message = (
                    f"{emoji} Señal {signal_5m} (5M)\n"
                    f"Par: {SYMBOL}\n"
                    f"Entrada: {entry_price_5m:.5f}\n"
                    f"SL: {sl_5m:.5f}\n"
                    f"TP: {tp_5m:.5f}"
                )
                send_telegram_message(message)
            
            # Esperar 1 minuto antes de la siguiente iteración
            time.sleep(60 - datetime.now().second)
        
        except Exception as e:
            logging.error(f"Error general: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()

