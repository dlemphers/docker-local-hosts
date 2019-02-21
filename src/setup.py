import setuptools
import setuptools.command.install

setuptools.setup(
    name='Code Pilot Docker Local Hosts',
    version='1.0.0',
    author='Code Pilot Corp.',
    entry_points={
        'console_scripts': [
            'docker-local-hosts = cli.docker_hosts:main',
        ]
    },
    packages=setuptools.find_packages(),
)
