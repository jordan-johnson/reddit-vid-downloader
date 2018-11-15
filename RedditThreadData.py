class RedditThreadData:
	web_request_obj = None

	thread_addr = None
	thread_json = None
	thread_id = None
	video_addr = None
	audio_addr = None

	def __init__(self, web_obj):
		self.web_request_obj = web_obj
		thread_addr = input('Enter reddit thread URL:')

		tmp_json = self.web_request_obj.request(thread_addr + ".json", True)

		self.parse(tmp_json)
		self.download()

	def parse(self, json):
		tmp_data = json[0]["data"]["children"][0]["data"]
		tmp_media = tmp_data["media"]

		self.thread_id = tmp_data["id"]
		self.video_addr = tmp_media["reddit_video"]["fallback_url"]
		self.audio_addr = self.video_addr.split("DASH_")[0] + "HLSPlaylist.m3u8"

	def download(self):
		self.web_request_obj.download(self.audio_addr, self.thread_id, 'm3u8')
		self.web_request_obj.download(self.video_addr, self.thread_id, 'mp4')