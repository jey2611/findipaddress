
import re


files_dlloc = 'IPLocalPool.txt'

f = open(files_dlloc, 'r')
raw_text = str(f.readlines())
f.close()

newfile = open ('IPList.txt','w')

ip_address = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'

#remove subnet mask fromk Raw Text
raw_text2 = re.sub( r'(255)\.(?:[\d]{1,3})\.(?:[\d]{1,3})', ' ', raw_text)

print (raw_text2)

foundip = re.findall( ip_address, raw_text2 )

for ip in foundip:
    newfile.writelines(ip)
    newfile.writelines("\n")
