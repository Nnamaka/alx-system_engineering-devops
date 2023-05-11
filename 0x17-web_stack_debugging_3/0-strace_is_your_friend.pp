# change typo errors from 'phpp' to 'php'

exec { 'Adjust typos':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path => '/usr/local/bin/:/bin/'
}
