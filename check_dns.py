
import sys

import dns.resolver


VERBOSE = False
FAILED_RESULT = 'Failed'

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

results = {}

def add_result(domain, server, res):
    if domain not in results:
        results[domain] = {}

    if res not in results[domain]:
        results[domain][res] = []

    results[domain][res].append(server)


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
            add_result(domain, server, answer)
            v_print("%s: %s" % (server, answer))
        except Exception as exc:
            print("%s: Error: %s" % (server, str(exc)))
            add_result(domain, server, FAILED_RESULT)

    # Check results for domain
    if len(results[domain]) > 1:
        print("Domain has differing results: " + domain + " : " + str(results[domain]))
    elif FAILED_RESULT in results[domain]:
        print('Domain has failed results: ' + domain + ' : ' + str(results[domain]))

