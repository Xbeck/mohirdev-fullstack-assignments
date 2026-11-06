"""Reconstruct reviewed source files from SOURCE_FILES.json. Python 3.10+."""
import json
from pathlib import Path
base=Path(__file__).resolve().parent
out=base/'source'
for name,content in json.loads((base/'SOURCE_FILES.json').read_text(encoding='utf-8')).items():
    target=(out/name).resolve()
    if not target.is_relative_to(out.resolve()): raise ValueError('Invalid path')
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(content,encoding='utf-8')
print('Sources extracted into',out)
