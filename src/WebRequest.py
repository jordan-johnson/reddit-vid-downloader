import requests
import os

class WebRequest:
	download_dir = 'downloads/'

	# fixes 429/too many requests error
	headers = {
		'User-Agent': 'Sample Agent 1.0',
		'From': 'email@domain.com'
	}

	def request(self, url):
		return requests.get(url, headers=self.headers)

	def request_json(self, url):
		return self.request(url).json()

	def download(self, url, filename):
		request = self.request(url)

		if not os.path.exists(self.download_dir):
			os.mkdir(self.download_dir)

		with open(self.download_dir + filename, 'wb') as file:
			file.write(request.content)