#!/usr/bin/env python
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        links = collections.OrderedDict([
            ("Verkoop", "verkoop"),
            ("Stock", "stock"),
            ("Historiek", "historiek"),
        ])
        self.render('index.html', title='MijnWinkelApp', links=links)

# Put here yours handlers.

handlers = [(r'/', HomeHandler),
			()]
