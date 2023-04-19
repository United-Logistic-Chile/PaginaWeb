#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

if username == 'your_username' and password == 'your_password':
	print('Content-Type: text/html')
	print('')
	print('<html>')
	print('<head>')
	print('<title>Welcome</title>')
	print('</head>')
	print('<body>')
	print('<h1>Welcome, {}!</h1>'.format(username))
	print('</body>')
	print('</html>')
else:
	print('Content-Type: text/html')
	print('')
	print('<html>')
	print('<head>')
	print('<title>Error</title>')
	print('</head>')
	print('<body>')
	print('<h1>Invalid username or password</h1>')
	print('</body>')
	print('</html>')
