import time

def log(text):
	def abc(func):
		def wrapper(*args, **kw):
			print '%s call %s():'%(text,func.__name__)
			return func(*args, **kw)
		return wrapper
	return abc

@log("abc")
def now():
    print '2013-12-25'
now()
