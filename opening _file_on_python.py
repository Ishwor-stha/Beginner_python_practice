text=open('/home/esor/Desktop/myfile.txt')

print(text.read())
text.seek(0)

print(text.write('this is fourth line'))

text.close()