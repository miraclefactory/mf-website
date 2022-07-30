<?php
	// The global $_POST variable allows you to access the data sent with the POST method by name
	// To access the data sent with the GET method, you can use $_GET
  	$name = htmlspecialchars($_POST['name']);
  	$email  = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

  	echo  $name, ' ', $email, ' ', $message;
?>