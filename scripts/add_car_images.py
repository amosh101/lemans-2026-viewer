#!/usr/bin/env python3
"""
Add car images to the entry list
"""

import json
import os
from datetime import datetime

# Data directory
DATA_DIR = "/root/.hermes/workspace/projects/lemans-2026-viewer/data"

def add_car_images():
    """Add car images to the entry list"""
    
    # Load existing entry list
    with open(os.path.join(DATA_DIR, "entry-list.json"), "r") as f:
        entry_list = json.load(f)
    
    # Car images mapping (using placeholder URLs for now)
    car_images = {
        # Hypercar class
        "7": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Toyota_GR010_Hybrid_Le_Mans_2021.jpg/800px-Toyota_GR010_Hybrid_Le_Mans_2021.jpg",
        "20": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/BMW_M_Hybrid_V8_Le_Mans_2023.jpg/800px-BMW_M_Hybrid_V8_Le_Mans_2023.jpg",
        "8": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Toyota_GR010_Hybrid_Le_Mans_2021.jpg/800px-Toyota_GR010_Hybrid_Le_Mans_2021.jpg",
        "12": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Cadillac_V-Series.R_Le_Mans_2023.jpg/800px-Cadillac_V-Series.R_Le_Mans_2023.jpg",
        "51": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Ferrari_499P_Le_Mans_2023.jpg/800px-Ferrari_499P_Le_Mans_2023.jpg",
        "35": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Alpine_A424_Le_Mans_2023.jpg/800px-Alpine_A424_Le_Mans_2023.jpg",
        "83": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Ferrari_499P_Le_Mans_2023.jpg/800px-Ferrari_499P_Le_Mans_2023.jpg",
        "007": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Aston_Martin_Valkyrie_AMR-LMH_Le_Mans_2023.jpg/800px-Aston_Martin_Valkyrie_AMR-LMH_Le_Mans_2023.jpg",
        "94": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Peugeot_9X8_Le_Mans_2022.jpg/800px-Peugeot_9X8_Le_Mans_2022.jpg",
        "1": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/BMW_M_Hybrid_V8_Le_Mans_2023.jpg/800px-BMW_M_Hybrid_V8_Le_Mans_2023.jpg",
        "93": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Peugeot_9X8_Le_Mans_2022.jpg/800px-Peugeot_9X8_Le_Mans_2022.jpg",
        "19": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Genesis_GMR-001_Le_Mans_2023.jpg/800px-Genesis_GMR-001_Le_Mans_2023.jpg",
        "009": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Aston_Martin_Valkyrie_AMR-LMH_Le_Mans_2023.jpg/800px-Aston_Martin_Valkyrie_AMR-LMH_Le_Mans_2023.jpg",
        
        # LMP2 class
        "43": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "343": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "29": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "26": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "37": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "28": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "4": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "22": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "17": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "2": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "9": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "10": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "31": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "30": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
        "21": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg",
    }
    
    # Add images to cars
    for car in entry_list["cars"]:
        car_number = str(car["car_number"])
        if car_number in car_images:
            car["image_url"] = car_images[car_number]
        else:
            # Default image for cars without specific images
            car["image_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Oreca_07_Le_Mans_2019.jpg/800px-Oreca_07_Le_Mans_2019.jpg"
    
    # Save updated entry list
    with open(os.path.join(DATA_DIR, "entry-list.json"), "w") as f:
        json.dump(entry_list, f, indent=2)
    
    print("Car images added to entry list")

def main():
    """Main function to add car images"""
    print("Adding car images to entry list...")
    
    add_car_images()
    
    print("Car images added successfully!")

if __name__ == "__main__":
    main()