# linkedin_scraper
> Scrape public available jobs on Linkedin using headless browser. 
> For each job, the following fields are extracted: 
> `title`, 
> `company`, 
> `job_id`, 
> `date`, 
> `link`, 
> `insights`.
> `description`,

## Requirements
- [Chrome](https://www.google.com/intl/en_us/chrome/) or [Chromium](https://www.chromium.org/getting-involved/download-chromium)
- [Chromedriver](https://chromedriver.chromium.org/)
- Python >= 3.6

## Installation
Install package:
```shell
pip install linkedin-jobs-scraper pandas
```

## Usage
```
usage: linkedin_scraper.py [-h] -q QUERY [-loc LOCATIONS] -lim LIMIT
                           [-com COMPANY_JOBS] -w MAX_WORKERS

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        job query (str)
  -loc LOCATIONS, --locations LOCATIONS
                        Enter locations
  -lim LIMIT, --limit LIMIT
                        Enter limit
  -com COMPANY_JOBS, --company_jobs COMPANY_JOBS
                        Enter company_jobs_url
  -w MAX_WORKERS, --max_workers MAX_WORKERS
                        Enter max_workers (from 1 to 5)
```
