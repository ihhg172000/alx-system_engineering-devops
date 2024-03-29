# nginx web server config
exec { 'update' :
  command  => 'apt-get -y update',
  provider => 'shell',
}

package { 'nginx' :
  ensure => installed,
}

file { '/var/www/html/hello_world.html' :
  content => 'Hello World!',
}

file { '/var/www/html/404.html' :
  content => 'Ceci n\'est pas une page',
}

$conf = "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index hello_world.html;

	rewrite ^/redirect_me http://youtube.com/ permanent;

	error_page 404 /404.html;

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
