import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="port", type=int)



class MainHandler(tornado.web.RequestHandler):
    def get(self, name = "World"):
           self.write("Hello " + name)

class TemplateHandler(tornado.web.RequestHandler):
    def get(self, name):
        self.render("templates/TemplateHandler.html", title="yay", name=name)

class JsonEndpointHandler(tornado.web.RequestHandler):
    def get(self, name="no_param"):
        items = {0:'Python', 1:'Nii', 2: name}
        self.set_header('Content-Type', 'text/javascript')
        self.write(items)

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/json", JsonEndpointHandler),
        (r"/json/([a-zA-Z]+)", JsonEndpointHandler),
        (r"/([a-zA-Z]+)", TemplateHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()