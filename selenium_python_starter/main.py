import time
from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv


scraper = Scraper('https://facebook.com')
scraper.add_login_functionality('https://facebook.com', 'a[href="/me/"]', 'facebook')
scraper.go_to_page("https://www.facebook.com/groups/371814107751376")