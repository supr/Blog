<html>
	<head>
		<title> Login </title>
	</head>
	<body>
		<font color="#ff0000">${message}</font>
		<form method="post" action="${url}">
			<input type="hidden" name="came_from" value="${came_from}"/>
			<input type="text" name="username" value="${login}"/>
			<input type="password" name="password"/>
			<input type="submit" name="form.submitted" value="Login!"/>
		</form>
	</body>
</html>