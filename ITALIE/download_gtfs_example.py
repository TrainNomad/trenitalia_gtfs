# ════════════════════════════════════════════════════════════════════════
# Exemples : télécharger le ZIP GTFS depuis ton backend
# URL stable (ne change jamais même quand le ZIP est mis à jour) :
#
#   https://github.com/<USER>/<REPO>/releases/download/latest-gtfs/trenitalia_gtfs.zip
#
# Remplace <USER>/<REPO> par ton dépôt GitHub.
# ════════════════════════════════════════════════════════════════════════

# ── Python (requests) ────────────────────────────────────────────────────────
import requests, zipfile, io, os

GTFS_URL = "https://github.com/<USER>/<REPO>/releases/download/latest-gtfs/trenitalia_gtfs.zip"

def fetch_gtfs(dest_dir="./gtfs_data"):
    r = requests.get(GTFS_URL, timeout=60, stream=True)
    r.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        z.extractall(dest_dir)
    print(f"GTFS extrait dans {dest_dir}/")
    for f in os.listdir(dest_dir + "/trenitalia_it_api"):
        print(" ", f)

fetch_gtfs()

# ── Node.js (sans dépendance externe) ────────────────────────────────────────
# const https = require('https');
# const fs    = require('fs');
# const path  = require('path');
# const { execSync } = require('child_process');
#
# const GTFS_URL = 'https://github.com/<USER>/<REPO>/releases/download/latest-gtfs/trenitalia_gtfs.zip';
# const ZIP_PATH = '/tmp/trenitalia_gtfs.zip';
# const OUT_DIR  = './gtfs_data';
#
# function downloadFile(url, dest) {
#   return new Promise((resolve, reject) => {
#     const file = fs.createWriteStream(dest);
#     https.get(url, res => {
#       // Suivre les redirects (GitHub redirige vers storage CDN)
#       if (res.statusCode === 301 || res.statusCode === 302) {
#         file.close();
#         return downloadFile(res.headers.location, dest).then(resolve).catch(reject);
#       }
#       res.pipe(file);
#       file.on('finish', () => { file.close(); resolve(); });
#     }).on('error', reject);
#   });
# }
#
# async function fetchGTFS() {
#   console.log('Téléchargement du ZIP GTFS…');
#   await downloadFile(GTFS_URL, ZIP_PATH);
#   fs.mkdirSync(OUT_DIR, { recursive: true });
#   execSync(`unzip -o ${ZIP_PATH} -d ${OUT_DIR}`);
#   console.log('GTFS prêt dans', OUT_DIR);
# }
#
# fetchGTFS().catch(console.error);

# ── curl (shell / Docker entrypoint) ─────────────────────────────────────────
# curl -L \
#   "https://github.com/<USER>/<REPO>/releases/download/latest-gtfs/trenitalia_gtfs.zip" \
#   -o /tmp/gtfs.zip \
#   && unzip -o /tmp/gtfs.zip -d /data/gtfs \
#   && rm /tmp/gtfs.zip
