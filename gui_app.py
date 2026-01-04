import tkinter as tk
from tkinter import messagebox, filedialog
import os
import sys
import json
import threading
# Import the logic directly
import report_generator
import daily_job

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def run_reports_thread():
    # Run in a separate thread to keep GUI responsive
    try:
        # Redirect stdout to capture output if needed, or just let it print to console
        report_generator.main()
        messagebox.showinfo("Success", "Reports generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate reports.\n{e}")

def run_reports():
    threading.Thread(target=run_reports_thread).start()

def run_full_pipeline_thread():
    try:
        daily_job.run_job()
        messagebox.showinfo("Success", "Data refreshed and reports generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run daily job.\n{e}")

def run_full_pipeline():
    threading.Thread(target=run_full_pipeline_thread).start()

def open_output_dir():
    config = load_config()
    out_dir = config.get('output_dir', 'reports')
    if os.path.exists(out_dir):
        os.startfile(out_dir)
    else:
        messagebox.showwarning("Warning", "Reports directory does not exist yet.")

def schedule_task():
    import scheduler
    scheduler.create_schedule()
    messagebox.showinfo("Success", "Task scheduled successfully (Daily at 09:00 AM).")

def main():
    # Check for CLI arguments for headless mode (Scheduler)
    if len(sys.argv) > 1 and sys.argv[1] == "--generate":
        print("Running in headless mode...")
        report_generator.main()
        sys.exit(0)

    root = tk.Tk()
    root.title("Auto Report Manager")
    root.geometry("400x350")
    
    label = tk.Label(root, text="Automated Report Tool", font=("Arial", 16, "bold"))
    label.pack(pady=20)
    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    btn_run = tk.Button(btn_frame, text="Generate Reports Only", command=run_reports, height=2, width=25, font=("Arial", 10))
    btn_run.pack(pady=10)

    btn_full = tk.Button(btn_frame, text="Run Full Pipeline (Data+Report)", command=run_full_pipeline, height=2, width=25, bg="#4CAF50", fg="white", font=("Arial", 10))
    btn_full.pack(pady=10)
    
    btn_open = tk.Button(btn_frame, text="Open Reports Folder", command=open_output_dir, height=2, width=25, font=("Arial", 10))
    btn_open.pack(pady=10)
    
    btn_schedule = tk.Button(btn_frame, text="Enable Daily Schedule", command=schedule_task, height=2, width=25, bg="#2196F3", fg="white", font=("Arial", 10))
    btn_schedule.pack(pady=10)
    
    # Version info
    ver_label = tk.Label(root, text="v2.0 - Bundled Edition", fg="gray")
    ver_label.pack(side=tk.BOTTOM, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
