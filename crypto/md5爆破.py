from hashlib import md5

tables = '0123456789abcdefghijklmnopqrstuvwxyz'

for i in tables:
    for j in tables:
        for k in tables:
            for l in tables:
                for m in tables:
                    c = 'qnfpgs{47r%s%s%s%s%s-5pqp-47q0-n5o4-912p00nr4qnp}' % (i, j, k, l, m)
                    if md5(c.encode()).hexdigest() == 'abfc064eec625a1fe487bda8c0995808':
                        print(c)
                        exit()