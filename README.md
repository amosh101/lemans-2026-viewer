# 🏁 24 Hours of Le Mans 2026 Viewer

A static, mobile-friendly viewer for the 2026 24 Hours of Le Mans race weekend.

## 🌐 Access

**Live URL:** http://100.91.143.50:8083/?v=lemans1 (Tailscale-only)

## 📱 Pages

1. **Home** (`index.html`) - Race status card + 3 class cards + standings tables (RACE/CHAMPIONSHIP toggle)
2. **Car Detail** (`car.html`) - Tap any car # for full deep-dive (tech specs + 3-driver narrative)
3. **Classes** (`classes.html`) - Hypercar / LMP2 / LMGT3 breakdown with entry tables
4. **Regulations** (`regulations.html`) - LMH vs LMDh comparison, BoP, 2026 rule changes
5. **History** (`history.html`) - 11 years of winners (2015-2025)

## 📁 Data Files

- `data/entry-list.json` - 62 cars, livery colors, grid positions, driver crews
- `data/championship.json` - WEC standings (Hypercar manufacturers, LMGT3 teams)
- `data/history.json` - 11 years winners
- `data/regulations.json` - LMH/LMDh tech specs
- `data/driver-bios.json` - 30+ driver bios + narratives
- `data/race-card.json` - Race status (in_progress, finished, etc)

## ⏰ Cron Jobs

1. **Live Timing** - `0 13-16 13-14 6 *` (hourly during race Sat 14:00 UTC → Sun 16:00 UTC)
2. **Post-Race Results** - `0 16 14 6 *` (+1hr after race end Sun 16:00 UTC)
3. **Monday Re-run** - `0 6 15 6 *` (in case results drop later)

## 🛠️ Scripts

- `scripts/refresh_live_timing.py` - Hourly live timing scraper
- `scripts/post_race_results.py` - Post-race results scraper (+1hr and Monday re-run)
- `scripts/test-ios.mjs` - Playwright iOS WebKit test

## 🧪 Testing

```bash
# Run Playwright iOS test
cd scripts
node test-ios.mjs
```

## 🚀 Deployment

The site is served via Python's built-in HTTP server:

```bash
cd /root/.hermes/workspace/projects/lemans-2026-viewer
python3 -m http.server 8083 --bind 100.91.143.50
```

## 📝 Notes

- All internal links use `?v=lemans1` to bust Safari cache
- Live timing and post-race results currently use mock data (JS walls on fiawec.com / RaceMonitor)
- Ready for real data sources when they become available