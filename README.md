# Global Trade Data Analysis | Tariff & Compliance Intelligence

### Python Analytics • International Trade Compliance • Tariff Exposure • Executive Decision Support

A Python-based portfolio project demonstrating how trade data analytics can support import compliance, tariff exposure assessment, and strategic decision-making.

The project combines historical trade trend analysis (2022–2024) with a simulated U.S. import compliance and tariff intelligence model (2025–2026).

> **PORTFOLIO SIMULATION NOTICE**
>
> This project uses synthetic demonstration data and hypothetical tariff assumptions. The Section 201, 232, and 301 scenarios are not representations of actual historical or current U.S. tariff rates, legal applicability, or customs liabilities. All calculated duty exposure and mitigation opportunities are illustrative and should not be used for actual import compliance decisions.

---

## 1. Business Challenge

International trade teams must manage shifting tariff requirements, import costs, country-of-origin considerations, and evolving trade remedy measures.

Without centralized analytics, organizations may struggle to:

- Understand import and export trends.
- Identify products requiring trade remedy review.
- Quantify potential tariff-related financial exposure.
- Prioritize HTS classification and country-of-origin verification.
- Evaluate lawful tariff mitigation opportunities.
- Communicate trade compliance risks to executive leadership.

**Project objective:** Demonstrate how Python can transform trade and import data into structured, decision-ready compliance intelligence.

## 2. Project Components

### Historical Global Trade Analysis | 2022–2024

The original analysis evaluates synthetic import and export activity across China, Canada, Mexico, and Germany.

Key analytical outputs include:

- Annual import and export trends.
- Import and export values by country.
- Trade balances by trading partner.
- Country share of total imports.

![Historical Global Trade Dashboard](./trade_dashboard.png)

### Tariff & Compliance Intelligence | 2025–2026

The expanded model evaluates 150 synthetic U.S. import transactions against simplified, effective-dated tariff scenarios.

The analysis demonstrates:

- Transaction-level import data validation.
- Product-category and country-of-origin screening.
- Illustrative Section 201, 232, and 301 scenario matching.
- Modeled additional duty exposure.
- Country-level and trade remedy exposure reporting.
- Executive compliance priorities.

![Tariff & Compliance Intelligence Dashboard](./tariff_intelligence_dashboard.png)

**Important:** Scenario matches are screening results, not legally verified determinations of tariff applicability.

---

## 3. Executive Findings

The following findings are generated from fictional import transactions and hypothetical tariff rules.

| Metric | Simulated Result |
|---|---:|
| Import transactions analyzed | 150 |
| Total entered customs value | $19,796,679.82 |
| Transactions matching illustrative tariff scenarios | 93 |
| Scenario match rate | 62.0% |
| Modeled additional duty exposure | $2,702,835.93 |

### Modeled Exposure by Trade Remedy Program

| Program | Matched Entries | Modeled Additional Duties |
|---|---:|---:|
| Section 232 | 48 | $1,656,909.13 |
| Section 201 | 32 | $666,667.76 |
| Section 301 | 13 | $379,259.04 |

Under the modeled assumptions, Section 232 represents the largest share of additional duty exposure.

These figures demonstrate how compliance teams can prioritize review efforts using quantitative screening. They do not indicate actual tariff liability.

---

## 4. Trade Compliance Methodology

### Data Validation

Python validates transaction identifiers, entered values, and required data fields before performing analysis.

### Illustrative Tariff Rule Matching

Synthetic import transactions are compared against a separate tariff scenario table using:

- Product category.
- Country of origin.
- Entry date.
- Scenario effective dates.
- Hypothetical additional duty rates.

### Financial Exposure Modeling

For each matching transaction:

**Modeled Additional Duty = Entered Value × Illustrative Additional Duty Rate**

Results are aggregated by trade remedy program and country of origin.

### Regulatory Considerations

Actual U.S. tariff applicability can depend on HTS classification, Chapter 99 reporting requirements, country of origin, effective dates, exclusions, product scope, and interactions among applicable duty measures.

This demonstration uses simplified category-level screening rather than a legally validated tariff determination engine.

---

## 5. Executive Compliance Priorities

Based on the simulated analysis, the project identifies three management priorities:

**Priority 1 | Classification and Chapter 99 Review**

Validate HTS classifications, product descriptions, and applicable Chapter 99 provisions before determining additional duty exposure.

**Priority 2 | Country of Origin and Trade Remedy Review**

Evaluate country-specific trade remedy applicability, effective dates, exclusions, and supporting documentation.

**Priority 3 | Tariff Mitigation and Sourcing Strategy**

Assess lawful opportunities such as alternative sourcing, available exclusions, duty drawback, and Foreign-Trade Zone programs, subject to eligibility and regulatory requirements.

These are illustrative recommendations rather than findings of actual noncompliance or confirmed savings.

---

## 6. Technology Stack

- **Python:** Automated analysis and reporting.
- **pandas:** Data validation, merging, grouping, and calculations.
- **Matplotlib:** Executive dashboards and visualizations.
- **CSV:** Synthetic source data, scenario rules, and analytical reports.
- **GitHub:** Version control and portfolio documentation.

---

## 7. Repository Structure

Global-Trade-Data-Analysis/
├── README.md
├── requirements.txt
├── analysis.py
├── dashboard.py
├── trade_data.csv
├── trade_dashboard.png
├── generate_import_data.py
├── import_entries.csv
├── tariff_rules.csv
├── tariff_analysis.py
├── tariff_intelligence_dashboard.png
├── tariff_scenario_matches.csv
├── tariff_program_summary.csv
├── tariff_country_exposure.csv
└── tariff_category_exposure.csv

## 8. How to Run the Project

Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate the reproducible synthetic import dataset:

```bash
python3 generate_import_data.py
```

Run the tariff scenario analysis:

```bash
python3 tariff_analysis.py
```

Open the generated dashboard:

```bash
open outputs/tariff_intelligence_dashboard.png
```

The analysis generates CSV reports and an executive dashboard in the `outputs/` folder.

The original historical trade analysis is preserved in `analysis.py` and `dashboard.py`.

---

## 9. Limitations and Future Enhancements

## Limitations and Future Enhancements

This portfolio project uses synthetic import transactions and illustrative tariff assumptions to demonstrate Python-based trade compliance analytics. The modeled Section 201, Section 232, and Section 301 rates do not represent verified historical or current tariff treatment.

The analysis uses simplified product-category, country-of-origin, and effective-date matching. Actual U.S. customs determinations require review of the applicable HTS classification, Chapter 99 provisions, product-specific scope, origin rules, exclusions, duty stacking, and effective dates.

**Planned enhancements include:**

- **Compliance risk screening:** Flag transactions requiring additional HTS, origin, and trade remedy review.
- **Tariff mitigation scenarios:** Evaluate hypothetical sourcing alternatives and identify potential duty drawback or Foreign-Trade Zone considerations for further eligibility review.
- **Enhanced executive reporting:** Add risk prioritization, mitigation opportunities, and scenario comparisons.

Any potential mitigation benefits will be presented as hypothetical opportunities, not guaranteed duty savings.

## Professional Application

This project demonstrates skills relevant to international trade compliance, global sourcing, procurement analytics, and supply chain risk management.

It combines Python data processing with trade remedy awareness to translate complex import information into actionable business intelligence.

## Official Reference Resources

- [U.S. International Trade Commission: Harmonized Tariff Schedule](https://hts.usitc.gov/)
- [U.S. Customs and Border Protection: Trade Remedies](https://www.cbp.gov/trade/remedies)
- [Office of the United States Trade Representative](https://ustr.gov/)

---

*Portfolio demonstration only. All transaction data is synthetic, and tariff assumptions are illustrative. This project does not provide customs classification, legal advice, or verified duty calculations.*
