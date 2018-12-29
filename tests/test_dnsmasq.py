#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyarchops_dnsmasq` package."""

import textwrap
from suitable import Api
from pyarchops import helpers
from pyarchops_dnsmasq import dnsmasq


def test_dnsmasq_using_docker():
    """Test the dnsmasq."""

    dnsmasq_conf = textwrap.dedent('''
        no-poll
        no-resolv
        cache-size=1500
        no-negcache
        server=/core-vpn/172.16.254.1
        server=/core-vpn/172.16.254.2
        server=/core-vpn/172.16.254.3
        server=/kubernetes/172.16.254.11
        server=/kubernetes/172.16.254.12
        server=/kubernetes/172.16.254.13
        server=/mesos/172.16.254.11
        server=/mesos/172.16.254.12
        server=/mesos/172.16.254.13
        server=/service/172.16.254.1
        server=8.8.4.4
        server=8.8.8.8
    ''')

    config = {
        'dnsmasq_conf': dnsmasq_conf,
    }

    with helpers.ephemeral_docker_container(
            image='registry.gitlab.com/pyarchops/pyarchops-base'
    ) as container:
        connection_string = "{}:{}".format(
            container['ip'], container['port']
        )
        print('connection strings is ' + connection_string)
        api = Api(connection_string,
                  connection='smart',
                  remote_user=container['user'],
                  private_key_file=container['pkey'],
                  become=True,
                  become_user='root',
                  sudo=True,
                  ssh_extra_args='-o StrictHostKeyChecking=no')

        try:
            dnsmasq.apply(api, config=config)
        except Exception as error:
            raise error
        try:
            result = api.shell(
                'systemctl is-active dnsmasq')['contacted'][connection_string]
        except Exception as error:
            raise error

        assert result['stdout'] == 'active'
