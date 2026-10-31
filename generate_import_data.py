
"""Generate synthetic 2025–2026 U.S. import transactions."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
random.seed(42)
# Fictional importer used throughout the synthetic trade scenario.
IMPORTER_NAME = "GaiAnQi Global Trading"
# HTS codes are illustrative and require classification review.
products = [
    ("Steel fasteners", "7318.15.0000", "Steel"),
    ("Aluminum components", "7616.99.5190", "Aluminum"),
    ("Electronic control units", "8537.10.9170", "Electronics"),
    ("Industrial pumps", "8413.70.2004", "Machinery"),
    ("Solar panels", "8541.43.0010", "Solar"),
    ("Industrial batteries", "8507.60.0020", "Batteries"),
]

origins = [
    ("China", "CN"),
    ("Canada", "CA"),
    ("Mexico", "MX"),
    ("Germany", "DE"),
    ("Vietnam", "VN"),
    ("South Korea", "KR"),
]

start_date = date(2025, 1, 1)
end_date = date(2026, 10, 29)
days = (end_date - start_date).days

rows = []

for i in range(1, 151):
    product, hts, category = random.choice(products)
    country, origin_code = random.choice(origins)

    entry_date = start_date + timedelta(
        days=random.randint(0, days)
    )

    rows.append({
        "entry_id": f"ENT-{i:04d}",
        "importer_name": IMPORTER_NAME,
        "entry_date": entry_date.isoformat(),
        "country_of_origin": country,
        "origin_code": origin_code,
        "supplier": f"Supplier-{random.randint(1, 25):02d}",
        "product_description": product,
        "product_category": category,
        "hts_code": hts,
        "entered_value_usd": round(
            random.uniform(15000, 250000), 2
        ),
        "quantity": random.randint(100, 5000),
        "entry_type": "Consumption",
        "review_status": "Pending Review",
    })

output = ROOT / "import_entries.csv"

with output.open("w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=rows[0].keys()
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} synthetic import transactions.")
print(f"Saved to: {output}")
