<?php
try
{
	$bdd = new PDO('mysql:host=localhost;dbname=InjectionSQL', 'root', 'root');
}
catch(Exception $e)
{
        die('Erreur : '.$e->getMessage());
}
?>

<html>
	<head>
		<title>Hack Me !</title>
		<LINK href="style.css" rel="stylesheet" type="text/css">
	</head>
	<body>
		<div id="header">
			<pre><?include("Hack_Me.txt");?></pre>
			<small>if you can...</small>
			<p>
				<?php
					$reponse = $bdd->query('SELECT * FROM Compte WHERE NOM="'.$_POST['login'].'" AND PASSWORD="'.$_POST['password'].'"');

					if ($donnees = $reponse->fetch()){
						echo("OK !<br/>");
						echo($donnees["PASSWORD"]);
					}else{
						echo("echec de l'authentification !");
						echo($donnees["PASSWORD"]);
					}
					echo("<br/>Test");
					$reponse->closeCursor();
				?>
			</p>
		</div>	
	</body>
</html>