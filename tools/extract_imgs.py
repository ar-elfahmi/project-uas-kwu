import re, base64, os
src = r'D:\08_CodeKuliah\project-uas-kwu\UTS_KWU-TI_Tim1_Tumbuh-in-AI FINAL.md'
out = r'D:\08_CodeKuliah\project-uas-kwu\output\img'
os.makedirs(out, exist_ok=True)
txt = open(src, encoding='utf8').read()
for m in re.finditer(r'^\[(image\d+)\]:\s*<data:image/(\w+);base64,([A-Za-z0-9+/=]+)>', txt, re.M):
    name, ext, data = m.groups()
    p = os.path.join(out, 'uts_%s.%s' % (name, ext))
    open(p, 'wb').write(base64.b64decode(data))
    print(p, os.path.getsize(p))
