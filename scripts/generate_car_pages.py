#!/usr/bin/env python3
"""
Generate static car pages for the Le Mans 2026 Viewer
"""

import json
import os
from pathlib import Path

# Project directory
PROJECT_DIR = Path("/root/.hermes/workspace/projects/lemans-2026-viewer")
DATA_DIR = PROJECT_DIR / "data"
HTML_DIR = PROJECT_DIR

def generate_car_page(car, bios):
    """Generate a static HTML page for a car"""
    
    # Get tech specs
    tech_specs = {
        'Toyota GR010 Hybrid': {'chassis': 'Toyota GR010 (LMH)', 'engine': '3.5L V6 twin-turbo', 'hybrid': 'Yes (Toyota H8909)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Michelin', 'weight': '~1030 kg'},
        'Ferrari 499P': {'chassis': 'Ferrari 499P (LMH)', 'engine': '3.0L V6 twin-turbo (F163)', 'hybrid': 'Yes (spec MGU)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Goodyear', 'weight': '~1030 kg'},
        'Peugeot 9X8': {'chassis': 'Peugeot 9X8 (LMH)', 'engine': '2.6L V6 twin-turbo', 'hybrid': 'Yes (spec MGU)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Michelin', 'weight': '~1030 kg'},
        'BMW M Hybrid V8': {'chassis': 'BMW M Hybrid V8 (LMH, Dallara-derived)', 'engine': 'modified LMP2-class V8', 'hybrid': 'Yes (spec MGU)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Michelin', 'weight': '~1030 kg'},
        'Alpine A424': {'chassis': 'Alpine A424 (LMH)', 'engine': '3.4L V6 twin-turbo (Mecachrome)', 'hybrid': 'Yes (spec MGU)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Michelin', 'weight': '~1030 kg'},
        'Aston Martin Valkyrie': {'chassis': 'Aston Martin Valkyrie (LMH)', 'engine': '6.5L V12 NA (Cosworth)', 'hybrid': 'No (KERS removed 2025)', 'power': '~510 kW / 700 PS', 'bop': 'TBD', 'tyres': 'Michelin', 'weight': '~1030 kg'},
        'Cadillac V-Series.R': {'chassis': 'Cadillac V-Series.R (LMH, Dallara body)', 'engine': '5.5L V8 twin-turbo', 'hybrid': 'Yes (spec MGU)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Goodyear', 'weight': '~1030 kg'},
        'Genesis GMR-001': {'chassis': 'Genesis GMR-001 (LMH, Oreca-derived)', 'engine': 'modified LMP2-class V8', 'hybrid': 'Yes (spec MGU)', 'power': '500 kW / 680 PS', 'bop': 'TBD', 'tyres': 'Michelin', 'weight': '~1030 kg'},
        'Oreca 07 - Gibson': {'chassis': 'Oreca 07 (LMP2 spec)', 'engine': 'Gibson GK428 4.2L V8 NA', 'hybrid': 'No', 'power': '~440 kW / 600 PS', 'bop': 'Class-fixed (no BoP)', 'tyres': 'Goodyear', 'weight': '~950 kg'},
        'Aston Martin Vantage AMR GT3 Evo': {'chassis': 'Aston Martin Vantage GT3', 'engine': '4.0L V8 twin-turbo', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
        'BMW M4 GT3 Evo': {'chassis': 'BMW M4 GT3', 'engine': '3.0L I6 twin-turbo (P58)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
        'Chevrolet Corvette Z06 GT3.R': {'chassis': 'Corvette Z06 GT3', 'engine': '5.5L V8 NA (LT6)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
        'Ferrari 296 GT3 Evo': {'chassis': 'Ferrari 296 GT3', 'engine': '3.0L V6 twin-turbo (F163)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Pirelli', 'weight': '~1300 kg'},
        'Ford Mustang GT3 Evo': {'chassis': 'Ford Mustang GT3', 'engine': '5.0L V8 NA (Coyote-derived)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
        'Lexus RC F GT3': {'chassis': 'Lexus RC F GT3', 'engine': '5.0L V8 NA (2UR-GSE)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
        'McLaren 720S GT3 Evo': {'chassis': 'McLaren 720S GT3', 'engine': '4.0L V8 twin-turbo (M840T)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Pirelli', 'weight': '~1300 kg'},
        'Mercedes-AMG GT3 Evo': {'chassis': 'Mercedes-AMG GT3', 'engine': '6.2L V8 NA (M159)', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
        'Porsche 911 GT3 R (992.2)': {'chassis': 'Porsche 911 GT3 R', 'engine': '4.2L flat-6 NA', 'hybrid': 'No', 'power': '~415 kW / 565 PS', 'bop': 'Class BoP', 'tyres': 'Goodyear', 'weight': '~1300 kg'},
    }
    
    # Find tech specs
    tech = {'chassis': '—', 'engine': '—', 'hybrid': '—', 'power': '—', 'bop': '—', 'tyres': '—', 'weight': '—'}
    if car.get('car'):
        for key, specs in tech_specs.items():
            if key in car['car']:
                tech = specs
                break
    
    # Get driver info
    drivers = car.get('final_drivers', []) or [car.get('driver_1', ''), car.get('driver_2', ''), car.get('driver_3', '')]
    drivers = [d for d in drivers if d and d.strip() and d != 'TBA']
    
    # Generate driver cards HTML
    driver_cards_html = ''
    for driver_name in drivers:
        bio = bios.get(driver_name, {})
        rating = (bio.get('rating', 'gold') or 'gold').lower()
        stars = ''.join(['<span style="color:#fbbf24">★</span>'] * len(bio.get('le_mans_years', []))) or '—'
        
        # Driver stats
        driver_stats_html = ''
        if bio.get('le_mans_wins') or bio.get('le_mans_years') or bio.get('starts') or bio.get('podiums'):
            driver_stats_html = f'''
                <div class="driver-stats">
                  <div>
                    <div class="driver-stat-num">{bio.get('le_mans_wins', 0)}</div>
                    <div class="driver-stat-label">Wins</div>
                  </div>
                  <div>
                    <div class="driver-stat-num">{len(bio.get('le_mans_years', []))}</div>
                    <div class="driver-stat-label">Starts</div>
                  </div>
                  <div>
                    <div class="driver-stat-num">{bio.get('podiums', 0)}</div>
                    <div class="driver-stat-label">Podiums</div>
                  </div>
                  <div>
                    <div class="driver-stat-num">{bio.get('poles', 0)}</div>
                    <div class="driver-stat-label">Poles</div>
                  </div>
                </div>
            '''
        
        driver_cards_html += f'''
          <div class="driver-card">
            <div class="driver-header">
              <div>
                <div class="driver-name">{driver_name}</div>
                <div class="driver-meta">
                  {f'<span>{bio.get("country", "")}</span>' if bio.get("country") else ''}
                  {f'<span>{bio.get("series", "")}</span>' if bio.get("series") else ''}
                  {f'<span>{stars}</span>' if stars != '—' else ''}
                </div>
              </div>
              <div class="driver-rating rating-{rating}">{rating.upper()}</div>
            </div>
            {driver_stats_html}
            <div class="driver-narrative">
              <p>{bio.get("narrative", "No narrative available.")}</p>
            </div>
          </div>
        '''
    
    if not driver_cards_html:
        driver_cards_html = '<div class="driver-card"><p style="color: #6b6b7b;">Crew TBA</p></div>'
    
    # Build the page
    grid = f'P{car.get("grid_pos")}' if car.get("grid_pos") else '—'
    final_position = f'P{car.get("final_position")}' if car.get("final_position") else '—'
    final_laps = car.get("final_laps", "—")
    final_time = car.get("final_time", "—")
    livery = car.get("livery_color", "#888")
    
    # Car image section
    car_image_html = ''
    if car.get("image_url"):
        car_image_html = f'''
      <div class="section">
        <div class="section-title">Car Image</div>
        <div style="text-align: center; margin-bottom: 1.5rem;">
          <img src="{car["image_url"]}" alt="{car.get("car", "Car")}" style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #1f1f1f;">
        </div>
      </div>
        '''
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0">
<title>Car Detail — 24H Le Mans 2026</title>
<meta name="theme-color" content="#000000">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #000000; --bg-card: #111111; --bg-card-hover: #1a1a1a;
  --border: #1f1f1f; --border-light: #2a2a2a;
  --fg: #f0f0fa; --fg-dim: #a0a0b0; --fg-muted: #6b6b7b;
  --accent: #dc2626;
  --hypercar: #dc2626; --lmp2: #2563eb; --lmp2-proam: #7c3aed; --lmgt3: #16a34a;
  --gold: #fbbf24; --silver: #d1d5db; --bronze: #a16207;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: var(--bg); color: var(--fg); font-family: 'Inter', -apple-system, sans-serif; -webkit-font-smoothing: antialiased; }}
body {{ min-height: 100vh; padding-bottom: 4rem; }}

.container {{ max-width: 1100px; margin: 0 auto; padding: 0 1.25rem; }}

/* === HEADER === */
.car-header {{
  position: relative; padding: 2rem 0 1.5rem; border-bottom: 1px solid var(--border);
  background: radial-gradient(ellipse 70% 60% at 30% 0%, {livery}40, transparent 70%);
}}
.back-link {{
  display: inline-block; font-size: 0.75rem; font-weight: 600;
  color: var(--fg-muted); text-transform: uppercase; letter-spacing: 0.12em;
  text-decoration: none; margin-bottom: 1.5rem; padding: 0.4rem 0.8rem;
  border: 1px solid var(--border); border-radius: 100px;
  transition: all 0.2s;
}}
.back-link:hover {{ color: var(--fg); border-color: var(--border-light); }}
.car-num-display {{
  display: flex; align-items: center; gap: 1.25rem; margin-bottom: 0.75rem;
}}
.car-num {{
  font-size: 3.5rem; font-weight: 900; letter-spacing: -0.04em;
  line-height: 1; font-variant-numeric: tabular-nums;
  color: {livery};
}}
.car-class-badge {{
  display: inline-block; font-size: 0.7rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  padding: 0.35rem 0.7rem; border-radius: 100px;
  background: var(--class-bg, var(--bg-card));
  color: var(--class-color, var(--fg));
  border: 1px solid var(--class-color, var(--border));
}}
.car-position {{
  display: inline-block; font-size: 0.8rem; font-weight: 700;
  color: var(--fg-dim); margin-left: 0.5rem;
}}
.car-team {{
  font-size: 1.5rem; font-weight: 800; letter-spacing: -0.01em;
  margin-bottom: 0.4rem;
}}
.car-full-name {{
  font-size: 0.95rem; color: var(--fg-dim); letter-spacing: 0.02em;
}}

/* === SECTION TITLE === */
.section {{ padding: 2rem 0; }}
.section-title {{
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.18em;
  color: var(--fg-muted); text-transform: uppercase;
  margin-bottom: 1rem;
  display: flex; align-items: center; gap: 0.5rem;
}}
.section-title::before {{
  content: ''; width: 4px; height: 14px; background: var(--accent);
  border-radius: 2px;
}}

/* === CAR DEEP-DIVE === */
.spec-grid {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem; margin-bottom: 1.5rem;
}}
.spec-card {{
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 12px; padding: 1.1rem 1.25rem;
  border-left: 2px solid var(--border-light);
}}
.spec-label {{
  font-size: 0.65rem; font-weight: 700; letter-spacing: 0.15em;
  color: var(--fg-muted); text-transform: uppercase; margin-bottom: 0.4rem;
}}
.spec-value {{
  font-size: 1rem; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25;
}}
.spec-sub {{
  font-size: 0.8rem; color: var(--fg-dim); margin-top: 0.3rem; line-height: 1.4;
}}

/* === DRIVERS === */
.drivers-grid {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}}
.driver-card {{
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 12px; padding: 1.25rem 1.4rem;
}}
.driver-header {{
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 0.75rem;
}}
.driver-name {{
  font-size: 1.05rem; font-weight: 800; letter-spacing: -0.01em;
  margin-bottom: 0.2rem;
}}
.driver-meta {{
  font-size: 0.75rem; color: var(--fg-dim);
  display: flex; gap: 0.5rem; flex-wrap: wrap;
}}
.driver-rating {{
  display: inline-flex; align-items: center; gap: 0.3rem;
  font-size: 0.65rem; font-weight: 700; letter-spacing: 0.1em;
  text-transform: uppercase; padding: 0.25rem 0.55rem;
  border-radius: 100px;
  border: 1px solid;
}}
.rating-platinum {{ color: #e5e7eb; border-color: #6b7280; background: rgba(107, 114, 128, 0.1); }}
.rating-gold {{ color: var(--gold); border-color: var(--gold); background: rgba(251, 191, 36, 0.05); }}
.rating-silver {{ color: var(--silver); border-color: var(--silver); background: rgba(209, 213, 219, 0.05); }}
.rating-bronze {{ color: var(--bronze); border-color: var(--bronze); background: rgba(161, 98, 7, 0.05); }}

.driver-stats {{
  display: flex; gap: 1rem; margin: 0.75rem 0; padding: 0.6rem 0;
  border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
  font-size: 0.7rem;
}}
.driver-stat-num {{ font-size: 1.3rem; font-weight: 800; line-height: 1; }}
.driver-stat-label {{ font-size: 0.6rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--fg-muted); }}

.driver-bio {{
  font-size: 0.85rem; line-height: 1.55; color: var(--fg-dim);
  margin: 0.5rem 0 0.75rem;
}}
.driver-narrative {{
  background: var(--bg-elev, rgba(255,255,255,0.02));
  border-left: 2px solid var(--accent);
  padding: 0.6rem 0.8rem;
  font-size: 0.8rem; line-height: 1.55; color: var(--fg);
  font-style: italic; border-radius: 0 6px 6px 0;
  margin-top: 0.5rem;
}}
.driver-narrative::before {{
  content: 'Race narrative · ';
  font-style: normal;
  font-size: 0.6rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--accent);
  display: block; margin-bottom: 0.3rem;
}}

/* === FOOTER === */
.footer {{
  text-align: center; padding: 2rem 1rem; color: var(--fg-muted);
  font-size: 0.75rem; border-top: 1px solid var(--border); margin-top: 2rem;
}}
.footer a {{ color: var(--fg-dim); text-decoration: none; margin: 0 0.5rem; }}

/* === ERROR === */
.error-state {{
  text-align: center; padding: 4rem 1rem; color: var(--fg-dim);
}}
.error-state a {{ color: var(--accent); }}

/* === MOBILE === */
@media (max-width: 600px) {{
  .car-num {{ font-size: 2.75rem; }}
  .container {{ padding: 0 1rem; }}
  .car-team {{ font-size: 1.2rem; }}
  .drivers-grid {{ grid-template-columns: 1fr; }}
}}

@media (prefers-reduced-motion: reduce) {{
  * {{ transition: none !important; }}
}}
</style>
</head>
<body>

<div class="container">
  <header class="car-header">
    <div class="container">
      <a href="./" class="back-link">← Standings</a>
      <div class="car-num-display">
        <div class="car-num">{car.get("car_number_display", car.get("car_number", ""))}</div>
        <div>
          <div class="car-team">{car.get("team", "")}</div>
          <div class="car-full-name">{car.get("car", "")}</div>
        </div>
      </div>
    </div>
  </header>
  
  <main class="container">
    {car_image_html}
    
    <div class="section">
      <div class="section-title">Race Results</div>
      <div class="spec-grid">
        <div class="spec-card">
          <div class="spec-label">Final Position</div>
          <div class="spec-value">{final_position}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Laps Completed</div>
          <div class="spec-value">{final_laps}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Time/Gap</div>
          <div class="spec-value">{final_time}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Status</div>
          <div class="spec-value">{car.get("final_status", "—")}</div>
        </div>
      </div>
    </div>
    
    <div class="section">
      <div class="section-title">Car Deep-Dive</div>
      <div class="spec-grid">
        <div class="spec-card">
          <div class="spec-label">Chassis</div>
          <div class="spec-value">{tech["chassis"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Engine</div>
          <div class="spec-value">{tech["engine"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Hybrid</div>
          <div class="spec-value">{tech["hybrid"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Power</div>
          <div class="spec-value">{tech["power"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Min Weight</div>
          <div class="spec-value">{tech["weight"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">BoP</div>
          <div class="spec-value">{tech["bop"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Tyres</div>
          <div class="spec-value">{tech["tyres"]}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Series</div>
          <div class="spec-value">{car.get("series", "—")}</div>
        </div>
        <div class="spec-card">
          <div class="spec-label">Qualifying (best)</div>
          <div class="spec-value">{car.get("qual_time", "—")}</div>
        </div>
      </div>
    </div>
    
    <div class="section">
      <div class="section-title">Drivers ({len(drivers)})</div>
      <div class="drivers-grid">{driver_cards_html}</div>
    </div>
  </main>
  
  <footer class="footer">
    <div class="container">
      <div>
        <a href="./">Standings</a>·
        <a href="./classes.html">Classes</a>·
        <a href="./regulations.html">Regulations</a>·
        <a href="./history.html">History</a>
      </div>
    </div>
  </footer>
</div>

</body>
</html>'''
    
    return html_content

def generate_all_car_pages():
    """Generate static HTML pages for all cars"""
    
    # Load data
    with open(DATA_DIR / "entry-list.json", 'r') as f:
        entry_list = json.load(f)
    
    with open(DATA_DIR / "driver-bios.json", 'r') as f:
        driver_bios = json.load(f)
    
    # Generate a page for each car
    for car in entry_list.get('cars', []):
        car_number = car.get('car_number')
        if car_number:
            html_content = generate_car_page(car, driver_bios)
            filename = f"car-{car_number}.html"
            with open(HTML_DIR / filename, 'w') as f:
                f.write(html_content)
            print(f"Generated {filename}")
    
    print("All car pages generated successfully!")

if __name__ == "__main__":
    generate_all_car_pages()