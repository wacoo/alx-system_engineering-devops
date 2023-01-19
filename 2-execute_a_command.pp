# create a manifest tha kills a process

exec {'pkill':
  command => 'pkill killmenow',
  provider=> 'shell',      
}
