# VLC Update Checker

Dette programmet sjekker om det finnes oppdateringer for VLC media player og lagrer informasjon i en SQLite-database.

## Krav

- Python 3.x
- requests
- beautifulsoup4

## Installasjon

1. Installer avhengigheter: pip install requests beautifulsoup4

## Bruk

Kjør scriptet: python vlc_update_checker.py

Programmet vil:

- Hente siste versjon fra VLCs nettside
- Sammenligne med lagret versjon
- Vise melding om oppdatering er tilgjengelig eller ikke
- Oppdatere databasen med siste versjon og tidspunkt

## Database

Programmet bruker 'vlc_updates.db' for å lagre versjon og siste sjekk tidspunkt.