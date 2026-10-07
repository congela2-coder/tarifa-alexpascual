import re,subprocess,json,sys
txt=subprocess.run(['pdftotext','-layout',sys.argv[1],'-'],capture_output=True,text=True).stdout
rows=[]
for line in txt.splitlines():
    m=re.match(r'^(\S+)\s+(.+?)\s+(\d+,\d{2})\s*€\s+(.+?)\s*$',line)
    if not m or m.group(1)=='Codigo': continue
    c,d,p,f=m.groups()
    rows.append([c,re.sub(r'\s+',' ',d).strip(),float(p.replace(',','.')),f.strip()])
json.dump(rows,open('data.json','w'),ensure_ascii=False)
print(len(rows),'artículos'); print(sorted(set(r[3] for r in rows)))
