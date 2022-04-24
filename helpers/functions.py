from ast import Not
import time
import pandas as pd


def generate_multiple_images_path(path):
	images_path = ''

	images = path.split(',')

	for image in images:
		image = image.strip()

		if images_path != '':
				images_path += '\n'
		
		images_path += image
		
	return images_path

# scraper.driver.execute_script("""var scrollDiv = document.querySelector('div[role="main"] > div:first-child > div:nth-child(4)'); scrollDiv.scrollTop = 850;""")
