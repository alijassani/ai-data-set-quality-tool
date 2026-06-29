# AI Dataset Quality Tool

A Python tool designed to analyse and validate AI training datasets to improve data quality and consistency.

## Features

- Counts total dataset rows
- Detects missing labels
- Identifies duplicate entries
- Generates a simple dataset quality report

## Technologies Used

- Python
- CSV processing

## Example Dataset

The repository includes a sample CSV dataset containing image filenames and labels.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/alijassani/ai-data-set-quality-tool.git
```

2. Navigate to the project folder:

```bash
cd ai-data-set-quality-tool
```

3. Run the script:

```bash
python dataset_quality_checker.py
```

## Example Output

```text
Dataset Quality Report
----------------------
Total rows: 5
Missing labels: 1
Duplicate rows: 1
```

## Future Improvements

- Add graphical reports
- Support JSON datasets
- Export quality reports as CSV or PDF
- Build a web interface using React and Flask

## Author

Ali Mousa
