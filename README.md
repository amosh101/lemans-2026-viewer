# 🏁 24 Hours of Le Mans Viewer

A comprehensive viewer for the 24 Hours of Le Mans race at Circuit de la Sarthe, featuring real-time updates and historical data.

## 🌐 Access

**Live URL:** http://100.91.143.50:8083/?v=lemans1 (Tailscale-only)

## 📁 Project Structure

```
.
├── index.html              # Home page with standings and race card
├── car.html                # Car detail pages with tech specs and driver info
├── classes.html            # Class breakdown and entry tables
├── regulations.html        # LMH vs LMDh regulations and technical specs
├── history.html            # Historical winners and race history
├── data/                   # JSON data files
│   ├── entry-list.json     # 62-car entry list with real race results
│   ├── championship.json   # WEC standings (Hypercar manufacturers, LMGT3 teams)
│   ├── history.json        # 11 years of Le Mans winners (2015-2025)
│   ├── regulations.json    # LMH/LMDh tech specs and rules
│   ├── driver-bios.json    # 30+ driver bios with race narratives
│   ├── race-card.json      # Race status and information
│   ├── live-timing.json    # Live timing data (updated hourly)
│   └── 2026-results-final.json  # Final race results
└── scripts/                # Automation scripts
    ├── refresh_live_timing.py     # Hourly live timing updates
    ├── post_race_results.py       # Post-race final results processing
    ├── update_website_data.py     # Comprehensive data updater
    ├── update_race_results.py     # Race results data updater
    ├── update_driver_stats.py     # Driver statistics updater
    ├── add_car_images.py          # Car images adder
    └── test-ios.mjs               # Playwright iOS WebKit test
```

## 🔄 Automated Updates

The viewer automatically updates for future Le Mans races at Circuit de la Sarthe:

### Cron Jobs

1. **Live Timing Updates**
   - Runs hourly during race weekends (Saturday 13:00-16:00 UTC)
   - Updates live timing data on the website in real-time
   - Scheduled for June 10-11 each year

2. **Post-Race Results**
   - Runs 1 hour after race end (Sunday 16:00 UTC)
   - Updates final race results on the website
   - Scheduled for June 11 each year

3. **Monday Re-run**
   - Runs Monday at 06:00 UTC to catch any updated official results
   - Ensures website has the most accurate final data
   - Scheduled for June 12 each year

### Data Flow

```
Live Race Data → refresh_live_timing.py → live-timing.json → Website
Final Results → post_race_results.py → 2026-results-final.json → Entry List
```

## 🏆 2026 Race Results

The viewer includes complete results from the 2026 24 Hours of Le Mans:

- **Winner:** Toyota Racing #7 (Mike Conway, Kamui Kobayashi, Nyck de Vries)
- **Final Time:** 24:03:01.030
- **All 62 cars** with final positions, laps completed, and times
- **Driver statistics** including wins, starts, podiums, and pole positions
- **Car images** for visual reference
- **Updated championship standings** through 2026

## 🛠️ Technical Implementation

- **Pure HTML/CSS/JavaScript** - No build step required
- **JSON Data Backend** - Easy to update and maintain
- **Python HTTP Server** - Simple deployment with `python3 -m http.server 8083`
- **Tailscale Only** - Secure internal network access
- **Mobile Responsive** - Works on all devices
- **Cache-Busted URLs** - Ensures fresh content delivery

## 🚀 Deployment

```bash
# Clone the repository
git clone [repository-url]
cd lemans-2026-viewer

# Start the server
python3 -m http.server 8083 --bind 100.91.143.50

# Access at http://100.91.143.50:8083/?v=lemans1
```

## 📅 Future Race Support

The system is designed to automatically support future Le Mans races:

1. **June Race Window** - Cron jobs automatically trigger during race weekends
2. **Real-time Updates** - Live timing data refreshes hourly during races
3. **Post-Race Processing** - Final results automatically updated after each race
4. **Monday Verification** - Official results re-checked on Monday mornings

## 📦 Version Control

This project is managed with Git for version control:

```bash
# View commit history
git log --oneline

# Current commits:
# efed738 Update cron jobs and data system for future Le Mans races
# 0457d25 Initial commit: 24 Hours of Le Mans 2026 Viewer
```

## 📞 Support

For issues or questions, please contact the project maintainer.

---
*Built with ❤️ for motorsport enthusiasts*