import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
import pandas as pd
import numpy as np

import argparse
import pandas as pd


df0=[]
# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

def main(query=None,max_workers=None,locations=None,limit=10,company_jobs_url=None):
    global df0
    ddd=None

    columns=['title', 'company','job_id', 'date', 'link', 'insights', 'description']

    def on_data(data: EventData):
        global df0,ddd
        ddd=data
        df0.append([data.title, data.company,data.job_id, data.date, data.link, data.insights, data.description])
        print('[ON_DATA]', data.title, data.company, data.date, data.link, data.insights, len(data.description))


    def on_error(error):
        print('[ON_ERROR]', error)


    def on_end():
        print('[ON_END]')


    scraper = LinkedinScraper(
        chrome_options=None,  # Custom Chrome options here
        headless=True,  # Overrides headless mode only if chrome_options is None
        max_workers=max_workers,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
        slow_mo=1.5,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
    )

    # Add event listeners
    scraper.on(Events.DATA, on_data)
    scraper.on(Events.ERROR, on_error)
    scraper.on(Events.END, on_end)

    queries = [
        Query(
            options=QueryOptions(
                optimize=True,  # Blocks requests for resources like images and stylesheet

            )
        ),
        Query(
            query=query,
            options=QueryOptions(
                locations=locations,
                optimize=False,
                limit=5,
                filters=QueryFilters(
                    company_jobs_url=company_jobs_url,  # Filter by companies
                    relevance=RelevanceFilters.RECENT,
                    time=TimeFilters.MONTH,
                    type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                    experience=None,                
                )
            )
        ),
    ]

    scraper.run(queries)
    
    df=pd.DataFrame(df0,columns=columns)
    df.to_csv('link_job.csv')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q","--query",
                        help='job query',
                        required=True)
    parser.add_argument("-loc","--locations",
                        help='Enter locations',
                        required=0)
    parser.add_argument("-lim","--limit",
                        help='Enter limit',
                        required=True)
    parser.add_argument("-com","--company_jobs",
                        help='Enter company_jobs_url',
                        required=0)
    parser.add_argument("-w","--max_workers",
                        help='Enter max_workers',
                        required=True)
    
    args = parser.parse_args()
    main(args.query,int(args.max_workers),args.locations,int(args.limit),args.company_jobs)