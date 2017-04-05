# This will be a downloader

# Basic script
import urllib3

url = input("Enter url to file:")
name = url.split('/')[-1]
http = urllib3.PoolManager()

response = http.request('GET', url, preload_content=False)
size = int(response.headers.get("Content-Length")) / 1048576
print("Are you sure you want to download: " + name + " (" + str(size) +"MB)")
p = input ("Y (yes), N (no)")

if p.lower() == "y":
    with open(name, 'wb') as f:
        f.write(response.data)

    response.release_conn()

elif p.lower() == "n":
    print("Did not download...")
