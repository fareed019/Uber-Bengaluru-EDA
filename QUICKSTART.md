# ⚡ Quick Start Guide

Get your Uber Bengaluru EDA analysis up and running in 5 minutes!

---

## 🎯 5-Minute Setup

### **1. Clone/Download the Repository**
```bash
git clone https://github.com/YOUR-USERNAME/uber-bengaluru-eda.git
cd uber-bengaluru-eda
```

### **2. Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add Your Data**
Place your `uber-data.csv` file in the `data/` folder

### **5. Run Analysis**
```bash
python scripts/eda_analysis.py
```

✅ **Done!** Check the `images/` folder for visualizations.

---

## 📖 Run Jupyter Notebook

```bash
jupyter notebook notebooks/Uber_Bengaluru_EDA.ipynb
```

Then click through each cell to run the analysis step-by-step.

---

## 📂 Directory Structure at a Glance

```
uber-bengaluru-eda/
├── README.md                          # Start here for overview
├── QUICKSTART.md                      # This file
├── GITHUB_SETUP_GUIDE.md             # Upload to GitHub guide
├── DATA_DICTIONARY.md                 # Column descriptions
├── requirements.txt                   # Install with: pip install -r requirements.txt
│
├── data/
│   └── uber-data.csv                  # ← Add your CSV file here
│
├── notebooks/
│   └── Uber_Bengaluru_EDA.ipynb      # Jupyter notebook version
│
├── scripts/
│   └── eda_analysis.py               # Run with: python scripts/eda_analysis.py
│
└── images/
    ├── 01_status_distribution.png
    ├── 02_hourly_demand.png
    ├── 03_pickup_location_comparison.png
    ├── 04_status_by_hour.png
    ├── 05_city_pickup_analysis.png
    └── 06_airport_pickup_analysis.png
```

---

## 🔧 Common Commands

| Task | Command |
|------|---------|
| Activate virtual env | `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows) |
| Install packages | `pip install -r requirements.txt` |
| Run analysis | `python scripts/eda_analysis.py` |
| Start Jupyter | `jupyter notebook` |
| Deactivate env | `deactivate` |
| Update requirements | `pip freeze > requirements.txt` |

---

## 📊 What Gets Generated

After running the analysis, you'll get:

✅ **6 Visualizations**
- Status distribution
- Hourly demand pattern
- Location comparison
- Status by hour
- City pickup analysis
- Airport pickup analysis

✅ **Console Output**
- Data shape and info
- Descriptive statistics
- Key metrics
- Insights summary

✅ **PNG Files** in `images/` folder
- High resolution (300 DPI)
- Ready for presentations

---

## 💡 Key Insights You'll Find

1. **Peak Demand Hours:** 6-9 AM and 5-8 PM
2. **Availability Issues:** Spike during rush hours
3. **Location Differences:** City vs Airport patterns
4. **Service Quality:** Varies by time of day

---

## 🐛 Troubleshooting

### **Issue: "ModuleNotFoundError: No module named 'pandas'"**
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### **Issue: "FileNotFoundError: 'uber-data.csv'"**
**Solution:** Ensure CSV is in the `data/` folder
```bash
# Check file location
ls data/
# or
dir data  # Windows
```

### **Issue: "Python command not found"**
**Solution:** 
- Windows: Use `python` instead of `python3`
- Mac/Linux: Use `python3`

### **Issue: Virtual environment not working**
**Solution:** Recreate it
```bash
rm -rf venv  # or: rmdir /s venv (Windows)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Next Steps

1. **Understand the Data**
   - Read `DATA_DICTIONARY.md`
   - Check column descriptions

2. **Explore Visualizations**
   - Open `images/` folder
   - Read `IMAGES_README.md` for interpretation

3. **Study the Code**
   - Review `eda_analysis.py` comments
   - Run Jupyter notebook cells one by one

4. **Upload to GitHub**
   - Follow `GITHUB_SETUP_GUIDE.md`
   - Share with others

5. **Extend the Analysis**
   - Add more visualizations
   - Create predictive models
   - Write blog post about findings

---

## 📚 File Descriptions

| File | Purpose |
|------|---------|
| `README.md` | Project overview and documentation |
| `QUICKSTART.md` | This file - get started fast |
| `GITHUB_SETUP_GUIDE.md` | How to upload to GitHub |
| `DATA_DICTIONARY.md` | Explanation of all columns |
| `IMAGES_README.md` | Visualization descriptions |
| `eda_analysis.py` | Main Python analysis script |
| `Uber_Bengaluru_EDA.ipynb` | Interactive Jupyter notebook |

---

## 📞 Need Help?

**For Python/Pandas issues:**
- Stack Overflow: https://stackoverflow.com/questions/tagged/pandas
- Official Docs: https://pandas.pydata.org/docs/

**For Git/GitHub issues:**
- GitHub Docs: https://docs.github.com
- Git Cheat Sheet: https://github.github.com/training-kit/

**For Jupyter issues:**
- Jupyter Docs: https://jupyter.org/

---

## ✨ Pro Tips

🎯 **Tip 1: Speed Up Analysis**
```bash
# Run only once, save outputs
python scripts/eda_analysis.py > output.txt
```

🎯 **Tip 2: Compare Versions**
```bash
# Keep different versions of analysis
python scripts/eda_analysis.py > reports/analysis_v1.txt
```

🎯 **Tip 3: Customize the Script**
- Edit `scripts/eda_analysis.py` to add your own analysis
- Change colors, sizes, formats in visualizations

🎯 **Tip 4: Share Results**
- Upload images to your blog
- Post on LinkedIn
- Include in portfolio

---

## 📈 Performance Tips

| Task | Expected Time |
|------|----------------|
| Setup (first time) | 5-10 minutes |
| Run analysis | 30 seconds - 2 minutes |
| Generate visualizations | 5-30 seconds |
| Open Jupyter notebook | 10 seconds |
| Upload to GitHub | 2-5 minutes |

---

## 🎓 Learning Objectives

After completing this analysis, you'll understand:

✅ How to load and explore data with Pandas  
✅ How to clean and preprocess datasets  
✅ How to perform exploratory data analysis (EDA)  
✅ How to create meaningful visualizations  
✅ How to identify patterns and insights in data  
✅ How to document and share data science projects  
✅ How to use version control with Git/GitHub  

---

## 📊 Analysis Checklist

- [ ] Installed requirements
- [ ] Added data file
- [ ] Ran the analysis script
- [ ] Reviewed visualizations
- [ ] Read documentation
- [ ] Understood key findings
- [ ] Uploaded to GitHub
- [ ] Shared with others

---

## 🎉 You're Ready!

You now have a **production-ready EDA project**. Next step: Upload to GitHub and start building your portfolio! 

Follow `GITHUB_SETUP_GUIDE.md` for step-by-step instructions.

---

**Happy Analyzing!** 🚗📊✨

