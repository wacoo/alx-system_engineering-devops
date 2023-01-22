
exec {'update':
  commnad => 'apt update',
  provider => 'shell',
}
package {'nginx':
  ensure => installed',
}
exec {'allow http ufw':
  commnad => 'ufw allow Nginx HTTP';
  provider =>shell,
}
file {'/var/www/html/index.html':
  ensure => 'present',
  content => 'Hello World!',
}

