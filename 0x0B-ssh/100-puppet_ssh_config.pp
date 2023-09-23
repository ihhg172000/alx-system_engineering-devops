# Client configuration file
file { '/.ssh/ssh_config':
  ensure  => present,
  contant => 'Host * IdentityFile ~/.ssh/school PasswordAuthentication No'
}
