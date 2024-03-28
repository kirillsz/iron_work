import requests, re
from django.core.mail import EmailMultiAlternatives



def ya_translate(str_translate):

	replace = re.compile(r"[^\w]+", re.I)
    
	defice = re.compile(r"-+$", re.I)
    
	r = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',

		headers={
			"Content-Type": "application/json",
			"Authorization": "Api-Key AQVN0CIHN1QdcFaeHgslC3WyPMlYqKgI5mShVehZ",
		},
		
		json={
			"folder_id": "b1g5alsqk3ftmqq4kj28",
			"texts": [str_translate],
			"targetLanguageCode": "en"
		}
		
	)
	
	if r.status_code != 200:
		return True, ''
	
	result = replace.sub('-', r.json()['translations'][0]['text']).lower()
	result = defice.sub('', result)
	
	return False, result
	

def service_send_mail(subj, message, email):

	content = """
		<!DOCTYPE html>
		<html>
			<head>
				<title>Письмо с сайта TRIADA-SERVICE</title>
			</head>
			<body>
				{}
			</body>
		</html>
	""".format(message)
	
	subject		= subj
	from_email	= "TRIADA-SERVICE <triada-service@riseup.net>"
	text_content= 'Произошла какая-то ошибка, посмотри функцию настроки почты.'
	
	msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
	msg.attach_alternative(content, "text/html")
	msg.send()
	
	return True