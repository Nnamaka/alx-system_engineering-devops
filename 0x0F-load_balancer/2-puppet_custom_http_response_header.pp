# A puppet script that creates a custom http header

exec { 'command':
	command => 'sudo apt-get -y update;
	sudo apt-get -y install nginx;
	declare place="SSL configuration\n\tadd_header X-Served-By \$HOSTNAME;\n";
	sudo sed -i "s/SSL configuration/$place/g" /etc/nginx/sites-available/default;
	sudo service nginx restart',
	provider => shell,
}
