import base64

s = base64.b64encode(bytes('tao:password:123345', 'utf-8')).decode('utf-8')
print(s)
print(base64.b64decode(s).decode('utf-8'))