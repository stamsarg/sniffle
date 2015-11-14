import bottle
@bottle.get('/signup')
@bottle.post('/signup')
def signup():
    with open('signup.html') as template:
        name = bottle.request.forms.get('name')
        email = bottle.request.forms.get('email')
        password1 = bottle.request.forms.get('password1')
        password2 = bottle.request.forms.get('password2')
        likes = bottle.request.forms.get('likes')
        well = ''
        no_content = ''
        for field in ["name", "email", "password1", "password2", "likes"]:
            if not bottle.request.forms.get(field):
                no_content = "You didn't fill all the fields"
            elif password2 != "":
                if password1 != password2:
                    well = "password doesn't match"
                else:
                    well = ''
                    with open('done.html') as template:
                        goto = bottle.request.forms.get('gotomain')
                        kindof = ''
                        if goto:
                            kindof = type(goto)
                        return bottle.template(template.read(), usrn = "username: ", realusrn = email, passw = "password: ",
                            realpassw = password2, type = kindof)


        return bottle.template(template.read(), okOrNot = well, no_content = no_content)

@bottle.get('/test')
def test2():
    see = 'look'
@bottle.get('/test2')
def test():

    return see

@bottle.get("/static/<filename:path>")
def static_file(filename):
    return bottle.static_file(filename, root="static/")
bottle.run(port=8080, debug=True)
