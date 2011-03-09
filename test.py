from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import web
import tornado.options

class TestApp(web.Application):
	def __init__(self):
		handlers = [
			(r'/', TestHandler),
		]
		
		settings = {}
		
		web.Application.__init__(self, handlers, **settings)

class TestHandler(web.RequestHandler):
	def get(self):
		self.write("Beat it, punks!")

if __name__ == "__main__":
	# from optparse import OptionsParser
	# parser = OptionsParser()
	tornado.options.define('port', default=5000, type=int, 
		metavar='PORT', help='set which port on which the application will listen')
	tornado.options.define('address', default="", type=str, 
		metavar='ADDR', help='address of the interface the server binds to')
	tornado.options.parse_command_line()
	
	server = HTTPServer(TestApp())
	server.listen(tornado.options.options.port, tornado.options.options.address)
	IOLoop.instance().start()
