import openpyxl, re, sys
wb = openpyxl.load_workbook(sys.argv[1])
pat = re.compile(r'StokMudah|Honor|Co-working|Administrasi|Cloud|WhatsApp|payment|angel|laptop|MVP|PT |outlet|SKU|UMKM|contoh|Server|Supabase', re.I)
for ws in wb:
    for r in ws.iter_rows():
        for c in r:
            v = c.value
            if isinstance(v, str) and pat.search(v) and ws.title != 'Asumsi':
                print(ws.title, c.coordinate, v[:220])
print(wb['Asumsi']['A2'].value)
