# Automated Report Generation Tool

A complete solution for tracking project revenue and generating neat, visual Excel reports.

## 🚀 Features
- **Automated Reports**: Daily, Weekly, and Monthly Excel files.
- **Visuals**: Professional formatting + Bar & Pie Charts.
- **GUI**: Easy-to-use windowed application.
- **Scheduler**: Set it and forget it (runs daily at 9 AM).
- **Executable**: No Python required to run the EXE version.

## 🛠️ How to Run

### Option 1: The Easy Way (Executable)
1. Go to the `dist/` folder.
2. Double-click **`AutoReportTool.exe`**.
3. Use the buttons to:
   - **Generate Reports Now**: Creates files in `reports/`.
   - **Enable Daily Schedule**: Sets up the auto-run task.

### Option 2: The Developer Way (Python)
Ensure you have dependencies installed:
```bash
pip install pandas openpyxl
```

**Run the GUI:**
```bash
python gui_app.py
```

**Run the Generator directly (Headless):**
```bash
python report_generator.py
```

## 📂 Project Structure
- `customers.csv`: Input data (Customer Project info).
- `config.json`: Settings for file paths and report types.
- `reports/`: Folder where Excel files are saved.
- `generate_data.py`: Run this to create new dummy data.

## 🤝 Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
