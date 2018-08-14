def test_ntp_conf(File):
    ntp_conf= File("/etc/ntp.conf")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o644
    assert ntp_conf.contains("server 192.168.160.158")

def test_NTP_ntpstat(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_ntpd_service_exists(host):
    service = host.service("ntpd")
    assert service.is_enabled

def test_chronyd_service_exists(host):
    service = host.service("chronyd")
    assert service.is_enabled

def test_CCURhttpSession_service_exists(host):
    service = host.service("CCURhttpSession")
    assert service.is_enabled
    assert service.is_running

def test_CCURlighttpd_service_exists(host):
    service = host.service("CCURlighttpd")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhcm_service_exists(host):
    service = host.service("CCURmhcm")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhfrm_service_exists(host):
    service = host.service("CCURmhfrm")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhgs_service_exists(host):
    service = host.service("CCURmhgs")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhrtc_service_exists(host):
    service = host.service("CCURmhrtc")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhsp_service_exists(host):
    service = host.service("CCURmhsp")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhstore_service_exists(host):
    service = host.service("CCURmhstore")
    assert service.is_enabled
    #assert service.is_running

def test_CCURmhue_service_exists(host, Process):
    service = host.service("CCURmhue")
    assert service.is_enabled
    assert service.is_running
    mhuemon = Process.get(comm="mhuemon")
    assert mhuemon.user == "root"
    assert mhuemon.group == "root"

def test_CCURmhvp_service_exists(host):
    service = host.service("CCURmhvp")
    assert service.is_enabled
    assert service.is_running

def test_CCURredis_service_exists(host, Process, Socket, Command):
    service = host.service("CCURredis")
    assert service.is_enabled
    assert service.is_running
    redis = Process.get(ppid='1', comm="redis-server")
    assert redis.user == "root"
    assert redis.group == "root"
    assert Socket("tcp://0.0.0.0:6379").is_listening
    command = Command('/opt/MediaHawk/sbin/redis-cli ping')
    assert command.stdout.rstrip() == 'PONG'
    assert command.rc == 0

def test_CCURtimemon_service_exists(host, Process, Socket):
    service = host.service("CCURtimemon")
    assert service.is_enabled
    assert service.is_running
    timemon = Process.get(ppid='1', comm="timemon")
    assert timemon.user == "root"
    assert timemon.group == "root"
    assert Socket("tcp://0.0.0.0:8099").is_listening

def test_httpsmd_running(Process, Service, Socket, Command):
    httpsmd = Process.get(comm="httpsmd")
    assert httpsmd.user == "root"
    assert httpsmd.group == "root"
    assert Socket("tcp://0.0.0.0:8078").is_listening
    redis = Process.get(ppid='1', comm="redis-server")
    assert redis.user == "root"
    assert redis.group == "root"
    assert Socket("tcp://0.0.0.0:6379").is_listening
    command = Command('/opt/MediaHawk/sbin/redis-cli ping')

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
    




# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"autofs",
"autovt@",
"CCURhttpSession",
"CCURlighttpd",
"CCURmhcm",
"CCURmhfrm",
"CCURmhgs",
"CCURmhrtc",
"CCURmhsp",
"CCURmhstore",
"CCURmhue",
"CCURmhvp",
"CCURredis",
"CCURtimemon",
"chronyd",
"crond",
"dmraid-activation",
"getty@",
"kdump",
"lm_sensors",
"lvm2-monitor",
"mcelog",
"microcode",
"multipathd",
"ntpd",
"postfix",
"rsyslog",
"smartd",
"snmpd",
"sshd",
"sysstat",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"tuned"
    ):  
        service= host.service(spec)
        assert service.is_enabled

