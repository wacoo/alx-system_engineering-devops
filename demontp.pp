#Class Definition

class ntpconfig {
	#Installing ntp
	package {"ntp":
		ensure=> "present",

	}
	# Configureing NTP config file
	file {"/etc/ntp.conf":
		ensure=> "present",
		content=> "server 0.pool.ntp.org\n",
	}
	# Starting NTP services
	service {"ntpd":
		ensure=> "running",
	}
}
# Class Declaration
include ntpconfig
