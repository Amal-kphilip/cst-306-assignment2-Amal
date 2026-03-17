"""
Airline Flight Scheduling - Minimum Fuel Cost
Algorithm: Kruskal's MST (Greedy) | Time: O(E log E)
"""

AIRPORTS = {
    "DEL": "New Delhi", "BOM": "Mumbai", "BLR": "Bengaluru",
    "MAA": "Chennai",   "CCU": "Kolkata", "HYD": "Hyderabad",
    "COK": "Kochi",     "AMD": "Ahmedabad"
}

ROUTES = [
    ("DEL","BOM",85), ("DEL","AMD",55), ("DEL","CCU",90), ("DEL","HYD",75),
    ("BOM","BLR",60), ("BOM","HYD",50), ("BOM","AMD",40), ("BOM","COK",70),
    ("BLR","MAA",30), ("BLR","HYD",45), ("BLR","COK",55), ("MAA","HYD",48),
    ("MAA","CCU",80), ("MAA","COK",35), ("CCU","HYD",95), ("HYD","COK",65),
    ("AMD","BLR",72),
]

# Union-Find
parent = {n: n for n in AIRPORTS}
rank   = {n: 0  for n in AIRPORTS}

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry: return False
    if rank[rx] < rank[ry]: rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]: rank[rx] += 1
    return True

# Kruskal's MST
sorted_routes = sorted(ROUTES, key=lambda r: r[2])
mst, skipped  = [], []
for edge in sorted_routes:
    (mst if union(edge[0], edge[1]) else skipped).append(edge)
    if len(mst) == len(AIRPORTS) - 1: break

total = sum(c for _, _, c in mst)

# Output
D = "-" * 60
lines = [
    "=" * 60,
    "  AIRLINE FLIGHT SCHEDULING — MINIMUM FUEL COST",
    "  Algorithm : Kruskal's MST | Complexity: O(E log E)",
    "=" * 60,

    "\n[1] AIRPORTS",
    D,
    *[f"  {c}  {n}" for c, n in sorted(AIRPORTS.items())],

    "\n[2] ALL ROUTES",
    D,
    f"  {'#':<4} {'From':<6} {'To':<6} {'Cost (Rs.000s)'}",
    D,
    *[f"  {i:<4} {a:<6} {b:<6} Rs.{c:,}" for i,(a,b,c) in enumerate(ROUTES,1)],

    "\n[3] ROUTES CONSIDERED (Sorted Order)",
    D,
    f"  {'Rank':<5} {'From':<6} {'To':<6} {'Cost':>10}  {'Status'}",
    D,
    *[f"  {i:<5} {a:<6} {b:<6} {'Rs.'+str(c):>10}  {'SELECTED' if any((a==x and b==y) or (a==y and b==x) for x,y,_ in mst) else 'Skipped'}"
      for i,(a,b,c) in enumerate(sorted_routes,1)],

    "\n[4] OPTIMAL SCHEDULE (MST)",
    D,
    f"  {'Leg':<4} {'From':<6} {'To':<6} {'From Airport':<20} {'To Airport':<20} {'Cost':>10}",
    D,
    *[f"  {i:<4} {a:<6} {b:<6} {AIRPORTS[a]:<20} {AIRPORTS[b]:<20} Rs.{c:,}"
      for i,(a,b,c) in enumerate(mst,1)],
    D,
    f"  Legs: {len(mst)}  |  Airports: {len(AIRPORTS)}  |  Skipped: {len(skipped)}",
    f"  TOTAL MINIMUM FUEL COST : Rs.{total:,},000",
    D,

    "\n[5] SKIPPED ROUTES (Create Cycles)",
    D,
    *[f"  {a} -> {b}  Rs.{c:,}  (creates cycle)" for a,b,c in skipped],

    "\n[6] COMPLEXITY ANALYSIS",
    D,
    f"  Sort routes      : O(E log E)  <- dominant",
    f"  Union-Find ops   : O(E * a(V)) ~ O(E)",
    f"  Build MST        : O(V)",
    f"  TOTAL            : O(E log E)  where E={len(ROUTES)}, V={len(AIRPORTS)}",
    "=" * 60,
]

report = "\n".join(lines)
print(report)

with open("flight_schedule_output.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("\nSaved: flight_schedule_output.txt")
