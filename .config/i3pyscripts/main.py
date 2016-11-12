from i3pystatus import Status
import socket, requests, json, os, re


def external_ip(myformat="{hostname} ({country})"):
    if not os.path.isfile('ip.txt'):
        resp = requests.get("http://ifconfig.co/json")
        resp.close()
        if resp.ok:
            f = open('ip.txt','w')
            f.write(resp.text)
            f.close()
        else:
            f = open("ip.txt", 'w')
            a = {
                "ip":str(resp.status_code),
                "ip_decimal":str(resp.status_code),
                "country":resp.reason,
                "city":resp.reason,
                "hostname":str(resp.status_code)
            }
            f.write(json.dumps(a))
            f.close()
    else:
        f = open('ip.txt','r')
        ff = f.read()
        f.close()
        #try:
        ext_ip_info = json.loads(ff)
        s = myformat
        s = re.compile("\{ip\}").sub(ext_ip_info['ip'],s)
        #s = re.compile("\{ip_decimal\}").sub(ext_ip_info['ip_decimal'],s)
        s = re.compile("\{country\}").sub(ext_ip_info['country'],s)
        s = re.compile("\{city\}").sub(ext_ip_info['city'],s)
        s = re.compile("\{hostname\}").sub(ext_ip_info['hostname'],s)
        return s
        #except TypeError:
        #    return "JSON error"
        #except:
        #    return "Error"



status = Status()

#status.register("clock",format = { '%y %a %b %-d %X'} )
status.register("clock",format = { '%y-%m-%-d %X'} )
status.register("clock",format = { '%A %V'})


status.register("text",
    text="IP: %s / %s" % (socket.gethostbyname(socket.gethostname()) , external_ip("{hostname} ({country})") )  )


status.register("disk",
    path="/",
    format="Root: {avail}G",)

status.register("disk",
    path="/home/",
    format="Home: {avail}G",)

status.register("mem")


status.run()