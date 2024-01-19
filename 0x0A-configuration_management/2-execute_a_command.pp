# Using a bash command here
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/bin']
}
