# -*- coding: utf-8 -*-

"""Main module."""

import suitable


def apply(api: suitable.api.Api, config: dict, quiet: bool = False) -> dict:
    """ installs dnsmasq """

    results = dict()

    results['pacman'] = api.pacman(name='dnsmasq', state='present')
    if 'dnsmasq_conf' in config.keys():
        results['dnsmasq_conf'] = api.copy(
            dest='/etc/dnsmasq.conf',
            content=config['dnsmasq_conf']
        )
    if 'resolv_conf' in config.keys():
        results['resolv_conf'] = api.copy(
            dest='/etc/resolv.conf',
            content=config['resolv_conf']
        )
    results['service'] = api.service(
        name='dnsmasq', state='started', enabled=True)
    if not quiet:
        print(results)
    return dict(results)
