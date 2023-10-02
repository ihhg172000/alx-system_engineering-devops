# nginx web server config
exec { 'update' :
  command  => 'apt-get -y update',
  provider => 'shell',
}

package { 'nginx' :
  ensure => installed,
}

$conf = "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

	add_header X-Served-By \$hostname;

        server_name _;

        location / {
                try_files \$uri \$uri/ =404;
        }
}
"

file { '/etc/nginx/sites-available/default' :
  content => $conf,
}

exec { 'nginx restart' :
  command  => 'service nginx restart',
  provider => 'shell',
}
