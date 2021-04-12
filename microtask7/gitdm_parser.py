import requests

file = open('developers_affiliations1.txt')
contents = file.read()
file.close()

contents = contents.replace('\n\t', '\t').split('\n')[7:]

for user in contents:
	try:
		user = user.split('\t')
		name = user[0].split(': ')[0]
		email = user[0].replace('.g', '@g').replace('!', '@')\
					   .split(': ')[1].split(', ')
		orgs = user[1:]
	except IndexError:
		continue

	if name and email and orgs:
		url = 'http://localhost:8000/graphql/'
		query = 'mutation{addIdentity(name: "%s" email: "%s" source:"Git" username: "%s"){uuid}}' % (name, email[0], name)
		r = requests.post(url=url, json={'query': query})
		print(r, r.text)