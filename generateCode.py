#===============================================================================
# Script provided by Vinod Halaharvi, vinod.halaharvi@gmail.com
# RTP Network Services, Inc. / 904-236-6993 ( http://www.rtpnet.net )
# DESCRIPTION: Python code generator program   , read in a dictionary structure 
# generate python code for it
#===============================================================================
import ast
import sys

class CodeGeneratorDispatcher(object):
	"""docstring for CodeGeneratorDispatcher"""
	def __init__(self, fileString, handler):
		super(CodeGeneratorDispatcher, self).__init__()
		self.fileString = fileString
		self.root = ast.literal_eval(self.fileString) 
		self.handler = handler
		self.idnt = 0

	def generateCode(self):
		"""docstring for """
		for gkey, packages in  self.root.items():
			for package in packages: 
				self.handler.printPackage(package, self.idnt)
				self.handler.printBranding(package, self.idnt)
				self.handler.printalls(package, self.idnt)
				self.idnt = 0 
				for cls in  package["classes"]:
					self.handler.printClass(package,cls, self.idnt)
					self.idnt += 1
					self.handler.setupInit(package, cls, self.idnt)
					for getter in cls["getters"]:
						self.handler.printGetter(package, cls, getter, self.idnt)
						print
					for setter in cls["setters"]:
						self.handler.printSetter(package, cls, setter, self.idnt)
						print

class CodeGeneratorHandler(object):
	"""docstring for CodeGeneratorHandler"""
	def __init__(self, ):
		super(CodeGeneratorHandler, self).__init__()

	def printBranding(self, package, idnt):
		"""docstring for printBranding"""
		print package["branding"]

	def printalls(self, package, idnt):
		"""docstring for printalls"""
		packageString = "%s= %s" % ("__all__", str(package["__all__"]))
		print packageString

	def printPackage(self, package, idnt):
		"""docstring for printPackage"""
		pass

	def printClass(self, package, cls, idnt):
		"""docstring for printClass"""
		print "%sclass %s(%s):" % ("\t"*idnt, cls["name"], ",".join(cls["bases"]))

	def setupInit(self, package, cls, idnt):
		"""docstring for setupInit"""
		print "%s\"\"\"docstring for %s\"\"\"" % ("\t" * idnt, cls["name"])
		print """%sdef __init__(self, ):\n%ssuper(%s, self).__init__()""" % ("\t" * idnt, "\t"*(idnt+1), cls["name"])
		print

	def printSetter(self, package, cls, setter, idnt):
		p = ("\t"*idnt,) +  (setter.title(),) + (setter,) + ("\t"*(idnt+1),) + (setter.title(),) + ("\t"*(idnt+1),) + (setter,)*2
		"""docstring for printSetter"""
		print """%sdef set%s(self, %s):\n%s\"\"\"docstring for set%s\"\"\"\n%sself.%s = %s""" % p

	def printGetter(self, package, cls, getter, idnt):
		p = ("\t"*idnt,) +  (getter.title(),) + (getter,) + ("\t"*(idnt+1),) + (getter.title(),) + ("\t"*(idnt+1),) + (getter,)
		"""docstring for printSetter"""
		print """%sdef get%s(self, %s):\n%s\"\"\"docstring for get%s\"\"\"\n%sreturn self.%s""" % p


if __name__ == '__main__':
	ch = CodeGeneratorHandler()
	cg = CodeGeneratorDispatcher(sys.stdin.read(), ch)
	cg.generateCode()


