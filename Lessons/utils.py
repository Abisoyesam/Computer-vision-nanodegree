def rgb2hsv(R,G,B,scaleFactor=100):
	'''	
	To convert rgb color to hsv color space
	:params: r -> It is the red color code
	:params: g -> It is the green color code
	:params: b -> It is the blue color code
	'''
	r, g, b = R/255, G/255, B/255
	vmax = max(r,g,b)
	vmin = min(r,g,b)
	diff = vmax - vmin

	if vmax == vmin:
		h = 0
	elif vmax == r:
		h = (60 * ((g-b)/diff)+0)%360
	elif vmax == g:
		h = (60 * ((b-r)/diff)+120)%360
	elif vmax == b:
		h = (60 * ((r-g)/diff)+240)%360

	if h < 0:
		h = h+360
	if vmax == 0:
		s = 0
	else:
		s = (diff/vmax)* scaleFactor

	v = scaleFactor * vmax
	return h,s,v
