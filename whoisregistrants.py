import os
import pprint

filepath = "hosts-grindr"
field = "Registrant Name"
results = {}

with open(filepath) as fd:
    for host in fd.readlines():
        host = host.strip()
        d = ".".join(host.split(".")[1:])
        c = 'whois ' + d + ' |grep "' + field + '"'
        print("? WHOIS query for " + host)
        w = os.popen(c).read().split(":")
        if len(w) > 1:
            print("  WHOIS reply " + " ".join(w[1:]))
            results[host] = w[1:]
        else:
            print(w)

# pprint.pprint(results)
