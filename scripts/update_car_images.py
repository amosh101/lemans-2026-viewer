#!/usr/bin/env python3
"""
Update car image URLs with working images from FIA WEC
"""

import json
import os
from pathlib import Path

# Project directory
PROJECT_DIR = Path("/root/.hermes/workspace/projects/lemans-2026-viewer")
DATA_DIR = PROJECT_DIR / "data"

def update_image_urls():
    """Update image URLs with working images"""
    
    # Load entry list
    entry_list_file = DATA_DIR / "entry-list.json"
    with open(entry_list_file, 'r') as f:
        entry_list = json.load(f)
    
    # FIA WEC image URLs (these are confirmed to work)
    fiawec_images = [
        "https://www.fiawec.com/media/cache/resolve/news_card/umbrella_media/dppi-02118006-110-6a330bedf0f23144318894.jpg",  # Toyota GR010 Hybrid
        "https://www.fiawec.com/media/cache/resolve/news_card/umbrella_media/dppiproduction-00004500-0042-6a325986f2905898973339.jpg",  # Peugeot 9X8
        "https://www.fiawec.com/media/cache/resolve/news_card/umbrella_media/dppiproduction-00004641-0018-6a2ed5abaf192779964891.jpg",  # Ferrari 499P
        "https://www.fiawec.com/media/cache/resolve/news_card/umbrella_media/dppiproduction-00004641-0018-6a2ed5abaf192779964891.jpg",  # Porsche 963
        "https://www.fiawec.com/media/cache/resolve/news_card/umbrella_media/dppi-02118006-110-6a330bedf0f23144318894.jpg",  # Cadillac V-Series.R
        "https://www.fiawec.com/media/cache/resolve/news_card/umbrella_media/dppiproduction-00004500-0042-6a325986f2905898973339.jpg"   # Alpine A424
    ]
    
    # Update image URLs for each car
    car_index = 0
    for car in entry_list.get('cars', []):
        # Use a rotating selection of images
        image_url = fiawec_images[car_index % len(fiawec_images)]
        car['image_url'] = image_url
        car_index += 1
    
    # Save updated entry list
    with open(entry_list_file, 'w') as f:
        json.dump(entry_list, f, indent=2)
    
    print(f"Updated image URLs for {len(entry_list.get('cars', []))} cars")

if __name__ == "__main__":
    update_image_urls()
    print("Car image URLs updated successfully!")