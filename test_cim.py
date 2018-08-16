def test_ntp_conf(File):
    ntp_conf= File("/etc/ntp.conf")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o644
    assert ntp_conf.contains("server 192.168.160.158")

def test_NTP_time_accuracy(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_ntpd_service_exists(host):
    service = host.service("ntpd")
    assert service.is_enabled

def test_chronyd_service_exists(host):
    service = host.service("chronyd")
    assert service.is_enabled

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
"chronyd",
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

