# Czech Election Results Scraper

A Python web scraper that extracts election results from the Czech Statistical Office website (volby.cz) for the 2017 parliamentary elections.

## Project Description

This project is the third assignment for the Engeto Online Python Academy. It scrapes election data from Czech municipalities within a specified district and exports the results to a CSV file.

The scraper collects:
- Municipality code and name
- Number of registered voters
- Number of envelopes issued
- Number of valid votes
- Vote counts for each political party

## Installation

### Prerequisites
- Python 3.6 or higher

### Required Libraries

Install the required dependencies using pip:

```bash
pip install requests beautifulsoup4
```

Or install from a requirements file:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
requests
beautifulsoup4
```

## Running the Project

The script requires two command-line arguments:

```bash
python main.py <target_district_url> <csv_file_name>
```

### Arguments:
1. **target_district_url** - URL of the district election page from volby.cz
2. **csv_file_name** - Name of the output CSV file (must end with `.csv`)

### Example Usage

Scraping results for the Benešov district:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "benešov_results.csv"
```

### Expected Output

```
[Initiating scraper]
[Scraping municipalities]
[Scraping finished - results saved to benešov_results.csv]
```

### Output CSV Format

The resulting CSV file will contain columns:
- `municipality_code` - Municipal identification code
- `municipality_name` - Name of the municipality
- `registered_voters` - Total registered voters
- `envelopes_issued` - Number of envelopes issued
- `valid_votes` - Number of valid votes cast
- `[Party Name]` - Vote count for each political party

**Sample output (benešov_results.csv):**

| municipality_code | municipality_name | registered_voters | envelopes_issued | valid_votes | Občanská demokratická strana | Řád národa - Vlastenecká unie | ... |
|-------------------|-------------------|-------------------|------------------|-------------|------------------------------|-------------------------------|-----|
| 529303 | Benešov | 12 345 | 8 234 | 8 156 | 1 234 | 45 | ... |
| 532568 | Červený Újezd | 856 | 567 | 562 | 89 | 12 | ... |

## Error Handling

The script validates inputs and will exit with an error message if:
- Incorrect number of arguments provided
- URL is not from the volby.cz domain
- Output filename does not end with `.csv`
