import os
import re
import tempfile

atom_file_path = 'public/atom.xml'

print('Handling RSS start...')

with tempfile.NamedTemporaryFile(dir='.', delete=False) as tmp, \
        open(atom_file_path, 'r', encoding='utf-8') as f:

    content = f.read()
    # ? means no eager
    pattern = r'src="(/images/loading/loading.svg)" data-original="(.+?)"'
    repl = r'src="\2" data-original="\2"'
    result, n = re.subn(pattern, repl, content)

    tmp.write(result.encode('utf-8'))


os.replace(tmp.name, atom_file_path)

print('Success!!')
