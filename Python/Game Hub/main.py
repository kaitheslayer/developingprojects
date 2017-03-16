import pymysql



def ghsetup (username, pkey, pswd):
    global ghconnect
    ghconnect = pymysql.connect(host='sweb.ga', port=3306, user='sweb_' + username , passwd= pswd, db='sweb_' + pkey)
    global loggedin
    loggedin = "false"

def ghlogin(username, password):
    global ghconnect
    execu = ghconnect.cursor()
    execu.execute("SELECT * FROM blackjack WHERE username='%s' AND password='%s'" % (username, password))
    global user
    user = execu.fetchone()
    return "An error Occured"




# ================= EXAMPLES =====================

ghsetup(username="mainapp", pkey="gamehub", pswd="314159")

if loggedin == "false":
    s = input("Do you have a sweb account? (y/n)")
    if s == "y":
        uname = input("Whats Your Username?")
        ghlogin(username=uname, password=pas)
        
    if s == "n":
        uname = input("Create username")

print (user)
