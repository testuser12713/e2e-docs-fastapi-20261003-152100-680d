# Notiz-API

Eine kleine REST-API in Python mit FastAPI und Pydantic v2. Sie verwaltet Notizen
(id, titel, inhalt, tags, erstellt_am) in einem In-Memory-Speicher – ganz ohne
Datenbank. Notizen lassen sich anlegen, auflisten (optional nach Tag gefiltert),
per ID abrufen und löschen.

## Tech-Stack

- **Sprache**: Python
- **Framework**: FastAPI
- **Validierung**: Pydantic v2
- **Konfiguration**: pydantic-settings
- **Speicher**: In-Memory (keine Datenbank)
- **Tests**: pytest + FastAPI TestClient

## Installation

```bash
pip install -e .
```

## Starten (Entwicklung)

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Die API ist dann unter `http://localhost:8000` erreichbar. Die interaktive
OpenAPI-Dokumentation liegt unter `http://localhost:8000/docs`.

## Endpunkte

| Methode | Pfad          | Beschreibung                                   |
| ------- | ------------- | ---------------------------------------------- |
| GET     | `/health`     | Health-Check, liefert `{"status": "ok"}`       |
| POST    | `/notes`      | Legt eine Notiz an (Body: `NoteCreate`)        |
| GET     | `/notes`      | Listet Notizen auf (optional `?tag=<str>`)     |
| GET     | `/notes/{id}` | Ruft eine Notiz per ID ab                       |
| DELETE  | `/notes/{id}` | Löscht eine Notiz per ID                        |

### Modelle

- `Note`: `{ id: int, titel: str, inhalt: str, tags: list[str], erstellt_am: datetime }`
- `NoteCreate`: `{ titel: str (1–100 Zeichen), inhalt: str, tags: list[str] (max. 5, Default []) }`

## Tests

```bash
pytest
```
