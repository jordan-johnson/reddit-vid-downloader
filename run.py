from WebRequest import WebRequest
from RedditThreadData import RedditThreadData

class ApplicationMain:

	def __init__(self):
		web = WebRequest()
		data = RedditThreadData(web)

app = ApplicationMain()