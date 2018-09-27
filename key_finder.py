# formal grammar for JSON describes key (or name) to be `{"characters"}``

def dump_value(f):
    print("***********GOT IT*************")
    with open('result.json', 'w') as fd:
        # since we have found a key, the previous character must have been a {, so
        # find the matching { and that should be the end of this keys value
        brackets = 1
        c = f.read(1)
        in_str = False
        in_arr = False
        in_obj = False
        while brackets > 0 and c:
            print('c:', c, in_str)
            if c == '{':
                brackets += 1
            elif c == '}':
                brackets -= 1
            # enter or exit string
            if c == '"':
                in_str = not in_str

            # arrays
            if not in_str and c == '[':
                in_arr = True
            if not in_str and c == ']':
                in_arr = False

            # objects
            if not in_str and c == '{':
                in_obj = True
            if not in_str and c == '}':
                in_obj = False

            if not in_str and not in_arr and not in_obj and c == ',':
                brackets = 0
            if brackets > 0:
                fd.write(c)
            c = f.read(1)

# key to find
key = 'GlossList'
data = 'test1.json'

tokens = ''
with open(data) as f:
    c = f.read(1)
    in_str = False
    while(c):
        # skip escaped characters and spaces
        if c == '\\' or c == '{' or c == '}':
            c = f.read(1)
            continue
        print('c:', c, in_str)
        tokens += c
        print ('token:', tokens)
        if c == '"':
            in_str = True
            c = f.read(1)
            if c == ':':
                in_str = False
                tokens = tokens.strip().strip('"')
                print('KEY: ', tokens)
                if tokens == key:
                    # tokens should contain the whole key now, as well as leading and
                    # trailing "
                    dump_value(f)
                    break
                tokens = ''
            elif c == ',' or c == '}' or c == ']':
                in_str = False
                tokens = ''
            else:
                tokens += c
        if not in_str and c == ',':
            tokens = ''
        c = f.read(1)
