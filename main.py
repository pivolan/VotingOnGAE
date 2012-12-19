#!/usr/bin/env python
# -*- coding: utf8 -*-
from libs.libs import WSGIApplication, BaseHandler
from libs.BeautifulSoup import BeautifulStoneSoup

config = {}
config['webapp2_extras.sessions'] = {
	'secret_key': '321ertrere5',
}
app = WSGIApplication(debug=True,
                      config=config)

@app.route('/')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/main.html')


@app.route('/proizvodstvennye-linii-iz-kitaya')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/proizvodstvennye-linii-iz-kitaya.html')


@app.route('/mini-zavody-iz-kitaya')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/mini-zavody-iz-kitaya.html')


@app.route('/oborudovanie-iz-kitaia')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/oborudovanie-iz-kitaia.html')


@app.route('/uslugi-kompanii-bereg')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/uslugi-kompanii-bereg.html')


@app.route('/poisk-proizvoditelei-i-tovarov-v-kitae')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/poisk-proizvoditelei-i-tovarov-v-kitae.html')


@app.route('/about-us')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/about-us.html')


@app.route('/contacts')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/contacts.html')


@app.route('/articles')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/articles.html')


@app.route('/etapy-postavki-tovarov-i-oborudovaniia')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/etapy-postavki-tovarov-i-oborudovaniia.html')


@app.route('/perevod-s-kitayskogo-i-na-kitayskiy-saytov-tekstov-dokumentov')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/perevod-s-kitayskogo-i-na-kitayskiy-saytov-tekstov-dokumentov.html')


@app.route('/termoplastavtomaty-kitay')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('tpa/termoplastavtomaty-kitay.html')


@app.route('/termoplastavtomat-<model>')
class UserList(BaseHandler):
	def get(self, model):
		return self.render_response('tpa/%s.html' % model)

@app.route('/table')
class Table(BaseHandler):
	def get(self):
		rv = self.jinja2.render_template('pages/table.txt')
		html = BeautifulStoneSoup(rv)
		[span.replaceWith(span.renderContents()) for span in html.findAll('span')]
		[span.replaceWith(span.renderContents()) for span in html.findAll('p')]
		for tag in html.findAll(True):
			tag.attrs = None
		return self.response.write(html.renderContents())

