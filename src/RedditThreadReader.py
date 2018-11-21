from WebRequest import WebRequest

class RedditThreadReader:
	web = WebRequest()

	thread_addr = None
	thread_id = None
	thread_json = None

	video_addr = None
	video_path = None
	audio_addr = None
	audio_path = None

	def read(self):
		self.thread_addr = input('Enter reddit thread URL:')
		self.thread_json = self.web.request_json(self.thread_addr + ".json")

		self.parse()
		self.download()

	def parse(self):
		if(self.thread_json is None):
			raise Exception('JSON data not found; could not parse data.')

		tmp_data = self.thread_json[0]["data"]["children"][0]["data"]
		tmp_media = tmp_data["media"]

		self.thread_id = tmp_data["id"]
		self.video_addr = tmp_media["reddit_video"]["fallback_url"]
		self.audio_addr = self.video_addr.split("DASH_")[0] + "audio"

	def download(self):
		if any([self.audio_addr is None, self.video_addr is None, self.thread_id is None]):
			raise Exception('Missing information required to download audio and video files. Try again.')

		print('Attempting to download audio and video...')

		self.audio_path = self.web.download(self.audio_addr, self.thread_id + '_audio.mp4')
		self.video_path = self.web.download(self.video_addr, self.thread_id + '_video.mp4')