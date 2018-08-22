def test_ntp_conf(File):
    ntp_conf= File("/etc/ntp.conf")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o644
    assert ntp_conf.contains("server 10.48.77.8")

def test_NTP_ntpstat(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_ntpd_service_exists(host):
    service = host.service("ntpd")
    assert service.is_running
    assert service.is_enabled

def test_timezone_check(Command):
    command = Command('timedatectl |grep zone')
    assert command.stdout.rstrip() == '       Time zone: Europe/Warsaw (CEST, +0200)'
    assert command.rc == 0

def test_vtsi_service_exists(host):
    service = host.service("vtsi")
    assert service.is_enabled

def test_java_running(Process, Service, Socket, Command):
    wrapper = Process.get(ppid='1', comm="wrapper")
    assert wrapper.user == "seachange"
    assert wrapper.group == "seachange"
    java = Process.get(ppid=wrapper.pid)
    assert java.user == "seachange"
    assert java.group == "seachange"
    assert java.comm == "java"
    assert Socket("tcp://127.0.0.1:32000").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:9010").is_listening
    assert Socket("tcp://0.0.0.0:8021").is_listening

def test_curl_cim(Command):
    command = Command('curl http://cim:8081/CIM/ws/Contents')
    assert command.rc == 0

def test_curl_localhost(Command):
    command = Command('curl http://localhost:8080/h2')
    assert command.rc == 0

def test_localhost_health(Command):
    command = Command('curl localhost:8080/actuator/health')
    assert command.stdout.rstrip() == '{"status":"UP"}'
    assert command.rc == 0

def test_vtsi_log_file(host):
    file = host.file("/seachange/log/vtsi.log")
    assert file.user == "seachange"
    assert file.group == "seachange"
    assert file.mode == 0o664

def test_vtsi_config_file(host):
    file = host.file("/seachange/local/vtsi/config/application-vtsi.properties")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644

# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"autofs",
"autovt@",
"avahi-daemon",
"CCURcim",
"chronyd",
"crond",
"dbus-org.freedesktop.Avahi",
"dmraid-activation",
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
"tuned"
    ):  
        service= host.service(spec)
        assert service.is_enabled
