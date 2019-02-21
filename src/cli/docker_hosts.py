import logging
import sys
import termcolor
import jmespath

import cement.core.foundation
import cement.core.controller

import docker as Docker

VERSION = '1.0.0'

BANNER = """
Docker Local Hosts Version: {}
Copyright (c) 2019 Code Pilot Corp.
""".format(
    termcolor.colored(VERSION, 'green')
)

docker = Docker.from_env()


class ProjectController(cement.core.controller.CementBaseController):

    class Meta:
        label = 'base'

        arguments = [
            (
                ['-v', '--version'], dict(action='version', version=BANNER)
            ),
            (
                ['-c', '--container'], dict(action='store',
                                            help='Name of container to map')
            ),
            (
                ['-l', '--local'], dict(action='store',
                                        help='Local (.local) name to use')
            )
        ]

    @cement.core.controller.expose(help='Map internal container IP address to local hostname')
    def map(self):
        if not self.app.pargs.container or not self.app.pargs.local:
            sys.exit("Please provide a container name and local name")

        logging.info(
            'Mapping {} to {}.local'.format(
                self.app.pargs.container,
                self.app.pargs.local
            )
        )

        try:
            container = docker.containers.get(self.app.pargs.container)
        except Docker.errors.NotFound:
            sys.exit('Could not find container {}'.format(
                termcolor.colored(
                    self.app.pargs.container,
                    "yellow"
                )
            ))

        container_ip_address = jmespath.search(
            'NetworkSettings.Networks | values(@)[0] | IPAddress',
            container.attrs
        )

        if not container_ip_address:
            sys.exit('Could not locate IP address for {}'.format(
                self.app.pargs.container
            ))

        hosts = open('/etc/hosts').readlines()
        entry_location = None

        for i, _ in enumerate(hosts):
            if self.app.pargs.local in hosts[i]:
                entry_location = i

        if not entry_location:
            hosts.append('')
            entry_location = len(hosts) - 1

        hosts[entry_location] = '{} {}.local # {}'.format(
            container_ip_address,
            self.app.pargs.local,
            self.app.pargs.container
        )

        open('/etc/hosts', 'w').write('\n'.join(
            hosts + ['\n']
        ))


class DockerLocalHost(cement.core.foundation.CementApp):
    class Meta:
        label = 'dlh'
        base_controller = 'base'
        handlers = [
            ProjectController
        ]


def main():

    with DockerLocalHost() as app:
        # Have to blow away Cement app logger
        logging.root = logging.getLogger('cement:app:dlh')
        logging.root.propagate = False

        app.run()


if __name__ == '__main__':

    main()
