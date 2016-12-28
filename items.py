pkg_dnf = {
    'hddtemp': {},
}

svc_systemd = {
    'hddtemp': {
        'enabled': True,
        'needs': [
            "pkg_dnf:hddtemp",
        ],
    },
}

files = {}

if node.has_bundle("collectd"):
    files['/etc/collectd.d/hddtemp.conf'] = {
        'source': "collectd.conf",
        'mode': "0640",
        'owner': "root",
        'group': "root",
        'needs': [
            "pkg_dnf:hddtemp",
            "svc_systemd:hddtemp",
        ],
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    }
