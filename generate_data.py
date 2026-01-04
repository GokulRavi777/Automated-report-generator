import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data():
    print("Generating dummy data...")
    
    adjectives = ["Global", "Tech", "Dynamic", "Future", "Smart", "Prime", "Elite", "NextGen", "Alpha", "Omega"]
    nouns = ["Systems", "Solutions", "Innovations", "Consulting", "Group", "Enterprises", "Networks", "Labs", "Digital", "Soft"]
    
    services = [
        ("Cloud Migration", 50000, 200000),
        ("AI Implementation", 30000, 150000),
        ("Cybersecurity Audit", 10000, 50000),
        ("Custom ERP Dev", 100000, 500000),
        ("Mobile App Dev", 20000, 80000),
        ("Data Analytics", 25000, 120000),
        ("IT Support Retainer", 5000, 20000),
        ("DevOps setup", 15000, 60000),
        ("Legacy Modernization", 40000, 180000),
        ("Blockchain POC", 20000, 100000)
    ]
    
    data = []
    
    # Randomly pick a "trend" for this data generation run
    # This ensures that each time you run it, the data looks different (e.g. "Cloud" is popular vs "AI" is popular)
    trending_service = random.choice(services)[0] 
    print(f"📈 Trend for this run: {trending_service} is booming!")

    data = []
    
    # Randomize total records (400 to 600)
    total_records = random.randint(400, 600)
    
    for i in range(1, total_records + 1):
        # Create a company name
        comp_name = f"{random.choice(adjectives)} {random.choice(nouns)}"
        
        # Pick a service project (apply bias)
        # 30% chance to pick the "trending" service, otherwise random
        if random.random() < 0.3:
             # Find the trending service tuple
             svc_tuple = next(s for s in services if s[0] == trending_service)
             svc_name, min_amt, max_amt = svc_tuple
        else:
             svc_name, min_amt, max_amt = random.choice(services)
        
        # Date within last year
        # Force some records to be today/recent for "Daily" reports
        if i <= 20: 
             days_ago = 0 # Today
        elif i <= 50:
             days_ago = random.randint(1, 7) # This week
        else:
             days_ago = random.randint(0, 365) # Last year

        date_val = datetime.now() - timedelta(days=days_ago)
        
        row = {
            "customer_id": i,
            "name": comp_name,
            "project_name": f"{svc_name} - {comp_name}",
            "service_type": svc_name,
            "amount": random.randint(min_amt, max_amt),
            "date": date_val.strftime("%Y-%m-%d")
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    # Ensure correct column order for the existing tool, plus new ones
    df = df[["customer_id", "name", "project_name", "service_type", "amount", "date"]]
    
    output_file = "customers.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Generated 500 records in {output_file}")
    
    # Show glimpse
    print(df.head())

if __name__ == "__main__":
    generate_data()
