# routes/populate_data.py - USE THIS VERSION TO MATCH THE TREE IMAGE
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airport_system.settings') 
django.setup()

from routes.models import Airport, FlightRoute

def run():
    print("⚠️  Cleaning old data to match image (One-Way Tree) exactly...")
    FlightRoute.objects.all().delete()
    Airport.objects.all().delete()

    print("🚀 Starting data population...")

    # --- 1. Create Airports (Nodes: A, B, C) ---
    airport_a = Airport.objects.create(code='A')
    airport_b = Airport.objects.create(code='B')
    airport_c = Airport.objects.create(code='C')
    print(f"Created Airports: {airport_a.code}, {airport_b.code}, {airport_c.code}")

    # --- 2. Create Routes (Edges: A -> B, A -> C ONLY) ---
    
    # 🛫 Route 1: A -> B (Left, 150 km)
    FlightRoute.objects.create(
        source=airport_a,
        destination=airport_b,
        direction='LEFT',
        distance_km=150,
        duration_mins=150 
    )
    print("Created Route: A -> left -> B (150 mins)")

    # 🛫 Route 2: A -> C (Right, 250 km)
    FlightRoute.objects.create(
        source=airport_a,
        destination=airport_c,
        direction='RIGHT',
        distance_km=250,
        duration_mins=250
    )
    print("Created Route: A -> right -> C (250 mins)")
    
    # DO NOT ADD B->A or C->A to force the visualization into a one-way tree.

    print("✅ Data population complete. Database reflects the one-way tree image.")

if __name__ == '__main__':
    run()