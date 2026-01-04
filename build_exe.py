import PyInstaller.__main__
import os
import shutil

def build():
    print("🚀 Building Executable...")
    
    # Clean previous builds
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
        
    # PyInstaller arguments
    args = [
        'gui_app.py',  # Main script
        '--name=AutoReportTool',
        '--onefile',
        '--windowed',  # No console window for GUI
        '--clean',
        # Exclude bulky modules if possible, but pandas/openpyxl are needed
    ]
    
    PyInstaller.__main__.run(args)
    
    print("\n✅ Build Complete! Check 'dist/AutoReportTool.exe'")
    
    # Copy config and dummy data to dist for easy testing
    print("Copying config.json and customers.csv to dist/...")
    shutil.copy("config.json", "dist/config.json")
    if os.path.exists("customers.csv"):
        shutil.copy("customers.csv", "dist/customers.csv")

if __name__ == "__main__":
    build()
