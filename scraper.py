import os
import json
import requests
from bs4 import BeautifulSoup

# List of internal Reva University URLs
urls = [
     "https://www.reva.edu.in/all-programmes",
    "https://www.reva.edu.in/course-list/undergraduate-programmes",
    "https://www.reva.edu.in/course-list/postgraduate-programmes",
    "https://www.reva.edu.in/course-list/research-phd-programmes",
    "https://www.reva.edu.in/course-list/diploma-programmes",
    "https://www.reva.edu.in/minor-degree-program",
    "https://www.reva.edu.in/about-university",
    "https://www.reva.edu.in/learning-and-pedagogy",
    "https://www.reva.edu.in/academic-quality-and-standards",
    "https://www.reva.edu.in/academic-calendar",
    "https://www.reva.edu.in/life-at-reva",
    "https://www.reva.edu.in/new-admissions/",
    "https://www.reva.edu.in/admission-overview",
    "https://www.reva.edu.in/faq",
    "https://www.reva.edu.in/course/btech-in-computer-science-and-engineering",
    "https://www.reva.edu.in/course/btech-in-computer-science-and-information-technology",
    "https://www.reva.edu.in/course/btech-in-artificial-intelligence-and-data-science",
    "https://www.reva.edu.in/course/btech-in-information-science-and-engineering",
    "https://www.reva.edu.in/course/b-tech-in-computer-science-and-engineering-internet-of-things-and-cyber-security-including-block-chain-technology",
    "https://www.reva.edu.in/course/btech-computer-science-and-engineering-artificial-intelligence-and-machine-learning",
    "https://www.reva.edu.in/course/btech-in-civil-engineering",
    "https://www.reva.edu.in/course/btech-in-electronics-and-communication-engineering",
    "https://www.reva.edu.in/course/btech-in-electronics-and-computer-engineering",
    "https://www.reva.edu.in/course/btech-in-agricultural-engineering",
    "https://www.reva.edu.in/course/btech-in-mechanical-engineering",
    "https://www.reva.edu.in/course/btech-in-mechatronics-engineering",
    "https://www.reva.edu.in/course/btech-in-aerospace-engineering",
    "https://www.reva.edu.in/course/btech-in-electrical-and-electronics-engineering",
    "https://www.reva.edu.in/course/bachelor-of-architecture",
    "https://www.reva.edu.in/course/bsc-hons-in-interior-design",
    "https://www.reva.edu.in/course/bachelor-of-arts-and-bachelor-of-laws-ba-llb-honours",
    "https://www.reva.edu.in/course/bachelor-of-business-administration-and-bachelor-of-law-bba-llb-honours",
    "https://www.reva.edu.in/course/bcom-professional-ca-foundation-in-association-with-brics-academy",
    "https://www.reva.edu.in/course/bcom-dual-specialisations",
    "https://www.reva.edu.in/course/bcom-single-specialisation",
    "https://www.reva.edu.in/course/bcom-honours-accounting-and-taxation",
    "https://www.reva.edu.in/course/bcom-honours-statistics-and-accounting",
    "https://www.reva.edu.in/course/bcom-honours-economics-and-finance",
    "https://www.reva.edu.in/course/bcom-corporate-governance-and-auditing-dual-specialisation",
    "https://www.reva.edu.in/course/bachelor-of-computer-applications-bca",
    "https://www.reva.edu.in/course/bachelor-of-science-hons-in-computer-science-with-specialization-in-cloud-computing-and-big-data",
    "https://www.reva.edu.in/course/bachelor-of-science-in-computer-science-with-specialization-in-multimedia-and-animation",
    "https://www.reva.edu.in/course/bsc-biochemistry-microbiology-medical-laboratory-technology",
    "https://www.reva.edu.in/course/bachelor-of-science-in-computer-science-with-specialization-in-cyber-security",
    "https://www.reva.edu.in/course/bsc-in-biotechnology-biochemistry-genetics",
    "https://www.reva.edu.in/course/bsc-in-bioinformatics-statistics-computer-science-bstcs",
    "https://www.reva.edu.in/course/bsc-in-microbiology-chemistry-genetics",
    "https://www.reva.edu.in/course/ba-in-performing-arts-english-and-psychology",
    "https://www.reva.edu.in/course/bsc-in-medical-radiology-and-diagnostic-imaging",
    "https://www.reva.edu.in/course/bsc-in-nutrition-and-dietetics",
    "https://www.reva.edu.in/course/b-sc-sports-science",
    "https://www.reva.edu.in/course/bachelor-of-physiotherapy",
    "https://www.reva.edu.in/course/ba-in-journalism-english-and-psychology",
    "https://www.reva.edu.in/course/ba-in-political-science-economics-and-journalism",
    "https://www.reva.edu.in/course/ba-in-journalism-and-mass-communication",
    "https://www.reva.edu.in/course/bba-in-aviation",
    "https://www.reva.edu.in/course/bachelor-of-business-administration",
    "https://www.reva.edu.in/course/bsc-psychology-honours",
    "https://www.reva.edu.in/course/ba-in-journalism-and-mass-communication",
    "https://www.reva.edu.in/course/ba--journalism-major-and-political-science-minor",
    "https://www.reva.edu.in/course/b-tech-robotics-and-artificial-intelligence-2024-25",
    "https://www.reva.edu.in/course/bba-banking-and-finance",
    "https://www.reva.edu.in/course/bba-business-analytics",
    "https://www.reva.edu.in/course/bba-human-resource-management",
    "https://www.reva.edu.in/course/bba-international-business",
    "https://www.reva.edu.in/course/bba-in-marketing-and-supply-chain-management",
    "https://www.reva.edu.in/course/bcom-international-business",
    "https://www.reva.edu.in/course/bcom-banking-and-insurance",
    "https://www.reva.edu.in/course/bcom-accounting-and-fintech",
    "https://www.reva.edu.in/course/bcom-in-taxation",
    "https://www.reva.edu.in/course/bba-in-entrepreneurship",
    "https://www.reva.edu.in/course/bba-marketing-and-advertising",
    "https://www.reva.edu.in/course/bachelor-of-management-studies",
    "https://www.reva.edu.in/course/btech-computer-science-and-systems-engineering-csse",
    "https://www.reva.edu.in/course/bcom-in-accounting",
    "https://www.reva.edu.in/course/bcom-in-finance",
    "https://www.reva.edu.in/course/bcom-in-banking",
    "https://www.reva.edu.in/course/bcom-finance--data-analysis",
    "https://www.reva.edu.in/internal-quality-assurance-cell"
]

# Output directory to store HTML files and summary
OUTPUT_DIR = "reva_output"

def setup_output_directory():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def fetch_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_page(url, html):
    file_slug = url.rstrip("/").split("/")[-1] or "home"
    filename = os.path.join(OUTPUT_DIR, f"{file_slug}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return filename

def extract_title(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.get_text(strip=True) if soup.title else "No Title"

def scrape_all():
    setup_output_directory()
    summary = {}
    for url in urls:
        print(f"Fetching: {url}")
        html = fetch_url(url)
        if html:
            filename = save_page(url, html)
            title = extract_title(html)
            summary[url] = {"title": title, "filename": filename}
        else:
            summary[url] = {"title": "Error", "filename": None}
    return summary

if __name__ == "__main__":
    # For standalone testing: scrape and save summary as JSON
    summary = scrape_all()
    summary_file = os.path.join(OUTPUT_DIR, "summary.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)
    print("Scraping complete. Summary saved to:", summary_file)
