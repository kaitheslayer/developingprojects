import pymysql


def ghsetup (username, pkey, pswd):
    global ghconnect
    ghconnect = pymysql.connect(host='sweb.ga', port=3306, user='sweb_' + username , passwd= pswd, db='sweb_' + pkey)

def gamelogin(username, password):
    global ghconnect
    execu = ghconnect.cursor()
    execu.execute("SELECT * FROM blackjack WHERE username= " + username + " AND password= " + password)
    global user
    user = execu.fetchone()
    return "An error Occured"


ghsetup(username="mainapp", pkey="gamehub", pswd="31****")
gamelogin(username="kai", password="mypas")
print (user)
