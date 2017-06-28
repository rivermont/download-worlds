
import time as t
def get_time():
	return t.strftime('%H:%M:%S')

print('[{0}] [INIT]: Importing required libraries.'.format(get_time()))

import urllib.request
import shutil
import sys

try:
	todo = int(sys.argv[1])
except IndexError:
	print('[{0}] [ERR]: Please enter a number of images to get.'.format(get_time()))
	sys.exit()
except ValueError:
	print('[{0}] [ERR]: Please enter a valid number.'.format(get_time()))
	sys.exit()

try:
	for i in range(todo):
		url = 'http://worldgen.bin.sh/worldgen.cgi?palette=Atlas&iter=9000&pct_ice=10&height=1000&rotate=0&pct_water=60&projection=Square&seed={0}'.format(i)
		print('[{0}] [WORK]: Saving {1}.png'.format(get_time(), str(i)))
		with urllib.request.urlopen(url) as response, open(str(i) + '.png', 'wb+') as saveFile:
				shutil.copyfileobj(response, saveFile)
except KeyboardInterrupt:
	print('[{0}] [ERR]: User performed a keyboard interrupt. Stopping...'.format(get_time()))
