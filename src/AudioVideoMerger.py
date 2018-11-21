import os
import sys
import ffmpeg

class AudioVideoMerger:
	directory = 'downloads/'

	def convert_mp4_to_mp3(self, filename):
		path = self.directory + filename + '_audio.mp4'

		try:
			audio = ffmpeg.input(path)
			audio = ffmpeg.output(audio, self.directory + filename + '_audio.mp3')

			ffmpeg.run(audio)

		except ffmpeg.Error as e:
			print(e.stderr, file=e.stderr)
			sys.exit(1)

	def merge(self, filename):
		try:
			path = self.directory + filename
			audio = ffmpeg.input(path + '_audio.mp3')
			video = ffmpeg.input(path + '_video.mp4')
			stream = ffmpeg.output(audio, video, path + '_merged.mp4')

			ffmpeg.run(stream)
		except ffmpeg.Error as e:
			print(e.stderr, file=e.stderr)
			sys.exit(1)

	def clean_up(self, filename):
		path = self.directory + filename

		if os.path.isfile(path + '_audio.mp3'):
			os.remove(path + '_audio.mp3')

		if os.path.isfile(path + '_video.mp4'):
			os.remove(path + '_video.mp4')

		if os.path.isfile(path + '_audio.mp4'):
			os.remove(path + '_audio.mp4')

	def attempt(self, filename):
		self.convert_mp4_to_mp3(filename)
		self.merge(filename)
		self.clean_up(filename)