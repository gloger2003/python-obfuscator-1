import io
import tokenize
from typing import Dict, List
import keyword




# print('sum'.isidentifier())

name_mapping: Dict[str, str] = {}
i = 0


def create_name():
    global i
    name = f'_n{i}'
    i += 1
    return name


with open('./test.py', 'rb') as f:    
    tokens = [k for k in tokenize.tokenize(f.readline)]
    new_tokens: List[tokenize.TokenInfo] = []
    
    is_import = False

    for index, t in enumerate(tokens):
        name = t.string
        
        print(t)

        if name in ('import', 'from'):
            new_tokens.append(t)
            is_import = True
            continue
        
        if t.type == tokenize.NEWLINE or t.type == tokenize.NL:
            is_import = False

        if is_import:
            if not keyword.iskeyword(name):
                name_mapping[name] = name
            new_tokens.append(t)
            continue
        
        if index > 0 and keyword.iskeyword(tokens[index - 1]):
            new_tokens.append(t)
            continue
        
        if name.isidentifier() and not keyword.iskeyword(name) and not name.startswith('__'):    
            try:
                if type(print) == eval(f'type({name})'):
                    new_tokens.append(t)
                    continue
            except NameError:
                pass
            
            if name_mapping.get(name) is None:
                new_name = create_name()
                new_t = tokenize.TokenInfo(t.type, new_name, t.start, t.end, t.line)
                new_tokens.append(new_t)
                print(new_t)
                name_mapping[name] = new_name
            else:
                new_t = tokenize.TokenInfo(t.type, name_mapping[name], t.start, t.end, t.line)
                new_tokens.append(new_t)
        else:
            new_tokens.append(t)
            print(t)

    data = tokenize.untokenize(new_tokens)
    
    
with open('./test_obf.py', 'wb') as f:
    f.write(data)
    
    
print(name_mapping)