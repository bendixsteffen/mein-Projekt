# Textanalyse mit CI/CD-Pipeline

## Was macht das Projekt?
Eine kleine Python-Bibliothek zur Textanalyse (Wörter zählen, Zeichen zählen, häufigste Wörter). Die Anwendung ist bewusst klein und dient als Testfall für eine vollständige CI/CD-Pipeline mit GitHub Actions.

## Pipeline im Überblick
| Job | Zweck | Trigger / Bedingung | needs | Environment | Artifact |
|---|---|---|---|---|---|
| `test` | Dependencies installieren, Tests ausführen, ZIP-Paket bauen | push und pull_request | – | – | lädt `app-paket` hoch |
| `deploy` | Release mit dem Paket erstellen | nur push auf `main` (`if`) | `test` | `production` | lädt `app-paket` herunter |

Reihenfolge: Pull Request / Push → Test → Build → Artifact → (Freigabe) → Release.

## Trigger
- `push` (alle Branches): Job `test` läuft.
- `pull_request`: Job `test` läuft, `deploy` wird übersprungen.
- Deployment nur bei `push` auf `main` und nur, wenn die Tests grün sind.

## Secrets und Environment
- Secret: `DEPLOY_TOKEN` (Fantasiewert, wird nur über die Länge geprüft, nie ausgegeben)
- Variable: `DEPLOY_TARGET`
- Environment `production`: Required reviewers (manuelle Freigabe), Deployment nur von Branch `main`
- Rechte: global `contents: read`, im Deployment-Job zusätzlich `contents: write` und `actions: read`

## Deployment
Nach grünen Tests und Freigabe lädt der Job `deploy` das Artifact herunter und erstellt mit `gh release create` ein Release `v1.0.<run_number>` mit `app.zip` als Asset. Zu prüfen auf der Seite **Releases** im Repository.

## Lokal ausführen
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pytest -v
mkdir -p build && python -m zipfile -c build/app.zip src/
python -m src.anwendung
```
