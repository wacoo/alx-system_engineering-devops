# Create class
class create_file {
  #create the file school
  file {'/tmp/school':
    ensure => 'present',
    owner  => 'www-data',
    group  => 'www-data',
    mode   => '0744',
  }
}
#call the class
include create_file
