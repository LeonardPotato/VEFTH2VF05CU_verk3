import os
from bottle import route, run, template, static_file, error


frettir = [
    {
        'fyrirsogn': 'Obama hjónin mættu í baguette átkeppni í parís',
        'texti': 'Fólk var að háma í sig sem flest baguette í parís, í fyrstu verðlaun voru ársbirgðir af crépes. Michelle Obama hafnaði í 2.sæti.'
                 'Barrack Obama var í 1.sæti. Obama hefur nú fengið viðurnefnið Baguette Obama.',
        'mynd': 'baguetteobama.jpg',
        'email': 'eas@frettir.is'
    },
    {

        'fyrirsogn': 'Krakow útihátíð',
        'texti': 'Haldin var útihátíð í krakow, póllandi.', #her er nafn fyrir textann sem skal birta
        'mynd': 'krakow.jpg', #her seturu nafnið a myndinni sem þu vilt birta
        'email': 'eas@frettir.is'
    },
    {
        'fyrirsogn': 'Counterstrike mót haldið í Cologne',
        'texti': 'ESL One Cologne var haldið í Lanxess arena.',
        'mynd': 'cologne.jpg',
        'email': 'eas@frettir.is'
    },
    {
        'fyrirsogn': 'Tónlistarhátíð Berlin',
        'texti': 'Stór og mikil tónlistarhátíð var haldin 31.Janúar í berlín',
        'mynd': 'berlin.jpg',
        'email': 'eas@frettir.is'
    }
]

@route('/')
def index():
    return template('verk3')

@route('/a')
def lidura():
    return template('lidura')

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('kennitala.tpl',kennitala=kennitala)

@route('/b')
def lidurb():
    return template('index',frettir=frettir)

@route('/frett/<n>')
def frett(n):
    return template('frett',n=n, frettir=frettir)

#static file routing

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./myfiles')

@error(404)
def error404(error):
    return 'Villa 404, Ekkert fannst.'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
