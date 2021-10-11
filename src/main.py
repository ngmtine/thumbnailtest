# 以下のコードはシステムにatomicparsleyが無いとサムネの設定に失敗するはず

import sys
from youtube_dl import YoutubeDL

def downloadm4a(url: str):
	opts = {
		"outtmpl": '%(title)s.%(ext)s',
		"format": "bestaudio[ext=m4a]",
		"writethumbnail": True,
		'postprocessors': [{
			'key': 'EmbedThumbnail',
		}],
		}
	try:
		with YoutubeDL(opts) as ydl:
			result = ydl.download([url])
	except Exception as e:
		print(e)
		return False
	return result

if __name__ == "__main__":
	downloadm4a(sys.argv[1])

