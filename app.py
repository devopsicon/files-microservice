# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import uuid
import glob
import sys

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        file_path = "./files/"+ str(self.get_argument("file_name"))
        self.set_header("content-type", "application/octet-stream")
        with open(file_path, 'rb') as f:
            while 1:
                data = f.read(16384) # or some other nice-sized chunk
                if not data: break
                self.write(data)
        self.finish()

    def post(self):
        # get post data
        file_body = self.request.files['file0'][0]['body']
        file_name = str(uuid.uuid4())
        with open('./files/'+file_name,'wb') as f:
            f.write(file_body)
        self.write(file_name)

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({'file_names':glob.glob("./files/*")})

def make_app():
    return tornado.web.Application([
        (r"/v1/file", MainHandler),
        (r"/v1/file/list", ListHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
