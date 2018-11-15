import requests
import os

class WebRequest:
	# fixes 429/too many requests error
	headers = {
		'User-Agent': 'Sample Agent 1.0',
		'From': 'email@domain.com'
	}

	def request(self, url, isJson = False):
		if(isJson):
			return requests.get(url, headers=self.headers).json()
		else:
			return requests.get(url, headers=self.headers)

	def download(self, url, filename, ext):
		tmp_req = self.request(url, False)

		tmp_filename = filename + '.' + ext

		if not os.path.exists('downloads/'): os.mkdir('downloads/')

		with open('downloads/' + tmp_filename, 'wb') as file:
			file.write(tmp_req.content)

		print(tmp_filename + ' was downloaded.')