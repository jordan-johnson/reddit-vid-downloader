import os
import unittest
from RedditThreadReader import RedditThreadReader

class RedditThreadReaderTestCase(unittest.TestCase):
	reader = None
	example_url = None

	def setUp(self):
		self.reader = RedditThreadReader()
		self.example_url = 'https://old.reddit.com/r/Overwatch/comments/9x5h5q/booobbb_do_somthi_oh/.json'

	def test_read(self):
		self.reader.thread_addr = self.example_url
		self.reader.thread_json = self.reader.web.request_json(self.example_url)
		self.reader.parse()

		self.assertIsNotNone(self.reader.audio_addr)
		self.assertIsNotNone(self.reader.video_addr)

	def main(self):
		unittest.main()
