# Bot de Trading para MT5 y Telegram

Este es un bot de trading que se conecta a MetaTrader 5 (MT5) y envía señales de trading a un canal de Telegram. El bot está diseñado para operar en el par **XAUUSD (Oro)** y utiliza una estrategia de scalping basada en el **RSI** y el **ATR**.

---

## Características Principales

- **Conexión a MT5**: Se conecta a MetaTrader 5 para obtener datos de mercado en tiempo real.
- **Señales de Trading**: Genera señales de compra/venta basadas en el RSI y el ATR.
- **Notificaciones en Telegram**: Envía señales a un canal de Telegram con detalles de entrada, stop loss y take profit.
- **Gestión de Riesgo**: Calcula automáticamente el stop loss y take profit basado en el ATR.

---

## Requisitos

- **Python 3.8+**: El bot está escrito en Python.
- **MetaTrader 5**: Necesitas una cuenta en MT5 (demo o real).
- **Cuenta de Telegram**: Para recibir las señales en un canal o chat.
- **Librerías**:
  - `MetaTrader5`
  - `python-telegram-bot`
  - `pandas`
  - `python-dotenv`

---

## Instalación

Sigue estos pasos para instalar y ejecutar el bot:

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/mt5_telegram_bot.git
   cd mt5_telegram_bot