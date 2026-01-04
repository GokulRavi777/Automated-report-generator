import subprocess
import os
import sys

def create_schedule():
    # The command should run the daily_job.py script
    target_exe = sys.executable
    
    # If running as a script, sys.executable is python.exe
    if "python.exe" in target_exe.lower() or "pythonw.exe" in target_exe.lower():
        script_path = os.path.abspath("daily_job.py")
        cmd = f'"{target_exe}" "{script_path}"'
    else:
        # If running as Frozen EXE, we might need a different strategy, 
        # but for now let's assume we are running from source or the bundled exe handles it.
        # If bundled, we might simply run the executable with a flag that triggers daily_job logic internally
        # OR we assume daily_job is also built as an exe.
        # For simplicity in this context, we'll assume source execution for the fix first.
        script_path = os.path.abspath("daily_job.py") 
        cmd = f'"{target_exe}" "{script_path}"'
    
    # Task Name
    task_name = "AutoReportProject"
    
    # Create task using schtasks
    # Runs daily at 09:00, forcing execution directory to be correct is tricky in schtasks without XML,
    # but since our app finds config relative to itself (or CWD), we rely on it being in the folder.
    # To be safe, we can add a simple wrapper or assumption.
    
    schtasks_cmd = [
        "schtasks", "/create", "/sc", "daily", "/tn", task_name, "/tr", cmd, "/st", "09:00", "/f"
    ]
    
    print(f"Creating task '{task_name}'...")
    print(f"Command: {cmd}")
    
    try:
        result = subprocess.run(schtasks_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Task successfully scheduled.")
        else:
            print("❌ Failed to schedule task.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_schedule()

