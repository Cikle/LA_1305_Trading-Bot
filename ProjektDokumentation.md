1305 Trading Bot mit API

Cyril Lutziger, Julius Burlet
Datum	Version	Zusammenfassung
01.05.2024	0.0.1	Beginn des Projekts, Recherche zu NoSQL-Datenbanken und der ccxt-Bibliothek für den Trading-Bot.
08.05.2024	0.0.2	Grundlegende Funktionen des Trading-Bots implementiert, API-Anbindung getestet.
15.05.2024	0.0.3	Integration der EMA-Indikatoren, erste Handelsstrategien getestet.
22.05.2024	0.0.4	Optimierung der Handelsstrategien, Probleme bei der Feinabstimmung identifiziert.
29.05.2024	1.0.0	Projekt abgeschlossen, alle Backend-Funktionalitäten erfolgreich implementiert.
1 Informieren
1.1 Ihr Projekt

In diesem Projekt haben wir einen Trading-Bot entwickelt, der die EMA (Exponential Moving Average) von 9 und 21 verwendet und über eine API in Python und die ccxt-Bibliothek angebunden ist. Ziel war es, einen automatisierten Handelsbot zu erstellen, der auf Basis von EMA-Indikatoren Entscheidungen trifft.
1.2 User Stories
US-№	Verbindlichkeit	Typ	Beschreibung
1	Muss	Funktional	Als Benutzer möchte ich API-Schlüssel konfigurieren können, um Zugang zur Handelsplattform zu erhalten.
2	Muss	Funktional	Als Benutzer möchte ich Handelsparameter festlegen können, um die Handelsstrategien anzupassen.
3	Muss	Funktional	Als Benutzer möchte ich, dass der Bot auf Basis der EMA-Indikatoren automatisch Handelsaufträge ausführt.
4	Können	Qualität	Als Benutzer möchte ich, dass der Bot in einem Docker-Container läuft, um die Bereitstellung zu erleichtern.
5	Können	Qualität	Als Benutzer möchte ich eine einfache Benutzeroberfläche zur Überwachung der Handelsaktivitäten.
1.3 Testfälle
TC-№	Ausgangslage	Eingabe	Erwartete Ausgabe
1.1	API-Schlüssel konfiguriert	--	Erfolgreiche Verbindung zur Handelsplattform
2.1	Handelsparameter konfiguriert	--	Parameter gespeichert und verwendet
3.1	EMA-Indikatoren implementiert	--	Automatischer Handel basierend auf EMA-Indikatoren
4.1	Docker-Container eingerichtet	--	Bot läuft stabil in Docker-Umgebung
5.1	GUI zur Überwachung eingerichtet	--	Echtzeit-Anzeige der Handelsaktivitäten
1.4 Diagramme

2 Planen
AP-№	Frist	Zuständig	Beschreibung	geplante Zeit
1.A	08.05.24	Cyril	Recherche zu NoSQL-Datenbanken und ccxt-Bibliothek	60'
1.B	08.05.24	Julius/Cyril	Grundlegende API-Anbindung implementieren	120'
2.A	15.05.24	Julius/Cyril	Implementierung der EMA-Indikatoren	180'
2.B	15.05.24	Julius	Erste Handelsstrategien entwickeln und testen	120'
3.A	22.05.24	Cyril	Handelsstrategien optimieren	240'
3.B	22.05.24	Julius	API-Integration verfeinern	120'
4.A	29.05.24	Julius/Cyril	Endgültige Tests und Fehlerbehebung	180'
5.A	29.05.24	Cyril	Bereitstellung in Docker-Umgebung	60'
3 Entscheiden

Wir haben uns für diese User Stories und Aufgaben entschieden, weil sie die grundlegenden Funktionen eines Trading-Bots abdecken und eine solide Grundlage für zukünftige Erweiterungen bieten. Die Implementierung der EMA-Indikatoren und die Nutzung der ccxt-Bibliothek waren zentrale Bestandteile unserer technischen Entscheidung.
4 Realisieren
AP-№	Datum	Zuständig	geplante Zeit	tatsächliche Zeit
1.A	08.05.24	Cyril	60'	50'
1.B	08.05.24	Julius/Cyril	120'	130'
2.A	15.05.24	Julius/Cyril	180'	200'
2.B	15.05.24	Julius	120'	110'
3.A	22.05.24	Cyril	240'	250'
3.B	22.05.24	Julius	120'	130'
4.A	29.05.24	Julius/Cyril	180'	190'
5.A	29.05.24	Cyril	60'	50'
5 Kontrollieren
5.1 Testprotokoll
TC-№	Datum	Resultat	Tester
1.1	15.05.24	OK	Cyril
2.1	15.05.24	OK	Julius
3.1	22.05.24	OK	Julius
4.1	29.05.24	OK	Cyril
5.1	29.05.24	OK	Julius

Alle Funktionen wurden erfolgreich getestet und implementiert.
6 Auswerten
Was lief gut in unserem Projekt?

    Die Zusammenarbeit im Team war effizient und konstruktiv.
    Die API-Anbindung und die Grundfunktionen des Trading-Bots konnten schnell und zuverlässig umgesetzt werden.
    Die Implementierung und Tests der Backend-Funktionalitäten verliefen weitgehend reibungslos.

Was lief nicht gut in unserem Projekt?

    Die Feinabstimmung der Handelsstrategien erwies sich als komplexer und zeitaufwändiger als ursprünglich geplant.
    Die Integration der Börsen-APIs stellte eine unerwartete Herausforderung dar und führte zu Verzögerungen im Projektablauf.

Schlussbemerkungen

Obwohl das Projekt insgesamt erfolgreich war, wurden wir durch die Komplexität der Handelsstrategien und die Integration der Börsen-APIs herausgefordert. Diese Erfahrungen werden uns helfen, zukünftige Projekte besser zu planen und umzusetzen.
Demonstration

Wir haben einen Testcode erstellt, um sicherzustellen, dass die API Anfragen korrekt gesendet werden und ein Trade erfolgreich eingegangen und wieder geschlossen wird.

python

import os
import ccxt

# Retrieve API keys from environment variables
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
if not api_key or not api_secret:
    raise ValueError("API key and secret must be set")

# Set up the Binance Futures exchange connection using ccxt
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'options': {
        'defaultType': 'future',  # Enable futures trading
    },
    'enableRateLimit': True,
    'adjustForTimeDifference': True,  # Automatically adjust for time difference
})

def set_leverage(symbol, leverage):
    try:
        exchange.set_leverage(leverage, symbol)
        print(f"Leverage set to {leverage}x for {symbol}.")
    except Exception as e:
        print(f"Error setting leverage: {e}")

def get_min_trade_amount(symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        min_notional = 5.1  # Minimum notional value in USD for DOGE/USDT with buffer
        min_trade_amount = min_notional / ticker['last']
        return min_trade_amount
    except Exception as e:
        print(f"Error fetching minimum trade amount: {e}")
        return None

def test_binance_connection():
    try:
        # Fetch account balance
        balance = exchange.fetch_balance()
        print("Balance fetched successfully.")
        print(balance)
        
        # Set leverage for the trading pair to 1
        symbol = 'DOGE/USDT'
        leverage = 1  # No leverage
        set_leverage(symbol, leverage)
        
        # Calculate minimum trade amount
        min_trade_amount = get_min_trade_amount(symbol)
        if min_trade_amount is None:
            print("Could not determine minimum trade amount.")
            return
        print(f"Minimum trade amount for {symbol}: {min_trade_amount}")
        
        # Ensure the trade amount meets the $5 notional requirement
        ticker = exchange.fetch_ticker(symbol)
        min_trade_amount = max(min_trade_amount, 5.5 / ticker['last'])  # Ensure it's above $5 with buffer
        print(f"Adjusted trade amount for {symbol}: {min_trade_amount}")
        
        # Open a long position with the minimum trade amount
        order = exchange.create_market_buy_order(symbol, min_trade_amount)
        print("Buy order executed successfully.")
        print(order)
        
        # Close the position by selling the same amount
        sell_order = exchange.create_market_sell_order(symbol, min_trade_amount)
        print("Sell order executed successfully.")
        print(sell_order)
        
    except Exception as e:
        print(f"Error during Binance connection test: {e}")

# Execute the test function
test_binance_connection()

Was ist in diesem Code enthalten?

    API-Schlüsselverwaltung: Sorgt dafür, dass API-Schlüssel sicher aus Umgebungsvariablen abgerufen werden.
    Leverage-Einstellung: Ermöglicht das Setzen von Hebelwirkungen auf Handelspaare.
    Mindesthandelsbetrag: Berechnet den Mindesthandelsbetrag basierend auf aktuellen Marktpreisen.
    Verbindungs- und Handelsprüfung: Führt einen Test durch, um sicherzustellen, dass eine Verbindung zu Binance hergestellt werden kann, und führt einen vollständigen Handelszyklus (Kauf und Verkauf) durch.
