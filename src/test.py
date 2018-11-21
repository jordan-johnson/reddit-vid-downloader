import sys
from tests.web_request import WebRequestTestCase
from tests.reddit_thread_reader import RedditThreadReaderTestCase
from tests.audio_video_merger import AudioVideoMergerTestCase

if __name__ == '__main__':
	web_test = WebRequestTestCase()
	web_test.main()

	reddit_test = RedditThreadReaderTestCase()
	reddit_test.main()

	merge_test = AudioVideoMergerTestCase()
	merge_test.main()