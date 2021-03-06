#!/usr/bin/env python
# -*- coding: utf8 -*-
from libs.libs import WSGIApplication, BaseHandler
from libs.BeautifulSoup import BeautifulStoneSoup, Tag
from libs.pyquery.pyquery import PyQuery as pq
import re

config = {}
config['webapp2_extras.sessions'] = {
	'secret_key': '321ertrere5',
}
app = WSGIApplication(debug=False,
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


@app.route('/ekstruzionno-vyduvnye-mashiny')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/ekstruzionno-vyduvnye-mashiny.html')


@app.route('/ekstruzionno_vyduvnoi_avtomat_dhd-1lii')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/ekstruzionno_vyduvnoi_avtomat_dhd-1lii.html')


@app.route('/dhd-qr100-oborudovanie_dlia_proizvodstva_plastikovoi_tary')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/dhd-qr100-oborudovanie_dlia_proizvodstva_plastikovoi_tary.html')


@app.route('/seriia_vyduvnykh_mashin_dhd-l-a_dlia_proizvodstva_plastikovoi_tary')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/seriia_vyduvnykh_mashin_dhd-l-a_dlia_proizvodstva_plastikovoi_tary.html')


@app.route('/dhb-82pc-oborudovanie_dlia_proizvodstva_butylei')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/dhb-82pc.html')


@app.route('/ekstruzionno_vyduvnoe_oborudovanie_dhb80-110_dlia_proizvodstva_emkostei')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/dhb-80-100.html')


@app.route('/dhb-250a_dhb-250b_dhb-500_dhb-1000-oborudovanie_dlia_proizvodstva_plastikovykh_bochek')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/dhb-250-1000.html')


@app.route('/vyduvnye_mashiny_dhd-2lii_dhd-5lii_dhd-12lii_dhd-16lii')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/dhd-2lii-16lii.html')


@app.route('/ekstruzionno_vyduvnaia_mashina_dhd-30lii')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('extr/dhd-30lii.html')


@app.route('/sitemap')
class UserList(BaseHandler):
	def get(self):
		return self.render_response('pages/sitemap.html')


@app.route('/table')
class Table(BaseHandler):
	def post(self):
		rv = self.request.POST['txt']
		html = BeautifulStoneSoup(rv, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

		[tag.extract() for tag in html.findAll(['title', 'head'])]

		#clean all p tags in table
		table = html.find('table')
		if table:
			[tag.replaceWith(tag.renderContents()) for tag in table.findAll('span')]
			[tag.replaceWith(tag.renderContents()) for tag in table.findAll('p')]

		[tag.extract() for tag in html.findAll('a')]
		for tag in html.findAll('span', style=re.compile("text-decoration:underline")):
			tag.name = 'a'
		for tag in html.findAll('span', style=re.compile("font-style:italic;")):
			tag.name = 'em'
		for tag in html.findAll('span', style=re.compile("font-weight:bold")):
			tag.name = 'strong'
			tag.attrs = []
		for tag in html.findAll('p'):
			for title in tag.findAll(text=re.compile("H2 ")):
				tag.name = 'h2'
				tag.string = title.replace('H2', '').strip()
			for title in tag.findAll(text=re.compile("H3 ")):
				tag.name = 'h2'
				tag.string = title.replace('H3', '').strip()
			for title in tag.findAll(text=re.compile("Title.*")):
				tag.replaceWith(tag.renderContents())


		#clean all span tags
		[tag.replaceWith(tag.renderContents()) for tag in html.findAll('span')]
		#set header to table, and th tags instead of td for titles
		for tr in html.findAll('tr'):
			tr.find('td').name = 'th'
		if html.find('tr'):
			for td in html.find('tr').findAll('td'):
				td.name = 'th'
			thead = Tag(html, name='thead')
			thead.insert(0, html.find('tr'))
			html.find('table').insert(0, thead)
		#erase all attrs for all tags
		for tag in html.findAll(True):
			tag.attrs = []

		for tag in html.findAll('img'):
			tag.attrs = [('src', ''), ('alt', 'tpa')]

		for tag in html.findAll('a'):
			tag.attrs = [('href', '')]
		if html.body:
			html = html.body
		return self.render_response('pages/table.html',
		                            html=html.renderContents().replace('</img>', '').replace('<p></p>', '').decode(
			                            'utf8'))

	def get(self):
		return self.render_response('pages/table.html', html='')

@app.route('/table2')
class Table(BaseHandler):
	def get(self):
		return self.render_response('pages/table2.html', html='')

@app.route('/test')
class Table(BaseHandler):
	def get(self):
		host = self.request.host
		return self.render_json([host])
