════════════════════════════════════════════════════════════════════════
  AIRLINE FLIGHT SCHEDULING — MINIMUM FUEL COST OPTIMIZER
  Generated : 2026-03-17  12:58:17
  Algorithm : Kruskal's Minimum Spanning Tree (Greedy)
════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════
  1. REGISTERED AIRPORTS
════════════════════════════════════════════════════════════════════════
  Code    Airport Name                                      
  ──────  ──────────────────────────────────────────────────
  AMD     Sardar Vallabhbhai Patel Intl (Ahmedabad)         
  BLR     Kempegowda Intl (Bengaluru)                       
  BOM     Chhatrapati Shivaji Intl (Mumbai)                 
  CCU     Netaji Subhas Intl (Kolkata)                      
  COK     Cochin Intl (Kochi)                               
  DEL     Indira Gandhi Intl (New Delhi)                    
  HYD     Rajiv Gandhi Intl (Hyderabad)                     
  MAA     Chennai Intl (Chennai)                            

════════════════════════════════════════════════════════════════════════
  2. ALL AVAILABLE ROUTES WITH FUEL COSTS
════════════════════════════════════════════════════════════════════════
  No.   From    To      Fuel Cost (₹ 000s)  
  ────  ──────  ──────  ────────────────────
  1     DEL     BOM     ₹ 85                
  2     DEL     AMD     ₹ 55                
  3     DEL     CCU     ₹ 90                
  4     DEL     HYD     ₹ 75                
  5     BOM     BLR     ₹ 60                
  6     BOM     HYD     ₹ 50                
  7     BOM     AMD     ₹ 40                
  8     BOM     COK     ₹ 70                
  9     BLR     MAA     ₹ 30                
  10    BLR     HYD     ₹ 45                
  11    BLR     COK     ₹ 55                
  12    MAA     HYD     ₹ 48                
  13    MAA     CCU     ₹ 80                
  14    MAA     COK     ₹ 35                
  15    CCU     HYD     ₹ 95                
  16    HYD     COK     ₹ 65                
  17    AMD     BLR     ₹ 72                

  Total routes available : 17

════════════════════════════════════════════════════════════════════════
  3. ROUTES CONSIDERED (Sorted by Fuel Cost — Kruskal Order)
════════════════════════════════════════════════════════════════════════
  Rank   From    To      Fuel Cost (₹ 000s)    Status    
  ─────  ──────  ──────  ────────────────────  ──────────
  1      BLR     MAA     ₹ 30                  ✔ SELECTED
  2      MAA     COK     ₹ 35                  ✔ SELECTED
  3      BOM     AMD     ₹ 40                  ✔ SELECTED
  4      BLR     HYD     ₹ 45                  ✔ SELECTED
  5      MAA     HYD     ₹ 48                  ✘ Skipped 
  6      BOM     HYD     ₹ 50                  ✔ SELECTED
  7      DEL     AMD     ₹ 55                  ✔ SELECTED
  8      BLR     COK     ₹ 55                  ✘ Skipped 
  9      BOM     BLR     ₹ 60                  ✘ Skipped 
  10     HYD     COK     ₹ 65                  ✘ Skipped 
  11     BOM     COK     ₹ 70                  ✘ Skipped 
  12     AMD     BLR     ₹ 72                  ✘ Skipped 
  13     DEL     HYD     ₹ 75                  ✘ Skipped 
  14     MAA     CCU     ₹ 80                  ✔ SELECTED
  15     DEL     BOM     ₹ 85                  ✘ Skipped 
  16     DEL     CCU     ₹ 90                  ✘ Skipped 
  17     CCU     HYD     ₹ 95                  ✘ Skipped 

════════════════════════════════════════════════════════════════════════
  4. OPTIMAL FLIGHT SCHEDULE (Minimum Spanning Tree)
════════════════════════════════════════════════════════════════════════
  Leg   From   →   To     Airport (From)                    Airport (To)                      Fuel (₹ 000s) 
  ────  ─────  ──  ─────  ────────────────────────────────  ────────────────────────────────  ──────────────
  1     BLR    →   MAA    Kempegowda Intl (Bengaluru)       Chennai Intl (Chennai)            ₹ 30          
  2     MAA    →   COK    Chennai Intl (Chennai)            Cochin Intl (Kochi)               ₹ 35          
  3     BOM    →   AMD    Chhatrapati Shivaji Intl (Mumbai)  Sardar Vallabhbhai Patel Intl (Ahmedabad)  ₹ 40          
  4     BLR    →   HYD    Kempegowda Intl (Bengaluru)       Rajiv Gandhi Intl (Hyderabad)     ₹ 45          
  5     BOM    →   HYD    Chhatrapati Shivaji Intl (Mumbai)  Rajiv Gandhi Intl (Hyderabad)     ₹ 50          
  6     DEL    →   AMD    Indira Gandhi Intl (New Delhi)    Sardar Vallabhbhai Patel Intl (Ahmedabad)  ₹ 55          
  7     MAA    →   CCU    Chennai Intl (Chennai)            Netaji Subhas Intl (Kolkata)      ₹ 80          
────────────────────────────────────────────────────────────────────────
  Total Flight Legs    : 7
  Airports Connected   : 8
  Routes Skipped       : 7
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✈  TOTAL MINIMUM FUEL COST :  ₹ 335,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

════════════════════════════════════════════════════════════════════════
  5. SKIPPED ROUTES (Would Create Cycles — Excluded)
════════════════════════════════════════════════════════════════════════
  No.   From    To      Fuel Cost (₹ 000s)    Reason                        
  ────  ──────  ──────  ────────────────────  ──────────────────────────────
  1     MAA     HYD     ₹ 48                  Creates cycle → skipped       
  2     BLR     COK     ₹ 55                  Creates cycle → skipped       
  3     BOM     BLR     ₹ 60                  Creates cycle → skipped       
  4     HYD     COK     ₹ 65                  Creates cycle → skipped       
  5     BOM     COK     ₹ 70                  Creates cycle → skipped       
  6     AMD     BLR     ₹ 72                  Creates cycle → skipped       
  7     DEL     HYD     ₹ 75                  Creates cycle → skipped       

════════════════════════════════════════════════════════════════════════
  6. ALGORITHM ANALYSIS
════════════════════════════════════════════════════════════════════════

  Algorithm Used  : Kruskal's Minimum Spanning Tree
  Strategy        : Greedy — always pick cheapest safe route

  Step-by-step Complexity:
  ┌─────────────────────────────────────────────────────────────┐
  │  Step 1 : Sort all 17 routes by fuel cost   →  O(E log E)  │
  │  Step 2 : Union-Find with path compression   →  O(E · α(V)) │
  │           (α is inverse Ackermann ≈ constant)               │
  │  Step 3 : Select 7 edges for MST         →  O(V)        │
  └─────────────────────────────────────────────────────────────┘

  Overall Time Complexity  :  O(E log E)   [dominant step = sort]
  Overall Space Complexity :  O(V + E)

  Where:
    V = 8   (number of airports)
    E = 17  (number of available routes)

  Why Kruskal's?
  • Perfectly suited for sparse flight networks
  • Naturally greedy — picks minimum-cost routes first
  • Guarantees global minimum spanning tree (optimal schedule)
  • Simple to understand and implement

════════════════════════════════════════════════════════════════════════
  END OF REPORT
════════════════════════════════════════════════════════════════════════
