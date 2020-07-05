import rsa # RSA signature module from pip
import qrcode # qrcode generator  module from pip
import zxing # qrcode scanning modue from pip
import pickle # save class as file



def main():
	def gen_qrcode(student):
		tmp = ''
		message = ''.join([tmp + k + ':' + str(student[k]) + ' ' for k in student.keys()])

		# generate keys
		pubkey, prikey = rsa.newkeys(1024)
		with open(f"gen/{student['name']}_pubkey.pkl", 'wb') as f:
			pickle.dump(pubkey, f)
		with open(f"gen/{student['name']}_prikey.pkl", 'wb') as f:
			pickle.dump(prikey, f)

		# use private key to sign the message
		sign = rsa.sign(message.encode(), prikey, 'SHA-256')

		# pack message and signature
		lst_sign = []
		for s in sign:
			lst_sign.append(int(s))
		merge = []
		merge = [message, lst_sign]

		# produce qrcode
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4, )
		qr.add_data(merge)
		qr.make(fit=True)
		img = qr.make_image()
		img.save(f"static/ewm_img/{student['name']}.png")

	def bulk_gen(dic):
		for s in dic:
			gen_qrcode(s)

	# test
	shanting_Li = {
		'name': 'Shanting_Li',
		'gpa': 3.6,
		'major': 'architecture',
		'degree': 'bachelor',
		'enroll_num': '0815',
		'email': 'lishanting1014@gmail.com'
	}
	scarlett = {
		'name': 'Scarlett',
		'gpa': 3.3,
		'major': 'architecture',
		'degree': 'bachelor',
		'enroll_num': '0805',
		'email': 'scarlett1014@gmail.com'
	}

	kenny = {
		'name': 'Kenny',
		'gpa': 3.1,
		'major': 'architecture',
		'degree': 'bachelor',
		'enroll_num': '0892',
		'email': 'kenny1014@gmail.com'
	}
	levi = {
		'name': 'Levi',
		'gpa': 4.0,
		'major': 'architecture',
		'degree': 'bachelor',
		'enroll_num': '0870',
		'email': 'levi1014@gmail.com'
	}
	sherry = {
		'name': 'Sherry',
		'gpa': 4.0,
		'major': 'architecture',
		'degree': 'bachelor',
		'enroll_num': '0870',
		'email': 'sherry1014@gmail.com'
	}
	leon = {
		'name': 'Leon',
		'gpa': 3.0,
		'major': 'architecture',
		'degree': 'bachelor',
		'enroll_num': '0000',
		'email': 'leon1014@gmail.com'
	}

	arch_department = [shanting_Li, scarlett, kenny, levi, sherry, leon]

	bulk_gen(arch_department)

main()

