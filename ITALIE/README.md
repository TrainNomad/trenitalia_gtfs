# Trenitalia GTFS Auto-Builder

Génère un feed GTFS depuis l'API lefrecce.it, mis à jour automatiquement chaque jour via GitHub Actions.

## Télécharger le dernier GTFS

```bash
curl -L https://github.com/<USER>/<REPO>/releases/download/latest-gtfs/trenitalia_gtfs.zip -o gtfs.zip
```

**Fichiers inclus** dans `gtfs/trenitalia_it_api/` :

| Fichier | Contenu |
|---|---|
| `agency.txt` | Trenitalia |
| `routes.txt` | FR · FA · FB · IC · ICN · EC · EN |
| `trips.txt` | Un voyage par train × jour |
| `stop_times.txt` | Horaires HH:MM:SS par arrêt |
| `stops.txt` | Gares + coordonnées GPS |
| `calendar.txt` | Service par date exacte |
| `feed_info.txt` | Métadonnées du feed |

## Utilisation locale

```bash
node build-trenitalia-gtfs.js --days 30 --out ./gtfs/trenitalia_it_api
```

Options :
- `--days N` : fenêtre de jours à crawler (défaut 30)
- `--out ./path` : dossier de sortie
- `--dry-run` : affiche les stats sans écrire de fichiers
- `--verbose` : logs détaillés

## Architecture

```
GitHub Actions (cron 03:00 UTC)
  └─ node build-trenitalia-gtfs.js
       └─ API lefrecce.it (POST /website/ticket/solutions)
            └─ gtfs/trenitalia_it_api/*.txt
                 └─ trenitalia_gtfs.zip → GitHub Release "latest-gtfs"
                      └─ Ton backend télécharge via URL stable
```
