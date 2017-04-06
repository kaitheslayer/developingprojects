# This script will support downloading files form any url, as well as the ability to install python files


import urllib3

def configr(vars, filename, section):
    import configparser
    c = configparser.ConfigParser()
    c.read(filename)
    r = []
    for _ in vars:
        a = c.get(section, _)
        r.append(a)
    return r

def writer (fname, data, sep):
    z = open(fname, 'w')
    for x in data:
        z.write (x)
        z.write (sep)
    z.close()

def ssetup(op):
    if op == "init":
        print("Lets start by setting up some options")
        md = "maxdwn_size: " + input("Max download size in MB?, use * for unlimited. (Note: File size can only be read from websites with content size headers)")
        cd = "confirm_download: " + input("Confirm download prompt. (yes / no)")
        print("Thanks, other options can be set in the config.ini file")
        writer('config.ini', ["[Config]","setup: yes", md, cd], '\n')



setup, maxdwn, cdown = configr(['setup','maxdwn_size','confirm_download'],'config.ini', 'Config')

print("Welcome to the python downloader")

if setup != "yes":
    a =input("Would you like to run the setup?(y/n)")
    if a.lower() == "y":
        ssetup('init')

print("Type a command to get started...")
while True:
    com = input().split()
    if com[0] == "dwn":
        try:
            com.pop(0)
            d = {com[0]: com[1]}
            print(d['url'])

            name = d['url'].split('/')[-1]
        except:
            print("Invalid arguments given. (e.g use: dwn url http://go.com/file.zip)")


        try:
            http = urllib3.PoolManager()
            response = http.request('GET', d['url'], preload_content=False)
            size = int(response.headers.get("Content-Length")) / 1048576

            if cdown == "yes":
                print ("Are you sure you want to download %s (%sMB)? (y/n)" %(name, size))
                if input().lower() == "y":
                    with open(name, 'wb') as f:
                        f.write(response.data)
                    response.release_conn()
                    print ("Download Complete...")

        except:
            print("A download error occured. Could not fetch file.")



    else:
        print("No command found...")
