pkg_dnf = {
    'hddtemp': {},
}

svc_systemd = {
    'hddtemp': {
        'needs': ['pkg_dnf:hddtemp'],
    },
}

files = {}

if node.has_bundle('collectd'):
    files['/etc/collectd.d/hddtemp.conf'] = {
        'source': 'collectd.conf',
        'mode': '0640',
        'needs': [ 'pkg_dnf:hddtemp', 'svc_systemd:hddtemp'],
        'triggers': ['svc_systemd:collectd:restart'],
    }
