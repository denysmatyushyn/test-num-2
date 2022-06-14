<?php
$url = $_SERVER['REQUEST_URI'];

function writePhpInfo() {
	phpinfo();
}

function writeHelloName($strUrl) {
	echo ' Hi '.$strUrl;
}

if (isset($_GET['arg'])) {
	writeHelloName($_GET['arg']);
} else {
	writePhpInfo();
}