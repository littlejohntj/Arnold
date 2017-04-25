import urllib


def image_to_ascii(img):
	str1 = 'http://www.degraeve.com/img2txt-yay.php?url='
	str2 = '&mode=A&size=100&charstr=ABCDEFGHIJKLMNOPQRSTUVWXYZ&order=O&invert=N'
	url = str1 + img + str2
	f = urllib.urlopen(url)
	#return f.read().split('<pre>')[1].split('</pre>')[0]
	return '\n'.join([" ".join(list(l)) for l in f.read().split('<pre>')[1].split('</pre>')[0].split('\n')])

	
