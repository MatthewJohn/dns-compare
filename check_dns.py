
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

servers = sys.argv[0].split(',')
domains = sys.argv[1].split(',')

for n in domains:
    v_print(n)
    results = []
    for server in servers:
        my_resolver = dns.resolver.Resolver()
        my_resolver.timeout = 1
        my_resolver.lifetime = 1
        my_resolver.nameservers = [server]
        try:
            res = my_resolver.query(n)
            answer = ','.join(sorted([str(r) for a in res.response.answer for r in a.items ]))
            if answer not in results:
                if results:
                    #print "%s: %s" % (server, answer)
                    True
                results.append(answer)
            #print(results)
            v_print("%s: %s" % (server, answer))
        except Exception as exc:
            print("%s: Error: %s" % (server, str(exc)))


