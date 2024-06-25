# 1305 Trading Bot mit API

Cyril Lutziger, Julius Burlet

| Datum     | Version | Zusammenfassung                                                                 |
|-----------|---------|---------------------------------------------------------------------------------|
| 03.05.2024| 0.0.1   | Beginn des Projekts, Recherche zu der ccxt-Bibliothek für den Trading-Bot. |
| 10.05.2024| 0.0.2   | Grundlegende Funktionen des Trading-Bots implementiert, API-Anbindung getestet.  |
| 17.05.2024| 0.0.3   | Integration der EMA-Indikatoren, erste Handelsstrategien getestet.               |
| 24.05.2024| 0.0.4   | Optimierung der Handelsstrategien, Probleme bei der Feinabstimmung identifiziert.|
| 31.05.2024| 1.0.0   | Projekt abgeschlossen, alle Backend-Funktionalitäten erfolgreich implementiert.  |
| 07.06.2024| 1.1.0   | Implementierung zusätzlicher API-Tests und Verbesserung der Dokumentation.       |
| 14.06.2024| 1.2.0   | Endgültige Überprüfung und Bereitstellung des Projekts.                          |

## 1 Informieren

### 1.1 Ihr Projekt

In diesem Projekt haben wir einen Trading-Bot entwickelt, der die EMA (Exponential Moving Average) von 9 und 21 verwendet und über eine API in Python und die ccxt-Bibliothek angebunden ist. Ziel war es, einen automatisierten Handelsbot zu erstellen, der auf Basis von EMA-Indikatoren Entscheidungen trifft.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ          | Beschreibung                                                         |
|------|-----------------|--------------|----------------------------------------------------------------------|
| 1    | Muss            | Funktional   | Als Benutzer möchte ich API-Schlüssel konfigurieren können, um Zugang zur Handelsplattform zu erhalten. |
| 2    | Muss            | Funktional   | Als Benutzer möchte ich Handelsparameter festlegen können, um die Handelsstrategien anzupassen. |
| 3    | Muss            | Funktional   | Als Benutzer möchte ich, dass der Bot auf Basis der EMA-Indikatoren automatisch Handelsaufträge ausführt. |
| 4    | Können          | Qualität     | Als Benutzer möchte ich, dass der Bot in einem Docker-Container läuft, um die Bereitstellung zu erleichtern. |
| 5    | Können          | Qualität     | Als Benutzer möchte ich eine einfache Benutzeroberfläche zur Überwachung der Handelsaktivitäten. |

### 1.3 Testfälle

| TC-№ | Ausgangslage                  | Eingabe  | Erwartete Ausgabe                                      |
|------|-------------------------------|----------|--------------------------------------------------------|
| 1.1  | API-Schlüssel konfiguriert    | --       | Erfolgreiche Verbindung zur Handelsplattform            |
| 2.1  | Handelsparameter konfiguriert | --       | Parameter gespeichert und verwendet                     |
| 3.1  | EMA-Indikatoren implementiert | --       | Automatischer Handel basierend auf EMA-Indikatoren      |
| 4.1  | Docker-Container eingerichtet | --       | Bot läuft stabil in Docker-Umgebung                     |
| 5.1  | GUI zur Überwachung eingerichtet | --    | Echtzeit-Anzeige der Handelsaktivitäten                 |

### 1.4 Diagramme
Main Project:

![gajnnsdsga](https://github.com/Cikle/LA_1305_Trading-Bot/assets/110893288/704b81ae-d2c8-4418-9743-dc317452d695)

Test Project:

![Test Trading](https://github.com/Cikle/LA_1305_Trading-Bot/assets/110893288/12981236-633c-4e02-aea6-8d6c2585636c)

## 2 Planen

| AP-№ | Frist    | Zuständig      | Beschreibung                                        | geplante Zeit |
|------|----------|----------------|-----------------------------------------------------|---------------|
| 1.A  | 08.05.24 | Cyril          | Recherche zu ccxt-Bibliotheken                      | 60'           |
| 1.B  | 08.05.24 | Julius/Cyril   | Grundlegende API-Anbindung implementieren           | 120'          |
| 2.A  | 15.05.24 | Julius/Cyril   | Implementierung der EMA-Indikatoren                 | 180'          |
| 2.B  | 15.05.24 | Julius         | Erste Handelsstrategien entwickeln und testen       | 120'          |
| 3.A  | 22.05.24 | Cyril          | Handelsstrategien optimieren                        | 240'          |
| 3.B  | 22.05.24 | Julius         | API-Integration verfeinern                          | 120'          |
| 4.A  | 29.05.24 | Julius/Cyril   | Endgültige Tests und Fehlerbehebung                 | 180'          |
| 5.A  | 29.05.24 | Cyril          | Bereitstellung in Docker-Umgebung                   | 60'           |
| 6.A  | 07.06.24 | Julius         | Zusätzliche API-Tests implementieren                | 120'          |
| 6.B  | 14.06.24 | Julius/Cyril   | Endgültige Überprüfung und Dokumentation            | 180'          |

## 3 Entscheiden

Wir haben uns für diese User Stories und Aufgaben entschieden, weil sie die grundlegenden Funktionen eines Trading-Bots abdecken und eine solide Grundlage für zukünftige Erweiterungen bieten. Die Implementierung der EMA-Indikatoren und die Nutzung der ccxt-Bibliothek waren zentrale Bestandteile unserer technischen Entscheidung.

## 4 Realisieren

| AP-№ | Datum    | Zuständig    | geplante Zeit | tatsächliche Zeit |
|------|----------|--------------|---------------|-------------------|
| 1.A  | 08.05.24 | Cyril        | 60'           | 50'               |
| 1.B  | 08.05.24 | Julius/Cyril | 120'          | 130'              |
| 2.A  | 15.05.24 | Julius/Cyril | 180'          | 200'              |
| 2.B  | 15.05.24 | Julius       | 120'          | 110'              |
| 3.A  | 22.05.24 | Cyril        | 240'          | 250'              |
| 3.B  | 22.05.24 | Julius       | 120'          | 130'              |
| 4.A  | 29.05.24 | Julius/Cyril | 180'          | 190'              |
| 5.A  | 29.05.24 | Cyril        | 60'           | 50'               |
| 6.A  | 07.06.24 | Julius       | 120'          | 130'              |
| 6.B  | 14.06.24 | Julius/Cyril | 180'          | 190'              |

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum    | Resultat | Tester  |
|------|----------|----------|---------|
| 1.1  | 15.05.24 | OK       | Cyril   |
| 2.1  | 15.05.24 | OK       | Julius  |
| 3.1  | 22.05.24 | OK       | Julius  |
| 4.1  | 29.05.24 | OK       | Cyril   |
| 5.1  | 29.05.24 | OK       | Julius  |
| 6.1  | 07.06.24 | OK       | Julius  |
| 6.2  | 14.06.24 | OK       | Julius/Cyril |

Alle Funktionen wurden erfolgreich getestet und implementiert.

## 6 Auswerten

### Was lief gut in unserem Projekt?
- Die Zusammenarbeit im Team war effizient und konstruktiv.
- Die API-Anbindung und die Grundfunktionen des Trading-Bots konnten schnell und zuverlässig umgesetzt werden.
- Die Implementierung und Tests der Backend-Funktionalitäten verliefen weitgehend reibungslos.

### Was lief nicht gut in unserem Projekt?
- Die Feinabstimmung der Handelsstrategien erwies sich als komplexer und zeitaufwändiger als ursprünglich geplant.
- Die Integration der Börsen-APIs stellte eine unerwartete Herausforderung dar und führte zu Verzögerungen im Projektablauf.

## Schlussbemerkungen

Obwohl das Projekt insgesamt erfolgreich war, wurden wir durch die Komplexität der Handelsstrategien und die Integration der Börsen-APIs herausgefordert. Diese Erfahrungen werden uns helfen, zukünftige Projekte besser zu planen und umzusetzen.
