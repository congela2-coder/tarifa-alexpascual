import json,base64,sys,datetime
from PIL import Image
fecha=sys.argv[1] if len(sys.argv)>1 else datetime.date.today().strftime('%d/%m/%Y')
data=json.load(open('data.json'))
logo='data:image/png;base64,'+base64.b64encode(open('logo.png','rb').read()).decode()
h=open('template.html').read()
h=h.replace('__DATA__',json.dumps(data,ensure_ascii=False)).replace('__LOGO__',logo).replace('__FECHA__',fecha).replace('__VER__',fecha.replace('/',''))
open('index.html','w').write(h)
# imagen de vista previa para WhatsApp (1200x630)
im=Image.new('RGB',(1200,630),(255,45,45)); lg=Image.open('logo.png').convert('RGBA')
s=min(1000/lg.width,560/lg.height); lg=lg.resize((int(lg.width*s),int(lg.height*s)),Image.LANCZOS)
im.paste(lg,((1200-lg.width)//2,(630-lg.height)//2),lg); im.save('preview.png',optimize=True)
print('ok',len(data),'artículos',fecha)
