# nginx web server config
exec { 'update' :
  command  => 'apt-get -y update',
  provider => 'shell',
}

package { 'nginx' :
  ensure => installed,
}

exec { 'add header' :
  command  => 'sed -i "/listen 80 default_server;/a add_header X-Served-By $hostname;" /etc/nginx/sites-available/default;',
  provider => 'shell',
}


exec { 'nginx restart' :
  command  => 'service nginx restart',
  provider => 'shell',
}
