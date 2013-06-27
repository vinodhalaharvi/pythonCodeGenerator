# input to this program	
	{
		"packages": [
			{
				"name": "threadpool", 
				"__all__": ["Task", "TaskHandler",],
				"branding": "###\n#Author: Vinod Halaharvi\n###",
				"classes": [
					{
						"name": "Threadpool",
						"attributes": ["attr1", "attr2"], 
						"bases":["object",],
						"getters":["taskName",], 
						"setters":["taskName", "handler"], 
						"main": True, 
					}, 	
				], 	
			},

			{
				"name": "rtputils", 
				"__all__": ["HQapi", ],
				"branding": "###\n#Author: Vinod Halaharvi\n###",
				"classes": [
					{
						"name": "HQapi",
						"attributes": ["attr1", "attr2"], 
						"bases":["object",],
						"getters":["url",], 
						"setters":["url", "host"], 
						"main": True, 
					}, 	
				], 	
			},
		],
	}

# Will generate this output

	###
	#Author: Vinod Halaharvi
	###
	__all__= ['Task', 'TaskHandler']
	class Threadpool(object):
		"""docstring for Threadpool"""
		def __init__(self, ):
			super(Threadpool, self).__init__()

		def getTaskname(self, taskName):
			"""docstring for getTaskname"""
			return self.taskName

		def setTaskname(self, taskName):
			"""docstring for setTaskname"""
			self.taskName = taskName

		def setHandler(self, handler):
			"""docstring for setHandler"""
			self.handler = handler

	###
	#Author: Vinod Halaharvi
	###
	__all__= ['HQapi']
	class HQapi(object):
		"""docstring for HQapi"""
		def __init__(self, ):
			super(HQapi, self).__init__()

		def getUrl(self, url):
			"""docstring for getUrl"""
			return self.url

		def setUrl(self, url):
			"""docstring for setUrl"""
			self.url = url

		def setHost(self, host):
			"""docstring for setHost"""
			self.host = host

