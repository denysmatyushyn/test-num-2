<?php
$url = $_SERVER['REQUEST_URI'];

$key = '?arg=Denis';

if (strpos($url, $key) == false) {
	phpinfo();
}
else {
	$url_components = parse_url($url);
	parse_str($url_components['query'], $params);
	echo ' Hi '.$params['arg'];
}

?>
