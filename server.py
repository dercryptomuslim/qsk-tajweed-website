#!/usr/bin/env python3
"""
QSK Tajweed Website - Lokaler Entwicklungsserver
Startet einen einfachen HTTP-Server zum Testen der Webseite
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

# Konfiguration
PORT = 8000
HOST = "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Erweiterter HTTP-Handler mit besserer Fehlerbehandlung"""
    
    def end_headers(self):
        # CORS-Header für lokale Entwicklung
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Farbige Ausgabe für bessere Lesbarkeit"""
        message = format % args
        if "404" in message:
            print(f"\033[91m{message}\033[0m")  # Rot für 404
        elif "200" in message:
            print(f"\033[92m{message}\033[0m")  # Grün für 200
        else:
            print(message)

def start_server():
    """Startet den lokalen Webserver"""
    
    # Wechsel zum Verzeichnis des Scripts
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    print("\n" + "="*60)
    print("🚀 QSK TAJWEED - LOKALER WEBSERVER")
    print("="*60)
    
    # Versuche den Server zu starten
    try:
        with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
            url = f"http://{HOST}:{PORT}"
            
            print(f"\n✅ Server erfolgreich gestartet!")
            print(f"\n📍 Öffne diese URL in deinem Browser:")
            print(f"   \033[94m{url}\033[0m")
            print(f"\n📁 Serving from: {script_dir}")
            print(f"\n🛑 Zum Beenden: CTRL+C (oder CMD+C auf Mac)")
            print("\n" + "-"*60 + "\n")
            
            # Versuche den Browser automatisch zu öffnen
            try:
                webbrowser.open(url)
                print("🌐 Browser wurde automatisch geöffnet...")
            except:
                print("⚠️  Bitte öffne den Browser manuell mit der obigen URL")
            
            print("\n📊 Server-Logs:\n")
            
            # Server läuft dauerhaft
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Port bereits in Verwendung
            print(f"\n❌ FEHLER: Port {PORT} ist bereits belegt!")
            print(f"   Mögliche Lösungen:")
            print(f"   1. Beende andere lokale Server")
            print(f"   2. Ändere den PORT in dieser Datei")
            print(f"   3. Versuche: lsof -i :{PORT} um zu sehen, was den Port nutzt")
        else:
            print(f"\n❌ FEHLER beim Starten des Servers: {e}")
        sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("👋 Server wurde beendet")
        print("="*60 + "\n")
        sys.exit(0)

if __name__ == "__main__":
    try:
        start_server()
    except Exception as e:
        print(f"\n❌ Unerwarteter Fehler: {e}")
        sys.exit(1)
