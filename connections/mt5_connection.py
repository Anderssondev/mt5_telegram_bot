import MetaTrader5 as mt5
import os
from dotenv import load_dotenv
import pandas as pd

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener credenciales desde las variables de entorno
MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

def connect_to_mt5():
    """
    Inicializa y conecta a MetaTrader 5 utilizando las credenciales del archivo .env.
    """
    if not mt5.initialize():
        print("Error al inicializar MT5. Verifica que MT5 esté instalado y funcionando.")
        return False
    
    if not MT5_LOGIN or not MT5_PASSWORD or not MT5_SERVER:
        print("Error: Faltan credenciales en el archivo .env")
        return False
    
    authorized = mt5.login(int(MT5_LOGIN), MT5_PASSWORD, MT5_SERVER)
    if not authorized:
        print(f"Error al conectarse a la cuenta MT5. Código de error: {mt5.last_error()}")
        return False
    
    print("Conectado a MT5 correctamente")
    return True

def get_market_data(symbol, timeframe, n=100):
    """
    Obtiene datos del mercado para el símbolo y timeframe especificados.
    """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)
    if rates is None or len(rates) == 0:
        print(f"Error al obtener datos para {symbol}. Verifica el símbolo y el timeframe.")
        return None
    
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Prueba de conexión y obtención de datos
if __name__ == "__main__":
    if connect_to_mt5():
        symbol = "BTCUSDm"
        timeframe = mt5.TIMEFRAME_M1  # 1 minuto
        data = get_market_data(symbol, timeframe)
        
        if data is not None:
            print("Datos obtenidos correctamente:")
            print(data.head())
    else:
        print("No se pudo conectar a MT5.")



