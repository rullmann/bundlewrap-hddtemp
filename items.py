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
