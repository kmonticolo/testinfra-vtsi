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

def test_CCURhttpSession_service_exists(host):
    service = host.service("CCURhttpSession")
    assert service.is_enabled
    assert service.is_running

def test_CCURlighttpd_service_exists(host, Process, Socket, Command):
    service = host.service("CCURlighttpd")
    assert service.is_enabled
    assert service.is_running
    lighttpd = Process.filter(comm="lighttpd")
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert host.file("/opt/MediaHawk/lib64/lighttpd").is_directory
    assert host.file("/opt/MediaHawk/lib64/lighttpd").user == 'root'
    assert host.file("/opt/MediaHawk/lib64/lighttpd").group == 'root'
    command = Command('echo "GET /index.html" | nc 0.0.0.0 80 | grep lighttpd')
    assert command.stdout.rstrip() == 'Server: MediaHawk mhue lighttpd'
    assert command.rc == 0

def test_CCURmhcm_service_exists(host, Process, Socket):
    service = host.service("CCURmhcm")
    assert service.is_enabled
    assert service.is_running
    mhcm = Process.get(comm="mhcm")
    assert Socket("tcp://0.0.0.0:8040").is_listening
    assert Socket("tcp://0.0.0.0:8072").is_listening
    assert host.file("/var/log/mhcm.log").is_file
    assert host.file("/var/log/mhcm.log").user == 'root'
    assert host.file("/var/log/mhcm.log").group == 'root'
    assert host.file("/var/log/mhcm.log").mode == 0o644
    assert host.file("/etc/opt/MediaHawk/mhue.conf").is_file
    assert host.file("/etc/opt/MediaHawk/mhue.conf").user == 'root'
    assert host.file("/etc/opt/MediaHawk/mhue.conf").group == 'root'
    assert host.file("/etc/opt/MediaHawk/mhue.conf").mode == 0o644


def test_CCURmhfrm_service_exists(host):
    service = host.service("CCURmhfrm")
    assert service.is_enabled
    assert service.is_running

def test_CCURmhgs_service_exists(host, Process, Socket):
    service = host.service("CCURmhgs")
    assert service.is_enabled
    assert service.is_running
    mhgs = Process.get(comm="mhgs")
    assert mhgs.user == "root"
    assert mhgs.group == "root"
    assert Socket("tcp://0.0.0.0:554").is_listening
    assert Socket("tcp://0.0.0.0:8046").is_listening
    assert Socket("tcp://0.0.0.0:8081").is_listening
    assert Socket("tcp://0.0.0.0:8031").is_listening
    assert Socket("tcp://0.0.0.0:19743").is_listening
    assert Socket("tcp://0.0.0.0:8001").is_listening
    assert Socket("tcp://0.0.0.0:8002").is_listening
    assert Socket("tcp://0.0.0.0:8041").is_listening
    assert Socket("tcp://:::554").is_listening
    assert Socket("tcp://:::8081").is_listening
    assert Socket("tcp://:::8031").is_listening
    assert Socket("tcp://:::8041").is_listening
    assert host.file("/var/log/mhgs.log").is_file
    assert host.file("/var/log/mhgs.log").user == 'root'
    assert host.file("/var/log/mhgs.log").group == 'root'

def test_CCURmhrtc_service_exists(host, Process, Socket):
    service = host.service("CCURmhrtc")
    assert service.is_enabled
    assert service.is_running
    mhrtc = Process.filter(comm="mhrtc")
    assert Socket("tcp://127.0.0.1:8062").is_listening
    assert Socket("tcp://0.0.0.0:8037").is_listening
    assert Socket("tcp://0.0.0.0:8039").is_listening
    assert host.file("/var/log/mhrtc.log").is_file
    assert host.file("/var/log/mhrtc.log").user == 'root'
    assert host.file("/var/log/mhrtc.log").group == 'root'



def test_CCURmhsp_service_exists(host, Process, Socket):
    service = host.service("CCURmhsp")
    assert service.is_enabled
    assert service.is_running
    mhsp = Process.filter(comm="mhsp")
    assert Socket("tcp://0.0.0.0:8011").is_listening
    assert Socket("tcp://0.0.0.0:555").is_listening
    assert Socket("tcp://0.0.0.0:8075").is_listening
    assert Socket("tcp://0.0.0.0:9001").is_listening
    assert Socket("tcp://:::555").is_listening
    assert host.file("/var/log/mhsp.log").is_file
    assert host.file("/var/log/mhsp.log").user == 'root'
    assert host.file("/var/log/mhsp.log").group == 'root'

def test_CCURmhstore_service_exists(host):
    service = host.service("CCURmhstore")
    assert service.is_enabled
    #assert service.is_running

def test_CCURmhue_service_exists(host, Process):
    service = host.service("CCURmhue")
    assert service.is_enabled
    assert service.is_running
    mhuemon = Process.get(ppid='1',comm="mhuemon")
    assert mhuemon.user == "root"
    assert mhuemon.group == "root"
    assert host.file("/etc/opt/MediaHawk/mhue.conf").is_file
    assert host.file("/etc/opt/MediaHawk/mhue.conf").user == 'root'
    assert host.file("/etc/opt/MediaHawk/mhue.conf").group == 'root'
    assert host.file("/var/log/mhuemon.log").is_file
    assert host.file("/var/log/mhuemon.log").user == 'root'
    assert host.file("/var/log/mhuemon.log").group == 'root'

def test_CCURmhvp_service_exists(host, Process, Socket):
    service = host.service("CCURmhvp")
    assert service.is_enabled
    assert service.is_running
    mhvp = Process.get(ppid='1',comm="mhvp")
    assert Socket("tcp://0.0.0.0:8012").is_listening
    assert Socket("tcp://0.0.0.0:8025").is_listening
    assert host.file("/var/log/mhvp.log").is_file
    assert host.file("/var/log/mhvp.log").user == 'root'
    assert host.file("/var/log/mhvp.log").group == 'root'

def test_CCURredis_service_exists(host, Process, Socket, Command):
    service = host.service("CCURredis")
    assert service.is_enabled
    assert service.is_running
    redis = Process.get(ppid='1', comm="redis-server")
    assert redis.user == "root"
    assert redis.group == "root"
    assert Socket("tcp://0.0.0.0:6379").is_listening
    assert host.file("/etc/opt/MediaHawk/redis.conf").is_file
    assert host.file("/etc/opt/MediaHawk/redis.conf").user == 'root'
    assert host.file("/etc/opt/MediaHawk/redis.conf").group == 'root'
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
    assert host.file("/var/log/timemon.log").is_file
    assert host.file("/var/log/timemon.log").user == 'root'
    assert host.file("/var/log/timemon.log").group == 'root'

# http session management daemon
def test_httpsmd_running(host, Process, Service, Socket, Command):
    httpsmd = Process.get(ppid='1',comm="httpsmd")
    assert httpsmd.user == "root"
    assert httpsmd.group == "root"
    assert Socket("tcp://0.0.0.0:8078").is_listening
    httpsmd = Process.get(ppid='1', comm="httpsmd")
    assert httpsmd.user == "root"
    assert httpsmd.group == "root"
    assert Socket("tcp://0.0.0.0:8078").is_listening
    assert host.file("/var/log/httpsm.log").is_file
    assert host.file("/var/log/httpsm.log").user == 'root'
    assert host.file("/var/log/httpsm.log").group == 'root'

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

