# formal grammar for JSON describes key (or name) to be `{"characters"}``

def dump_value(f):
    print("***********GOT IT*************")
    with open('result.json', 'w') as fd:
        # since we have found a key, the previous character must have been a {, so
        # find the matching { and that should be the end of this keys value
        brackets = 1
        c = f.read(1)

        in_str = False
        square_count = 0
        curly_count = 0

        while brackets > 0 and c:
            if c == '{':
                brackets += 1
            elif c == '}':
                brackets -= 1
            # enter or exit string
            if c == '"':
                in_str = not in_str

            # arrays
            if c == '[':
                square_count += 1
            if c == ']':
                square_count -= 1

            # objects
            if c == '{':
                curly_count += 1
            if c == '}':
                curly_count -= 1

            if square_count == 0 and curly_count == 0 and not in_str and c == ',':
                brackets = 0
            if brackets > 0:
                fd.write(c)
            c = f.read(1)

# key to find
KEY = 'GlossSeeAlso'
data = 'test1.json'

tokens = ''
with open(data) as f:
    c = f.read(1)

    in_str = False
    tokens = ''
    while(c):
        if c == '"':
            in_str = not in_str
        if in_str:
            tokens += c
        if c == ',' and not in_str:
            tokens = ''
        if c == ':' and not in_str:
            key = tokens.strip().strip('"')
            if KEY == key:
                dump_value(f)
                break
            else:
                tokens = ''
        c = f.read(1)
