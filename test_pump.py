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
    assert mhcm.user == "root"
    assert mhcm.group == "root"
    assert Socket("tcp://0.0.0.0:8040").is_listening
    assert Socket("tcp://0.0.0.0:8072").is_listening
    assert host.file("/var/log/mhcm.log").is_file
    assert host.file("/var/log/mhcm.log").user == 'root'
    assert host.file("/var/log/mhcm.log").group == 'root'
    assert host.file("/var/log/mhcm.log").mode == 0o644
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").is_file
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").user == 'root'
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").group == 'root'
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").mode == 0o644
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[CM Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-ServicePort = 8040")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-SchedulingPriority = 20")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-CacheLineCount = 1000")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-AIOThreadCount = 64")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-RPCThreadCount = 64")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-FileCloseDelay = 30")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-StatsRefreshPeriod = 5")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-CMGSPort = 8072")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-EL2Port = 8076")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CM-EL2ReadTimeOutSeconds = 2")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[CMCM Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CMCM-Register = false")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("CMCM-Port = 8073")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[OBS Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("OBS-CephRegister = false")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[EL1 Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("EL1-Register = false")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("EL1-FileMigrateThreshold = 2")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[C2 Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("C2-TransferRate = 20000000")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("C2-ThreadCount = 20")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[HTTP Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("HTTP-ProxyRedirector =")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("HTTP-MaxActiveRequests = 150")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("HTTP-MaxQueuedRequests = 250")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[FRM Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("FRM-Register = true")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("FRM-Port = 8020")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[LOG Group] ")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("Log-Level = 20")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("Log-FilePath = /var/log/mhcm.log")
    assert host.file("/etc/opt/MediaHawk/mhcm.cfg").contains("[DEBUG Group] ")

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
    mhrtc = Process.get(comm="mhrtc")
    assert mhrtc.user == "root"
    assert mhrtc.group == "root"
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
    mhsp = Process.get(comm="mhsp")
    assert mhsp.user == "root"
    assert mhsp.group == "root"
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
    assert host.file("/var/log/mhuemon.log").is_file
    assert host.file("/var/log/mhuemon.log").user == 'root'
    assert host.file("/var/log/mhuemon.log").group == 'root'
    assert host.file("/etc/opt/MediaHawk/mhue.conf").is_file
    assert host.file("/etc/opt/MediaHawk/mhue.conf").user == 'root'
    assert host.file("/etc/opt/MediaHawk/mhue.conf").group == 'root'
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.document-root        = "/var/lib/MediaHawk/Edge/webroot/"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.errorlog             = "/var/log/mhue_error.log"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.core-files           = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.tag                 = "MediaHawk mhue lighttpd"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.network-backend = "linux-mediahawk-aio"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.use-noatime = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-read-threads = 16')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-stat-threads =  32')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-worker = 8')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-keep-alive-requests = 16')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-keep-alive-idle = 20')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-read-idle = 60')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-write-idle = 60')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.max-fds = 64511')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server_info.status-url     = "/server-status"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server_info.config-url     = "/server-config"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.stat-cache-engine = "fam"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.mediahawk             = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('server.pid-file            = "/var/run/mhue.pid"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('cachemanager.mhstore = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('proxy-core.use-mhstore = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('mhstore_cache.bases = ("/var/lib/MediaHawk/Edge/webroot/cache")')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('mhstore_cache.enable = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('mhstore_cache.backend = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('mhstore_cache.dynamic-mode = "enable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('mhstore_cache.debug = "disable"')
    assert host.file("/etc/opt/MediaHawk/mhue.conf").contains('mhstore_cache.max-memory-size = 2000')

def test_CCURmhvp_service_exists(host, Process, Socket):
    service = host.service("CCURmhvp")
    assert service.is_enabled
    assert service.is_running
    mhvp = Process.get(ppid='1',comm="mhvp")
    assert mhvp.user == "root"
    assert mhvp.group == "root"
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
    command = Command('/opt/MediaHawk/sbin/redis-cli ping')
    assert command.stdout.rstrip() == 'PONG'
    assert command.rc == 0
    assert Socket("tcp://0.0.0.0:6379").is_listening
    assert host.file("/etc/opt/MediaHawk/redis.conf").is_file
    assert host.file("/etc/opt/MediaHawk/redis.conf").user == 'root'
    assert host.file("/etc/opt/MediaHawk/redis.conf").group == 'root'
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('daemonize no')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('pidfile "/var/run/redis.pid"')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('port 6379')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('tcp-backlog 511')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('timeout 0')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('tcp-keepalive 0')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('loglevel notice')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('logfile "/var/log/redis.log"')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('databases 16')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('stop-writes-on-bgsave-error yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('rdbcompression yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('rdbchecksum yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('dbfilename "redis.rdb"')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('dir "/var/lib/MediaHawk/Edge"')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('slave-serve-stale-data yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('slave-read-only yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('repl-diskless-sync no')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('repl-diskless-sync-delay 5')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('repl-disable-tcp-nodelay no')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('slave-priority 100')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('appendonly yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('appendfilename "redis_appendonly.aof"')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('appendfsync no')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('no-appendfsync-on-rewrite no')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('auto-aof-rewrite-percentage 100')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('auto-aof-rewrite-min-size 2gb')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('aof-load-truncated yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('lua-time-limit 5000')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('slowlog-log-slower-than 10000')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('slowlog-max-len 128')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('latency-monitor-threshold 0')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('notify-keyspace-events ""')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('hash-max-ziplist-entries 512')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('hash-max-ziplist-value 64')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('list-max-ziplist-entries 512')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('hash-max-ziplist-value 64')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('list-max-ziplist-entries 512')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('list-max-ziplist-value 64')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('set-max-intset-entries 512')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('zset-max-ziplist-entries 128')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('zset-max-ziplist-value 64')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('hll-sparse-max-bytes 3000')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('activerehashing yes')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('client-output-buffer-limit normal 0 0 0')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('client-output-buffer-limit slave 256mb 64mb 60')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('client-output-buffer-limit pubsub 32mb 8mb 60')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('hz 10')
    assert host.file("/etc/opt/MediaHawk/redis.conf").contains('aof-rewrite-incremental-fsync yes')

def test_resource_cfg(host):
    assert host.file("/etc/opt/MediaHawk/resource.cfg").contains("Define:.*Disk.*1s0.*/r1.*VIRTUAL_1MB.**.*64")

    
def test_CCURtimemon_service_exists(host, Process, Socket):
    service = host.service("CCURtimemon")
    assert service.is_enabled
    assert service.is_running
    timemon = Process.get(ppid='1', comm="timemon")
    assert timemon.user == "root"
    assert timemon.group == "root"
    assert Socket("tcp://0.0.0.0:8099").is_listening

def test_CCURtimemon_service_exists(host, Process, Socket):
    service = host.service("CCURtimemon")
    assert service.is_enabled
    assert service.is_running
    timemon = Process.get(ppid='1', comm="timemon")
    assert timemon.user == "root"
    assert timemon.group == "root"
    assert Socket("tcp://0.0.0.0:8099").is_listening

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
    assert host.file("/var/log/httpsm.log").is_file
    assert host.file("/var/log/httpsm.log").user == 'root'
    assert host.file("/var/log/httpsm.log").group == 'root'
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").is_file
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").user == 'root'
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").group == 'root'
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("SM-ServicePort = 8078")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("SM-SchedulingPriority = 20")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("SM-RPCThreadCount = 256")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("Session-BackOffice = NOS")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("Session-AuthorityURL =")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("Session-MaxLifeTime = 30")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("HTTP-ProxyRedirector =")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("HTTP-MaxActiveRequests = 256")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("HTTP-MaxQueuedRequests = 512")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("FRM-Register = true")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("FRM-Port = 8020")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("Log-Level = 20")
    assert host.file("/etc/opt/MediaHawk/httpsm.cfg").contains("Log-FilePath = /var/log/httpsm.log")

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
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("mechs = krb5")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_store = keytab:/etc/gssproxy/http.keytab")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_store = ccache:/var/lib/gssproxy/clients/krb5cc_%U")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("euid = 48")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("mechs = krb5")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("socket = /run/gssproxy.sock")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_store = keytab:/etc/krb5.keytab")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("trusted = yes")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("kernel_nfsd = yes")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("euid = 0")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_store = keytab:/etc/krb5.keytab")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_store = ccache:FILE:/var/lib/gssproxy/clients/krb5cc_%U")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_store = client_keytab:/var/lib/gssproxy/clients/%U.keytab")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("cred_usage = initiate")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("allow_any_uid = yes")
    assert host.file("/etc/gssproxy/gssproxy.conf").contains("trusted = yes")

def test_mhcmd_dr(Command):
    command = Command('/usr/sbin/mhcmd dr -a |grep -A1 ^"Service Providers"|grep -w enable.*Y$')
    assert command.rc == 0
    command = Command('/usr/sbin/mhcmd dr -a |grep -A1 ^Video\ Pumps|grep -w enable.*Y$')
    assert command.rc == 0
    command = Command('/usr/sbin/mhcmd dr -a |grep -A1 ^Real\ Time\ Catchers|grep -w enable.*Y$')
    assert command.rc == 0

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

