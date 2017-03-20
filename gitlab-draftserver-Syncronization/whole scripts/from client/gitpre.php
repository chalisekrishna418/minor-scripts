<?php 
	$user= shell_exec('whoami');
	$argument1 = $_GET['argument1'];
	echo "$argument1";
	echo "<p>$user</p>";
	//$current_directory= shell_exec('pwd');
	echo "<p>$current_directory</p>";
	$cmd=shell_exec("python gitprecommit.py $argument1");
	//$cmd=shell_exec("git clone http://krishna:delluser418@git.ebpearls.com/test/test.git");
	echo ("<p>$cmd</p>");
?> 
