"""
main.py: třetí projekt do Engeto Online Python Akademie

author: David Horák
email: daviiid739@gmail.com
"""

import csv
import sys
from requests import get
from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup as soup


def get_municipality_urls(district_url: str) -> list:
    """
    Retrieves URLs of all municipalities in a given district
    
    Args:
        district_url (str): URL of the district election page
        
    Returns:
        list: List of municipality URLs
    """
    html = get(district_url)
    html_soup = soup(html.text, "html.parser")
    municipality_urls = [f"https://www.volby.cz/pls/ps2017nss/{a['href']}" for a in html_soup.select('td.cislo a')]

    return municipality_urls

def get_municipality_code(url: str) -> str:
    """
    Extracts municipality code from URL parameter xobec
    
    Args:
        url (str): Election page URL
        
    Returns:
        str: Municipality code (e.g. '589691')
    """
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    return params['xobec'][0]

def get_municipality_name(html_soup) -> str:
    """
    Retrieves municipality name from HTML heading
    Searches for <h3> tag containing text "Obec:" and extracts name after colon
    
    Args:
        html_soup: BeautifulSoup parsed HTML
        
    Returns:
        str: Municipality name
    """
    h3_tags = html_soup.find_all('h3')
    
    for h3 in h3_tags:
        text = h3.get_text(strip=True)
        if 'Obec:' in text:
            return text.split(':', 1)[1].strip()

def get_basic_stats(tables: list) -> dict:
    """
    Retrieves basic election statistics from the first table
    
    Args:
        tables (list): List of BeautifulSoup table elements
        
    Returns:
        dict: Dictionary with keys 'registered_voters', 'envelopes_issued', 'valid_votes'
    """
    first_table = tables[0]
    
    HTML_STATS_ID = {
        'registered_voters': 'sa2',
        'envelopes_issued': 'sa3',
        'valid_votes': 'sa6'
    }
    
    results = {}
    
    for column_name, html_id in HTML_STATS_ID.items():
        cell = first_table.find('td', headers=html_id)
        results[column_name] = cell.get_text(strip=True)
    
    return results

def get_party_votes(tables: list) -> dict:
    """
    Retrieves vote counts for all candidate parties
    
    Args:
        tables (list): List of BeautifulSoup table elements

    Returns:
        dict: Dictionary {party_name: vote_count}
    """
    party_results = {}
    
    for table in tables[1:]:
        rows = table.find_all('tr')
        
        for row in rows[2:]:
            cells = row.find_all('td')
            
            party_name = cells[1].get_text(strip=True)
            vote_count = cells[2].get_text(strip=True)
            
            if party_name != '-':
                party_results[party_name] = vote_count
    
    return party_results

def scrape_municipality(url: str) -> dict:
    """
    Main function for scraping data from one municipality
    
    Args:
        url (str): URL of municipality election page
        
    Returns:
        dict: Complete municipality data
    """
    html = get(url)
    html_soup = soup(html.text, "html.parser")
    tables = html_soup.find_all("table")
    
    result = {}
    result['municipality_code'] = get_municipality_code(url)
    result['municipality_name'] = get_municipality_name(html_soup)
    
    basic_stats = get_basic_stats(tables)
    result.update(basic_stats)
    
    party_votes = get_party_votes(tables)
    result.update(party_votes)
    
    return result

def save_to_csv(data: list, csv_file: str) -> None:
    """
    Saves list of dictionaries to CSV file
    
    Args:
        data (list): List of dictionaries with election results
        csv_file (str): Output CSV file name
    """
    with open(csv_file, mode="w", newline='', encoding='utf-8') as f:
        headers = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def validate_args() -> tuple:
    """
    Validates command line arguments
    
    Returns:
        tuple: (district_url, csv_filename) if valid
        
    Exits:
        Program exits with error message if arguments are invalid
    """
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments!")
        sys.exit(1)
    
    district_url = sys.argv[1]
    csv_filename = sys.argv[2]

    if 'www.volby.cz' not in district_url:
        print("Error: Invalid URL! URL must be from volby.cz domain")
        sys.exit(1)

    if not csv_filename.endswith('.csv'):
        print("Error: Invalid output filename! Output filename must end with '.csv'")
        sys.exit(1)

    return district_url, csv_filename


def main():
    district_url, csv_filename = validate_args()
    print(f"[Scraping data from Url: '{district_url}']") 

    municipality_urls = get_municipality_urls(district_url)
    print("[Scraping data from municipalities]")

    election_results = [scrape_municipality(url) for url in municipality_urls]
    save_to_csv(election_results, csv_filename)
    print(f"[Scraping finished - results saved to '{csv_filename}']")


if __name__ == "__main__":

    main()
