# Retail Demand Forecasting | Data Engineering Pipeline

> A production-ready ETL pipeline for processing and validating multi-source retail sales data, built with PySpark and pandas for scalable data engineering and analytics preparation.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/PySpark-4.0.0-orange.svg)](https://spark.apache.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.1-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents
- [Overview](#overview)
- [Pipeline Architecture](#pipeline-architecture)
- [Key Features](#key-features)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Output Structure](#output-structure)
- [Technologies](#technologies)
- [Project Highlights](#project-highlights)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project implements a scalable, end-to-end data engineering pipeline that processes 421,000+ rows of Walmart sales data. The pipeline ingests data from multiple sources, performs comprehensive validation checks, and produces analytics-ready datasets for downstream forecasting and business intelligence applications.

**Core Focus**: Data engineering best practices, validation-first approach, and production-quality ETL design.

### Business Context
Retail organizations require clean, validated data pipelines to support accurate demand forecasting and inventory optimization. This pipeline addresses data quality challenges by implementing multi-layer validation and automated quality checks.

---

## Pipeline Architecture

The pipeline follows a standard ETL (Extract, Transform, Load) pattern with an integrated validation layer:

```
┌─────────────────────────────────────────────────────────┐
│                      RAW DATA                            │
│         (Multi-source CSV: 421K+ rows)                   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    EXTRACT LAYER                         │
│   • PySpark distributed loading                          │
│   • Pandas in-memory processing                          │
│   • Schema inference & type casting                      │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 VALIDATION LAYER                         │
│   ✓ Schema validation (columns, types)                  │
│   ✓ Row count integrity (pre/post join)                 │
│   ✓ Null detection (critical fields)                    │
│   ✓ Duplicate prevention                                │
│   ✓ Data quality checks                                 │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 TRANSFORM LAYER                          │
│   • Multi-source joins (Store-Date alignment)           │
│   • Date parsing & standardization                      │
│   • Temporal feature engineering                        │
│   • Missing value handling                              │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              ANALYTICS-READY OUTPUT                      │
│   • Validated datasets                                   │
│   • Quality reports                                      │
│   • Visualizations                                       │
└─────────────────────────────────────────────────────────┘
```

---

## Key Features

### Data Quality & Validation
- ✅ **Schema Enforcement** - Validates expected column names and data types
- ✅ **Join Integrity** - Ensures row count preservation across multi-table joins
- ✅ **Null Detection** - Identifies missing values in critical columns
- ✅ **Duplicate Prevention** - Enforces unique Store-Dept-Date combinations
- ✅ **Range Validation** - Checks for anomalies (negative sales, invalid dates)
- ✅ **Cardinality Checks** - Verifies expected data distributions

### Data Engineering Capabilities
- **Multi-Source Integration** - Combines 3 data sources with different schemas
- **Distributed Processing** - Leverages PySpark for scalability
- **Temporal Features** - Extracts week, month, and seasonal patterns
- **Automated Reporting** - Generates validation reports and quality metrics
- **High-Resolution Outputs** - Produces publication-quality visualizations (300 DPI)

---

## Data Sources

The pipeline processes four datasets from Walmart's retail operations:

| Dataset | Records | Schema | Purpose |
|---------|---------|--------|---------|
| **train.csv** | 421,570 | Store, Dept, Date, Weekly_Sales, IsHoliday | Historical sales transactions |
| **test.csv** | 115,064 | Store, Dept, Date, IsHoliday | Forecast period (prediction targets) |
| **features.csv** | 8,190 | Store, Date, Temperature, Fuel_Price, Markdowns (1-5), CPI, Unemployment, IsHoliday | Economic & promotional indicators |
| **stores.csv** | 45 | Store, Type, Size | Store metadata & characteristics |

**Combined Output**: 421,570 validated rows with 20+ features ready for analytics and modeling.

---

## Installation

### Prerequisites
- **Python** 3.8 or higher
- **Java** 8 or 11 (required for PySpark)
- **Git** (for cloning repository)

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/retail-demand-forecasting.git
cd retail-demand-forecasting

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Java Configuration (PySpark)
```bash
# Set JAVA_HOME environment variable
# Windows
set JAVA_HOME=C:\Program Files\Java\jdk-11.0.x

# macOS/Linux  
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

---

## Usage

### 1. Data Preparation
Place the following CSV files in the `data/` directory:
- `data/train.csv/train.csv`
- `data/test.csv/test.csv`
- `data/features.csv/features.csv`
- `data/stores.csv`

### 2. Run the Pipeline

**Option A: Jupyter Notebook (Interactive)**
```bash
jupyter notebook
# Open and run: 01_eda_exploration.ipynb
# Open and run: 02_eda_pysparkk.ipynb
```

**Option B: VS Code (Recommended)**
```bash
code .
# Open notebooks in VS Code with Jupyter extension
# Run cells sequentially
```

### 3. Pipeline Execution Order

1. **01_eda_exploration.ipynb** - Pandas-based pipeline
   - Data ingestion and merging
   - Comprehensive validation checks
   - Exploratory data analysis
   - Visualization generation

2. **02_eda_pysparkk.ipynb** - PySpark-based pipeline
   - Distributed data processing
   - Scalable validation checks
   - Temporal feature engineering
   - Performance benchmarking

### 4. Review Outputs
Check the `outputs/` folder for:
- Validation reports (TXT)
- Visualizations (PNG, 300 DPI)
- Summary statistics (CSV)
- Processed data samples (CSV)

---

## Output Structure

All pipeline outputs are organized in the `outputs/` directory:

```
outputs/
├── validation_report.txt              # Comprehensive validation results
├── 01_sales_over_time.png            # Time series visualization
├── 02_sales_by_store_type.png        # Store type analysis
├── 03_sales_by_store_size.png        # Store size distribution
├── 04_sales_by_type_and_size.png     # Combined analysis
├── summary_statistics.csv             # Descriptive statistics
└── pyspark/
    ├── pyspark_validation_report.txt  # Distributed validation results
    └── processed_data_sample.csv      # Sample of cleaned data (1,000 rows)
```

### Sample Outputs

**Validation Report** - Automated quality checks with pass/fail status
**Visualizations** - Publication-quality plots for business stakeholders
**Statistics** - Descriptive metrics for all numeric features
**Data Samples** - Validated datasets ready for downstream modeling

---

## Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.x | Core programming language |
| **PySpark** | 4.0.0 | Distributed data processing |
| **Pandas** | 2.3.1 | In-memory data manipulation |
| **Matplotlib** | 3.10.3 | Data visualization |
| **Seaborn** | 0.13.2 | Statistical plotting |
| **Jupyter** | Latest | Interactive development |
| **NumPy** | 2.3.2 | Numerical computing |

**Development Tools**: VS Code, Git, virtual environments

---

## Project Highlights

### Data Engineering Expertise
- Designed and implemented a complete ETL pipeline from scratch
- Processed 421K+ records with multi-source integration
- Built a reusable validation framework with 6 distinct check types
- Achieved 100% data quality coverage through automated validation
- Implemented both distributed (PySpark) and in-memory (pandas) processing

### Technical Proficiency
- Distributed computing with PySpark
- Data quality engineering and validation frameworks
- SQL-like joins and multi-table transformations
- Time-series feature extraction and temporal analysis
- Production-quality documentation and code organization

### Engineering Best Practices
- **Validation-First Approach**: Quality checks before transformation
- **Modular Design**: Separation of ingestion, validation, and transformation
- **Reproducibility**: Documented workflows with version-controlled code
- **Scalability**: Designed for growth from local to distributed processing
- **Transparency**: Comprehensive reporting and audit trails

---

## Roadmap

### Completed ✅
- [x] ETL pipeline implementation (Extract, Transform, Load)
- [x] Multi-layer validation framework
- [x] Pandas and PySpark processing paths
- [x] Automated quality reporting
- [x] High-resolution visualization outputs

### In Progress 🚧
- [ ] Refactor notebooks to modular Python scripts
- [ ] Implement unit and integration tests
- [ ] Add CI/CD pipeline with GitHub Actions

### Future Enhancements 🎯
- [ ] Orchestration with Apache Airflow or Prefect
- [ ] Cloud deployment (AWS EMR, Databricks, GCP Dataproc)
- [ ] Data quality monitoring dashboard
- [ ] Automated email alerts for validation failures
- [ ] ML model integration for demand forecasting
- [ ] REST API for data access
- [ ] Docker containerization

---

## Contributing

Contributions are welcome! This project is designed for portfolio and educational purposes.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

### Areas for Contribution
- Performance optimization
- Additional validation checks
- New visualization types
- Documentation improvements
- Test coverage expansion

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Data Source**: Walmart Recruiting - Store Sales Forecasting (Kaggle)
- **Frameworks**: Apache Spark, pandas development team
- **Community**: Stack Overflow, PySpark documentation contributors

---

## Contact

**Project Maintainer**: [Your Name]  
**Email**: your.email@example.com  
**LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)  
**Portfolio**: [Your Portfolio Website](https://yourportfolio.com)

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star! ⭐**

Built with ❤️ for data engineering excellence

</div>

**✅ Completed**
- ETL pipeline (extract, transform, load)
- Validation layer (schema, nulls, duplicates, quality)
- Multi-source joins
- Exploratory analysis

**⏳ In Progress**
- ML modeling scripts
- Automated testing
- Production refactoring

---

## Limitations

- Notebook-based execution (not production scripts)
- No orchestration or scheduling
- Local PySpark mode (not distributed cluster)
- Manual validation review (no automated alerts)
- No CI/CD integration

---

## Next Steps

- Refactor to modular Python scripts
- Add orchestration (Airflow, Prefect)
- Implement automated testing
- Deploy to cloud (AWS, GCP, Databricks)
- Add data quality monitoring

---

## Contact

For questions about this project's data engineering approach, pipeline design, or validation strategy, please refer to the full technical documentation: `Retail_Demand_Forecasting_project_detail.md`

---

*This project bridges data engineering and analytics, suitable for roles in data engineering, analytics engineering, or data science with strong engineering fundamentals.*
