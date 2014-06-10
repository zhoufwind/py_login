database = {'stephen': '123'}

def lookup(name):
    'show the password if user exist/ return None if user don\'t exist.'
    return database.get(name)

def register():
    'Add user name and password into database'
    while True:
        name = raw_input('Add user name: ').lower()
        if not name:
            break
        if lookup(name):    # If user exist, re-enter user name
            print 'user exist!'
            break
        pwd = raw_input('Add user password: ').lower()
        database[name] = pwd

def login():
    'Login function'
    name = raw_input('Enter user name: ').lower()
    if lookup(name):
        for i in range(3):
            pwd = raw_input('Enter Password: ')
            if pwd == database[name]:
                login = True
                break
            else:
                login = False
                print 'Password Incorrect!'
        if login:
            print 'Login Success!! \nWelcome!!'
        else:
            print 'Login Failed'
    else:
        print ('User don\'t exist!!')

#print 'user\'s password: ', lookup('stephen')
#register()
login()