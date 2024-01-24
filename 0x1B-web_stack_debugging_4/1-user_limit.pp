# Sets content of limits_conf.pp file

file { '/etc/security/limits.conf':
  ensure  => present,
  content => "holberton hard nofile 50000\nholberton soft nofile 50000",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
