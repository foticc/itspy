def pl(text):
	def log(fun):
		def fvc(*args,**kw):
			print 'pre'+text
			return fun(*args,**kw)
		return fvc
	return log
@pl("123")
def pr():
	print 'mid'

if __name__ == '__main__':
	pr()