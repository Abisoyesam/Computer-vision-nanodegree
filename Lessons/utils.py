def rgb2hsv(Red, Green, Blue):
	"""
	:param Red: the value of red color ranges from 0 - 255
	:param Green: the value of green color ranges from 0 - 255
	:param Blue: the value of blue color ranges from 0 - 255
	"""
	r,g,b = Red/255, Green/255, Blue/255
	vmax = max(r,g,b)
	vmin = min(r,g,b)
	diff = vmax - vmin

	v = vmax

	if vmax == 0:
		s = 0
	else:
		s = diff/vmax

	if vmax == r:
		h = (60 * (g-b)/diff) % 360
		# modulus of 360 b'cos h ranges from 0 - 360
	elif vmax == g:
		h =  (120 + (60 * (b-r)/(diff)) % 360)
	elif vmax == b:
		h = (240 + (60 * (r-g)/(diff)) % 360)

	return h,s,v



def load_dataset(dir):
	pass

print(rgb2hsv(100,200,50))