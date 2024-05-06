# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page)
#using curl, it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”
# Your answer file should be a Puppet manifest containing 
#commands to automatically configure an Ubuntu machine to respect above requirements

#Install Nginx
package { 'nginx':
  ensure    => installed
}

#Create the index.html file
file { '/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  mode    => '0744',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "Hello World!\n"
}

#Redirect to 301
exec { 'redirect to 301':
  command => "sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://github.com/Darth-Jade-i/Darth-Jade-i.github.io.git permanent;' /etc/nginx/sites-available/default",
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  provider=> 'shell'
}

#Restart Nginx
exec { 'restart nginx':
  command => '/etc/init.d/nginx restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  provider=> 'shell'
}