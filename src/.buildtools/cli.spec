# -*- mode: python -*-

block_cipher = None


a = Analysis(['../cli/docker_hosts.py'],
             pathex=['.'],
             binaries=None,
             datas=None,
             hiddenimports=[
                "cement.ext.ext_alarm",
                "cement.ext.ext_argcomplete",
                "cement.ext.ext_argparse",
                "cement.ext.ext_colorlog",
                "cement.ext.ext_configobj",
                "cement.ext.ext_configparser",
                "cement.ext.ext_daemon",
                "cement.ext.ext_dummy",
                "cement.ext.ext_genshi",
                "cement.ext.ext_handlebars",
                "cement.ext.ext_jinja2",
                "cement.ext.ext_json",
                "cement.ext.ext_json_configobj",
                "cement.ext.ext_logging",
                "cement.ext.ext_memcached",
                "cement.ext.ext_mustache",
                "cement.ext.ext_plugin",
                "cement.ext.ext_redis",
                "cement.ext.ext_reload_config",
                "cement.ext.ext_smtp",
                "cement.ext.ext_tabulate",
                "cement.ext.ext_watchdog",
                "cement.ext.ext_yaml",
                "cement.ext.ext_yaml_configobj"
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pycrypto', 'PyInstaller'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='docker-local-hosts',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )
