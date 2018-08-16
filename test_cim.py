def test_ntp_conf(File):
    ntp_conf= File("/etc/ntp.conf")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o644
    assert ntp_conf.contains("server 192.168.160.158")

def test_NTP_time_accuracy(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_timezone_check(Command):
    command = Command('timedatectl |grep zone')
    assert command.stdout.rstrip() == '       Time zone: Europe/Warsaw (CEST, +0200)'
    assert command.rc == 0

def test_ntpd_service_exists(host):
    service = host.service("ntpd")
    assert service.is_enabled

#def test_chronyd_service_exists(host):
#    service = host.service("chronyd")
#    assert service.is_enabled

def test_gssproxy_running(host, File, Process, Service, Socket, Command):
    gssproxy = Process.get(ppid='1', comm="gssproxy")
    assert gssproxy.user == "root"
    assert gssproxy.group == "root"
    listening = host.socket.get_listening_sockets()
    file= File("/run/gssproxy.sock")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o666
    file= File("/var/lib/gssproxy/default.sock")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o666
    file= File("/etc/gssproxy/gssproxy.conf")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o600
    assert host.file("/etc/gssproxy/gssproxy.conf").is_file
    assert host.file("/etc/gssproxy/gssproxy.conf").user == 'root'
    assert host.file("/etc/gssproxy/gssproxy.conf").group == 'root'

def test_CCURcim_service_exists(host, Process, Socket, Command):
    service = host.service("CCURcim")
    assert service.is_enabled
    assert service.is_running
    cim = Process.get(comm="cim")
    assert cim.user == "root"
    assert cim.group == "root"
    assert Socket("tcp://0.0.0.0:8081").is_listening
    assert host.file("/etc/opt/MediaHawk/cim.cfg").is_file
    assert host.file("/etc/opt/MediaHawk/cim.cfg").user == 'root'
    assert host.file("/etc/opt/MediaHawk/cim.cfg").group == 'root'
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Log File Directory:  /var/log")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Library Interface:  MHMP")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Library Address: 10.48.77.30")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Library Volume Name Type: DiskSet")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Library Default Volume: MediaHawk")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("SNMP Trap Peername:   127.0.0.1:162")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("SNMP Traps Enabled:   false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Package Poll Frequency:  15")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Package Retries:  10")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Package Retry Delay:  3600")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Package Search Level:  2")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Content Retention Period:  2592000")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Content Purge Frequency:  3600")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Content Index Type:  ContentFilename")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("BMS Interface Enabled: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("BMS Success Required: ALL")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Origin Success Required: ALL")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Rollback On Failure: No")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Web Service Port: 8081")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Eventis Delete Interval:  86400")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Web Service Status Interval:  300")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Content Byte Per Second: 1048576")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Content Average Seconds: 7200")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("eFO Pp Reload Seconds: 60")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("CIM Virtual IP: 10.48.77.29")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Package Data Retention Period:  2592000")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Enable Rule Based Provision: true")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Retain Transformed ADI File: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Skip Content Ingest: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Skip ADI Transform: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Support ABR Within ADI: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Allow Content AssetId Reuse: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Support Byte Rate: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Snmp Resource Polling Enabled: true")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Eventis Content Size Supported: true")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Content Size Collection Limit: 100")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Rolling Buffer Duration Minutes: 10080")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Rolling Buffer File Duration Minutes: 5")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Rename smil File: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("Support Ingested Content Uri: false")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("TvVod Restart Delay Seconds: 60")
    assert host.file("/etc/opt/MediaHawk/cim.cfg").contains("ABR Restart Delay Seconds: 60")
    assert host.file("/var/log/cim.log").is_file
    assert host.file("/var/log/cim.log").user == 'root'
    assert host.file("/var/log/cim.log").group == 'root'
    command = Command('curl -f http://localhost:8081/CIM/ws/Contents')
    assert command.rc == 0

def test_docker_service_exists(host, Process, Socket, Command):
    service = host.service("docker")
    assert service.is_enabled
    assert service.is_running

def test_tomcat_service_exists(host, Process, Socket, Command):
    service = host.service("CCURtomcat")
    assert service.is_enabled
    assert service.is_running
    tomcat = Process.get(comm="java")
    assert tomcat.user == "ccur"
    assert tomcat.group == "ccur"
    assert Socket("tcp://:::8080").is_listening
    assert Socket("tcp://:::8009").is_listening

def test_CCURorigindb_service_exists(host, Process, Socket, Command):
    service = host.service("CCURorigindb")
    assert service.is_enabled
    assert service.is_running
    docker = Process.get(ppid=1, comm="docker-compose")
    assert docker.user == "root"
    assert docker.group == "root"
    dockerchild = Process.get(ppid=docker.pid, comm="docker-compose")
    assert dockerchild.user == "root"
    assert dockerchild.group == "root"
    command = Command('docker ps -f NAME=origin-mariadb|grep mariadb')
    assert command.rc == 0
    assert Socket("tcp://172.0.0.1:3306").is_listening
    
    #assert Socket("tcp://0.0.0.0:8081").is_listening
    assert host.file("/etc/opt/CCURorigin/origindb-compose.yml").is_file
    assert host.file("/etc/opt/CCURorigin/origindb-compose.yml").user == 'root'
    assert host.file("/etc/opt/CCURorigin/origindb-compose.yml").group == 'root'


# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"autofs",
"autovt@",
"avahi-daemon",
"CCURcim",
"CCURorigindb",
"CCURtomcat",
#"chronyd",
"crond",
"dbus-org.freedesktop.Avahi",
"dmraid-activation",
"docker",
"getty@",
"irqbalance",
"kdump",
"lm_sensors",
"lvm2-monitor",
"mcelog",
"microcode",
"multipathd",
"ntpd",
"postfix",
"rpcbind",
"rsyslog",
"smartd",
"sshd",
"sysstat",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"tuned",
    ):  
        service= host.service(spec)
        assert service.is_enabled

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:111",
"tcp://0.0.0.0:8081",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://:::3306",
"tcp://:::111",
"tcp://:::8080",
"tcp://:::22",
"tcp://::1:25",
"tcp://:::8009",
    ):
        socket = host.socket(spec)
        assert socket.is_listening

