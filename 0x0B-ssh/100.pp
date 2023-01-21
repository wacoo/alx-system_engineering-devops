#create puppet file
include stdlib

file {'/root/home/.ssh/ssh_config':
  ensure=>'present',
  content=>'Host *',
}
file_line{'force_pk_use':
  ensure=>'present',
  path=>'/root/home/.ssh/ssh_config',
  line=>'IdentityFile ~/.ssh/school',
}
file_line{'disable_pass_auth':
  ensure=>'present',
  path=>'/root/home/.ssh/ssh_config',
  line=>'PasswordAuthentication no',
}
