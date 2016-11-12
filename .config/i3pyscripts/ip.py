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




print(external_ip())
