import os
import subprocess
import sys
import time

def run_job():
    print("🚀 Starting Daily Report Job...")
    
    # 1. Generate new data
    print("\n--- Step 1: Generating New Data ---")
    try:
        # Check if generate_data.py exists
        if os.path.exists("generate_data.py"):
             subprocess.run([sys.executable, "generate_data.py"], check=True)
        else:
             print("⚠️ generate_data.py not found! Skipping data generation.")
    except Exception as e:
        print(f"❌ Error generating data: {e}")
        return

    # 2. Generate Reports
    print("\n--- Step 2: Generating Reports ---")
    try:
        if os.path.exists("report_generator.py"):
            subprocess.run([sys.executable, "report_generator.py"], check=True)
        else:
            print("❌ report_generator.py not found!")
            return
            
    except Exception as e:
        print(f"❌ Error generating reports: {e}")
        return

    print("\n✅ Daily Job Completed Successfully!")

if __name__ == "__main__":
    run_job()
