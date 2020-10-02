import dns.resolver

import subprocess


VERBOSE = True

for n in ['www.goog.co.uk']:
    print(n)
    results = []
    for server in ['8.8.8.8']:
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
            if VERBOSE:
                print("%s: %s" % (server, answer))
        except Exception as exc:
            print("%s: Error: %s" % (server, str(exc)))


