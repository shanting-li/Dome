import rsa # RSA signature module from pip
import qrcode # qrcode generator  module from pip
import zxing # qrcode scanning modue from pip
import pickle # save class as file
import smtplib #email module
import sys



#python会扫描并验证本地同文件夹里的二维码，一次只验证一个。您这边就验证一个刚生成的二维码就行了
#html验证Scarlett这一个人就行了。因为网页上本来也是写的她的名字

def veri(stu):
	lst = []
	# scan the qrcode
	reader = zxing.BarCodeReader()
	stu_name = stu['name']
	barcode = reader.decode(f"C:/Users/Administrator/Desktop/Dome/static/img/{stu_name}.png")
	msg_get = barcode.parsed
	n = 0
	count = 0
	while n < len(msg_get):
		if count == 2:
			break
		elif msg_get[n] == '[':
			count += 1
		n += 1
	msg_aca = msg_get[2:n-4] #remove''
	msg_sign = msg_get[n:-2] #remove[]
	try:
		msg_sign = (b''.join([bytes([int(i)]) for i in msg_sign.split(',')]))
	except ValueError:
		lst.append('The QR Code is unreadable')
		return lst

	# verify the message
	# print ('Applying for pulickey')
	lst.append('Applying for pulickey')
	with open(f'C:/Users/Administrator/Desktop/Dome/gen/{stu_name}_pubkey.pkl','rb') as f:
		pubkey = pickle.load(f)
	lst.append('Verifying ...')
	# print ('Verifying ...')
	try:
		veri = rsa.verify(msg_aca.encode(),msg_sign, pubkey)
		lst.append('The Certificate is genuine')
		return lst
	except rsa.pkcs1.VerificationError:
		lst.append('The Certificate is forged')
		return lst




#test
# test 
shanting_Li = {
	'name': 'Shanting_Li',
	'gpa': 3.6,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0815',
	'email':'lishanting1014@gmail.com'
}
scarlett = {
	'name': 'Scarlett',
	'gpa': 3.3,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0805',
	'email':'scarlett1014@gmail.com'
}

kenny = {
	'name': 'Kenny',
	'gpa': 3.1,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0892',
	'email':'kenny1014@gmail.com'
}
levi = {
	'name': 'Levi',
	'gpa': 4.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0870',
	'email':'levi1014@gmail.com'
}
sherry = {
	'name': 'Sherry',
	'gpa': 4.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0870',
	'email':'sherry1014@gmail.com'
}
leon = {
	'name': 'Leon',
	'gpa': 3.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0000',
	'email':'leon1014@gmail.com'
}
adversary = {
	'name': 'Adversary',
	'gpa': 3.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0000',
	'email':'leon1014@gmail.com'
}

#print(veri(adversary))
def maf():
	a = veri(adversary)
	return a[-1:]

#print(maf())
