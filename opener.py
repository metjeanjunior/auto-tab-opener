import webbrowser

url_list = ('google.com', 'example.com')
always_open_cmd = True
always_load_url_list = True

if always_open_cmd:
	url_list = () if not always_load_url_list else url_list
	print 'Please type the links you\'d like to open.'

	while True:
		print 'You can either enter a new link or type done.'
		res = raw_input('>>>')

		if res == 'done':
			break
		url_list += (res, )
		print 'added %s to url_list' % res
		print 'your list is now: ', url_list[0]

for url in url_list:
	webbrowser.get('chrome %s').open('http://www.google.com')