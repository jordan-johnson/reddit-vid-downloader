import os
import unittest
from WebRequest import WebRequest
from AudioVideoMerger import AudioVideoMerger

class AudioVideoMergerTestCase(unittest.TestCase):
	merger = None

	def setUp(self):
		web = WebRequest()
		self.merger = AudioVideoMerger()

		if not os.path.isfile('downloads/test_audio.mp4'):
			web.download('https://v.redd.it/i2h1g7n9sdy11/audio', 'test_audio.mp4')

		if not os.path.isfile('downloads/test_video.mp4'):
			web.download('https://v.redd.it/i2h1g7n9sdy11/DASH_9_6_M', 'test_video.mp4')

	def test_convert_mp4_to_mp3(self):
		self.merger.convert_mp4_to_mp3('test')

		path = os.path.isfile('downloads/test_audio.mp3')

		self.assertTrue(path)

	def test_merge(self):
		self.merger.merge('test')

		path = os.path.isfile('downloads/test_merged.mp4')

		self.assertTrue(path)

		self.merger.clean_up('test')

		if os.path.isfile('downloads/test_merged.mp4'):
			os.remove('downloads/test_merged.mp4')

	def main(self):
		unittest.main()
