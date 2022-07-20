import justpy as jp
def create_page():
    web=jp.QuasarPage()
    h1=jp.QDiv(a=web,text='Visualisation of the Course Data',classes='text-h3 q-pa-md text-center red-10 #33ccbd')
    p1=jp.QDiv(a=web,text='This web page contains the information about the course reviews data', classes='text-body1 text-left')
    return web
jp.justpy(create_page)
