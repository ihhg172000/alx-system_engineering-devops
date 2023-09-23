# Client configuration file
file { '/.ssh/ssh_config'
  ensure  => present,
  contant => 'Host *\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication No'
}
