import sys
from RedditThreadReader import RedditThreadReader
from AudioVideoMerger import AudioVideoMerger

class ApplicationMain:
	reader = RedditThreadReader()
	merger = AudioVideoMerger()

	def __init__(self):
		self.reader.read()
		self.merger.attempt(self.reader.thread_id)

app = ApplicationMain()