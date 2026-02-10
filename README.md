# Czech Election Results Scraper

## Project Description

A Python web scraper that scrapes election data from Czech municipalities within a specified district and exports the results to a CSV file.

### Required Libraries installation

The libraries used in the code are stored in the requirements.txt file. For installation, I recommend using a new virtual environment. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running the Project

The script requires two command-line arguments:

```bash
python main.py <target_district_url> <csv_file_name>
```

The results will then be downloaded as a file with the .csv extension

### Example Usage

Scraping results for the Benešov district:

1. argument: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"
2. argument: "benešov_results.csv"

Program launch:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "benešov_results.csv"
```

Download progress:

```bash
[Scraping data from Url: 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101']
[Scraping data from municipalities]
[Scraping finished - results saved to 'benešov_results.csv']
```

Partial output:

```bash
municipality_code,municipality_name,registered_voters,envelopes_issued,valid_votes,Občanská demokratická strana,...
529303,Benešov,13 104,8 485,8 437,1 052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2 577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
532380,Blažejovice,96,80,77,6,0,0,5,0,3,11,0,0,3,0,0,5,1,0,0,29,0,0,6,0,0,0,0,8,0
```
