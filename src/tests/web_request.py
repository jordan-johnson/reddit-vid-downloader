import os
import unittest
from WebRequest import WebRequest

class WebRequestTestCase(unittest.TestCase):
	web = None
	example_url = None
	example_dir = None
	example_file = None

	def setUp(self):
		self.web = WebRequest()
		self.example_url = 'https://old.reddit.com/r/Overwatch/comments/9x5h5q/booobbb_do_somthi_oh/.json'
		self.example_dir = 'downloads/'
		self.example_file = 'test.json'

	def tearDown(self):
		file_path = self.example_dir + self.example_file

		if os.path.isfile(file_path):
			os.remove(file_path)

	def test_request(self):
		content = self.web.request(self.example_url)
		self.assertIsNotNone(content)

	def test_request_json(self):
		content = self.web.request_json(self.example_url)
		self.assertIsNotNone(content)

	def test_download(self):
		self.web.download(self.example_url, self.example_file)

		dir_path = os.path.isdir(self.example_dir)
		file_path = os.path.isfile(self.example_dir + self.example_file)

		self.assertTrue(dir_path)
		self.assertTrue(file_path)

	def main(self):
		unittest.main()
