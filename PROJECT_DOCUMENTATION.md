# QSK Tajweed Website - Projekt Dokumentation

## 📋 Projekt Übersicht

**Projekt**: QSK Tajweed Website  
**Zweck**: Landing Page für Quran Tajweed Online-Kurs von Marcel Krass  
**Zielgruppe**: Deutsche Muslime, die Tajweed lernen möchten  
**Framework**: StoryBrand 2.0 Marketing Framework  

---

## 🌐 Live URLs

- **GitHub Repository**: https://github.com/dercryptomuslim/qsk-tajweed-website
- **Live Website (Vercel)**: https://qsk-tajweed-website.vercel.app
- **Bewerbungsseite**: https://qsk-tajweed-website.vercel.app/application.html
- **Lokaler Server**: http://localhost:8000

---

## 📁 Dateistruktur

```
/qsk-tajweed-website/
├── index.html                  # Hauptseite (Landing Page)
├── application.html            # Bewerbungsformular (8 Schritte)
├── impressum.html             # Impressum (vorhanden)
├── datenschutz.html           # Datenschutz (vorhanden)
├── assets/                    # Alle Bilder
│   ├── hintergrundtajweed.jpg # Hero Background
│   ├── marcel.png             # Marcel Krass Foto
│   ├── qsktajweedlogo.png     # Logo horizontal
│   └── qsktajweedlogoübereinander.png # Logo vertikal
└── PROJECT_DOCUMENTATION.md   # Diese Datei
```

---

## 🎨 Design & Branding

### Farbschema
```css
--primary-color: #006e9e      /* Blau primär */
--secondary-color: #0094d3    /* Blau sekundär */ 
--accent-color: #FFD700       /* Gold für CTAs */
--text-dark: #333             /* Dunkler Text */
--background-light: #f8f9fa   /* Heller Hintergrund */
```

### Schriftarten
- **Primary**: 'Montserrat' (Google Fonts)
- **Fallback**: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif

### Logo & Bilder
- **Hauptlogo**: qsktajweedlogo.png (Header)
- **Footer Logo**: qsktajweedlogoübereinander.png
- **Marcel Foto**: marcel.png (Hero Section)
- **Background**: hintergrundtajweed.jpg

---

## 📄 Seitenstruktur

### Hauptseite (index.html)

1. **Header** - Sticky Navigation mit Logo und CTAs
2. **Hero Section** - Problem/Solution mit Marcel Foto
3. **Video Section** - Vimeo Video Einbettung
4. **Trustpilot Section** - Echtes Trustpilot Widget
5. **Problem Section** - Schmerzpunkte der Zielgruppe
6. **Solution Section** - Transformation Vision
7. **Method Section** - 3 Hauptvorteile
8. **Steps Section** - 3-Schritte-Plan
9. **Contact Section** - E-Mail Kontaktformular
10. **Footer** - Links und rechtliche Seiten

### Bewerbungsseite (application.html)

**8-stufiger Bewerbungsprozess:**
1. Persönliche Daten (Name, E-Mail, Telefon)
2. Aktuelles Tajweed-Level (4 Optionen)
3. Lernziele (Multiple Choice)
4. Herausforderungen (Multiple Choice)
5. Zeitinvestition (4 Optionen)
6. Vorerfahrung (Textfeld)
7. Motivation (5 Optionen)
8. Zusätzliche Informationen

---

## 🎯 StoryBrand Framework Implementation

### 1. Character (Kunde)
- Deutsche Muslime
- Wollen Quran richtig rezitieren
- Frustriert von bisherigen Lernmethoden

### 2. Problem
- **Externe**: Falsche Aussprache, stockende Rezitation
- **Interne**: Unsicherheit, Frust, spirituelle Distanz
- **Philosophisch**: Nicht der Muslim sein, der man sein möchte

### 3. Guide (Marcel Krass)
- **Empathie**: "Ich war selbst an diesem Punkt"
- **Autorität**: 10+ Jahre Erfahrung, 1000+ Schüler, zertifiziert
- **Methode**: Speziell für deutsche Muttersprachler entwickelt

### 4. Plan (3 Schritte)
1. **Kostenloses Gespräch** - Situation analysieren
2. **Methode anwenden** - Strukturiert lernen
3. **Schön rezitieren** - Ziel erreichen

### 5. Call to Action
- **Primary**: "Bewirb dich jetzt für den Kurs"
- **Transitional**: Kostenloses Gespräch/Video anschauen

### 6. Success Vision
- Selbstbewusste Rezitation
- Spirituelle Verbindung
- Respekt in der Gemeinde

### 7. Failure Consequences
- Weiterhin unsicher bleiben
- Spirituelle Distanz
- Verpasste Chancen

---

## 🔧 Technische Details

### Trustpilot Integration
```javascript
Business Unit ID: 53T9sGC6Sik937Xh
Template ID: 5419b6a8b0d04a076446a9ad
Locale: de-DE
Profile URL: https://de.trustpilot.com/review/qsk-tajweed.de
```

### Vimeo Video
```
Video ID: 1069593257
Einstellungen: title=0&byline=0&portrait=0&badge=0
Responsive: 16:9 Aspect Ratio
```

### Kontaktformular
- **Methode**: mailto-Link
- **E-Mail**: info@example.com (placeholder)
- **Funktion**: Öffnet lokales E-Mail-Programm

### Responsive Breakpoints
```css
Mobile: max-width: 768px
Tablet: max-width: 968px  
Small Mobile: max-width: 480px
```

---

## 📊 Conversion Optimierung

### CTAs Hierarchie
1. **Primary**: "Bewirb dich jetzt für den Kurs" (Bewerbungsseite)
2. **Secondary**: Video anschauen, kostenloses Gespräch
3. **Tertiary**: Kontaktformular

### Urgency & Scarcity
- Begrenzte Plätze
- Zeitliche Begrenzung
- Nächster Kurs erst später

### Social Proof
- 1000+ erfolgreiche Schüler
- 98% Erfolgsrate
- Trustpilot Bewertungen
- Testimonials

### Trust Signals
- Zertifizierungen
- Geld-zurück-Garantie
- Lebenslanger Zugang
- Persönliches Zertifikat

---

## 🚀 Deployment & Hosting

### GitHub Repository
- **Owner**: dercryptomuslim
- **Repo**: qsk-tajweed-website
- **Branch**: main
- **Auto-Deploy**: Ja (Vercel Integration)

### Vercel Hosting
- **Auto-Deploy**: Bei jedem Git Push
- **Domain**: qsk-tajweed-website.vercel.app
- **SSL**: Automatisch
- **CDN**: Global

### Lokale Entwicklung
```bash
cd /Users/mustafaali/qsk-tajweed-website
python3 -m http.server 8000
# Öffne: http://localhost:8000
```

---

## 📝 Content Management

### Haupttexte (Deutsch)
- **Headline**: "Tajweed meistern – und den Quran jeden Tag genießen"
- **Subline**: "Einfach, flexibel und Schritt für Schritt"
- **Problem**: "Die stille Gefahr: ein kaltes Herz ohne Quran"
- **Solution**: "So sieht dein neues Leben aus..."

### Testimonials
- Ahmed, 28 Jahre
- Fatima, 35 Jahre  
- Yusuf, 42 Jahre
- Alle mit 5-Sterne-Bewertung

### Keywords/SEO
- Tajweed lernen
- Quran rezitieren
- Marcel Krass
- Online Kurs
- Deutsche Muslime

---

## 🔄 Git Workflow

### Wichtige Commits
- `986073a`: Initial commit (Original Version)
- `458b0a5`: Bewerbungsseite hinzugefügt
- `968613f`: Trustpilot Integration

### Branch Strategy
- **main**: Production Branch
- **development**: Feature Entwicklung (wenn nötig)

### Commit Conventions
```
feat: Neue Features
fix: Bug Fixes
docs: Dokumentation
style: Design Änderungen
refactor: Code Refactoring
```

---

## 📞 Kontakt & Externe Services

### E-Mail Konfiguration
- **Kontakt**: info@example.com (zu aktualisieren)
- **Support**: Über Kontaktformular
- **Bewerbungen**: Über application.html

### Trustpilot Account
- **Business Unit**: 53T9sGC6Sik937Xh
- **Domain**: qsk-tajweed.de
- **Status**: Aktiv

### Vimeo Account
- **Video ID**: 1069593257
- **Titel**: "Lesehack Landingpage"
- **Einbettung**: Erlaubt

---

## 🐛 Bekannte Issues & TODOs

### Aktueller Status: ✅ VOLLSTÄNDIG
- [x] Landing Page erstellt
- [x] Bewerbungsformular implementiert
- [x] StoryBrand Framework angewandt
- [x] Trustpilot integriert
- [x] Responsive Design
- [x] Live Deployment

### Zukünftige Erweiterungen
- [ ] E-Mail-Integration für Bewerbungen
- [ ] Analytics (Google Analytics/Hotjar)
- [ ] A/B Testing Setup
- [ ] Newsletter-Anmeldung
- [ ] Blog/Ressourcen Sektion
- [ ] Multi-language Support
- [ ] Payment Integration

### Wartung
- [ ] Regelmäßige Trustpilot Updates
- [ ] Content Updates basierend auf Performance
- [ ] SEO Optimierung
- [ ] Performance Monitoring

---

## 🔧 Entwickler Notizen

### Wichtige Code-Bereiche

1. **StoryBrand Texte**: Leicht zu finden über Kommentare
2. **Trustpilot Widget**: Separates Script am Ende
3. **Responsive Design**: Mobile-First Approach
4. **Form Validation**: JavaScript in application.html
5. **Smooth Scrolling**: Native CSS implementation

### Performance Optimierungen
- Bilder optimiert
- CSS minimiert (inline)
- JavaScript komprimiert
- Vimeo lazy loading
- HTTP/2 Ready

### Browser Support
- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+
- Mobile iOS/Android

---

## 📈 Analytics & Tracking

### Zu implementieren
```javascript
// Google Analytics 4
gtag('config', 'GA_MEASUREMENT_ID');

// Facebook Pixel  
fbq('init', 'PIXEL_ID');

// Hotjar Tracking
hj('trigger', 'form_submission');
```

### Conversion Events
- Bewerbungsformular gestartet
- Bewerbungsformular abgeschlossen  
- Video angeschaut (>50%)
- Kontaktformular verwendet
- Trustpilot-Link geklickt

---

## 🚨 Backup & Recovery

### Git Backup
- **Remote**: GitHub (automatisch)
- **Lokal**: /Users/mustafaali/qsk-tajweed-website
- **Vercel**: Automatische Backups

### Rollback Strategy
```bash
# Zu spezifischem Commit zurück
git reset --hard COMMIT_HASH
git push --force origin main

# Notfall: Zur ursprünglichen Version
git reset --hard 986073a
```

### Asset Backup
- Alle Bilder in /assets/ Ordner
- Hochauflösende Originale separat sichern
- Logo-Variationen verfügbar

---

**Letztes Update**: 24. September 2025  
**Version**: 1.2.0  
**Status**: Production Ready ✅

---

*Diese Dokumentation sollte bei jeder größeren Änderung aktualisiert werden.*