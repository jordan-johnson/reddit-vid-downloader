import os
import sys
import ffmpeg

class AudioVideoMerger:
	directory = 'downloads/'

	def convert_mp4_to_mp3(self, filename):
		path = directory + filename + '_audio.mp4'

		try:
			(
				ffmpeg
				.input(path)
				.output(directory + '_audio.mp3')
				.run()
			)
		except ffmpeg.Error as e:
			print(e.stderr, file=stderr)
			sys.exit(1)

	def merge(self, filename):
		try:
			path = directory + filename
			stream = ffmpeg.input(path + '_audio.mp3')
			stream = ffmpeg.input(path + '_video.mp4')
			stream = ffmpeg.output(stream, path + '_merged')
			ffmpeg.run(stream)
		except ffmpeg.Error as e:
			print(e.stderr, file=stderr)
			sys.exit(1)

	def attempt(self, filename):
		convert_mp4_to_mp3(filename)
		merge(filename)