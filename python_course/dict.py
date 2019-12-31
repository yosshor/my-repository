from functools import reduce

def inverse_dict3(src):
    return reduce(lambda acc, curr: {
        **acc,
        curr[1]: acc.get(curr[1], []) + [curr[0]]
    }, src.items(), {})

def inverse_dict2(src):
    dst = {}
    for k, v in src.items():
        dst[v] = dst.get(v, []) + [k]
    return dst

def inverse_dict1(src):
    dst = {}
    for k, v in src.items():
        if v not in dst:
            dst[v] = []
        dst[v].append(k)
    return dst

def inverse_dict(src):
    dst = {}
    for k in src:
        v = src[k]
        if v not in dst:
            dst[v] = [k]
        else:
            dst[v].append(k)
    return dst

def main():
    src = { 'a': 3, 'z': 3, 'b': 2 }
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    dst = inverse_dict2(src)
    print(dst)
    print('')
    print('')
    print('')
    print('')

if __name__ == '__main__':
    main()
