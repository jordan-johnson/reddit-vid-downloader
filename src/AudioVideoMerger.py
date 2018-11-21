import os
import sys
import ffmpeg

class AudioVideoMerger:
	def attempt(self, filename):
		print('Attempting to merge audio and video...')
		try:
			(
				ffmpeg
				.input('downloads/' + filename + '_audio.mp4')
				.output('downloads/' + filename + '_a.mp3')
				.run()
			)

			stream = ffmpeg.input('downloads/' + filename + '_a.mp3')
			stream = ffmpeg.input('downloads/' + filename + '_video.mp4')
			stream = ffmpeg.output(stream, 'downloads/' + filename + '_merged.mp4')
			ffmpeg.run(stream)
		except ffmpeg.Error as e:
			print(e.stderr, file=stderr)
			sys.exit(1)