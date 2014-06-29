<html>
	<head>
		<title>Hack Me !</title>
		<LINK href="style.css" rel="stylesheet" type="text/css">
	</head>
	<body>
		<div id="header">
			<pre><?include("Hack_Me.txt");?></pre>
			<small>if you can...</small>
			<p>Connectez-vous comme administrateur pour connaitre le secret...</p>
		</div>	
		<form id="form" method="POST" action="login.php">
			<table>
				<tr>
					<td class="blanc">Login : </td><td><input type="text" name="login" /></td>
				</tr>
				<tr>
					<td class="blanc">Mot de passe : </td><td><input type="password" name="password" /></td>
				</tr>
				<tr>
					<td><input type="submit" value="Connexion"/></td>
				</tr>
		</form>
	</body>
</html>