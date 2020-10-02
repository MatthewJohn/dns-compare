
import sys

import dns.resolver


VERBOSE = True

def v_print(words):
    """Print if verbose."""
    if VERBOSE:
        print(words)

if len(sys.argv) != 3:
    raise Exception(
        'Invalid arguments: Usage: '
        'check_dns.py dns-server1,dns-server2,.. domain.to.resolv,google.co.uk,...'
    )

servers = sys.argv[1].split(',')
domains = sys.argv[2].split(',')

resolvers = {}

for domain in domains:
    v_print("Checking Domain: {0}".format(domain))

    for server in servers:
        if server not in resolvers:
            resolvers[server] = dns.resolver.Resolver()
            resolvers[server].timeout = 1
            resolvers[server].lifetime = 1
            resolvers[server].nameservers = [server]
        try:
            res = resolvers[server].query(domain)
            answer = ','.join(sorted([str(r) for a in res.response.answer for r in a.items]))
            #print(results)
            v_print("%s: %s" % (server, answer))
        except Exception as exc:
            print("%s: Error: %s" % (server, str(exc)))


