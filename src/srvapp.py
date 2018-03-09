"""
Srv App
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from rx import Observable

from database import mongodb


define("port", default=8888, help="port", type=int)
define("mongoDb", default="mongodb+srv://localhost/test", help="MongoDB Connection String")
define("mongoDbDatabase", default="", help="Database")


class HelloWorldHandler(tornado.web.RequestHandler):
    """ HelloWorldHandler """

    def get(self, name="World"):
        self.write("Hello " + name)


class TemplateHandler(tornado.web.RequestHandler):
    """TemplateHandler"""

    def get(self, name):
        self.render("templates/TemplateHandler.html", title="yay", name=name)


class JsonEndpointHandler(tornado.web.RequestHandler):
    """JsonEndpointHandler"""

    def get(self, name="no_param"):
        items = {0: 'Python', 1: 'Nii', 2: name}
        self.set_header('Content-Type', 'text/javascript')
        self.write(items)


class ObservableHandler(tornado.web.RequestHandler):
    """ Ni"""

    def get(self):
        Observable.from_(["Knights", "Who", "Say", "Ni"]) \
            .filter(lambda string: len(string) > 2) \
            .subscribe(lambda value: self.write(value + " "))

        # yolo = Observable.from_(["Knights", "Who", "Say", "Ni"])
        # intervals = Observable.interval(1000)
        # Observable.zip(yolo, intervals, lambda s, i: (s, i)) \
        #     .subscribe(lambda value: print(value))


def main():
    """Main / entry """
    tornado.options.parse_command_line()
    tornado.options.parse_config_file("server.conf")

    db_con = mongodb.Connection().get_instance()
    print(db_con.countries.find_one())
    db2 = mongodb.Connection().get_instance()
    cursor = db2.countries.find()
    for document in cursor:
        print(document)

    application = tornado.web.Application([
        (r"/", HelloWorldHandler),
        (r"/json", JsonEndpointHandler),
        (r"/json/([a-zA-Z]+)", JsonEndpointHandler),
        (r"/([a-zA-Z]+)", TemplateHandler),
        (r"/ni/ops", ObservableHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
