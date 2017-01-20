
import string
import random

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
	new_code = code_generator(size=size)
	Klass = instance.__class__
	qs_exist = Klass.objects.filter(shortcode=newcode)
	if qs_exists:
		return create_short_code(size=size)
	return new_code


