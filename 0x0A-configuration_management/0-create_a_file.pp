# create a file in /tmp
file { '/tmp/school' :
  ownar => 'www-data',
  group => 'www-data',
  mode => '0744',
  content => 'I love Puppet'
}
