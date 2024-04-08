#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, run, put
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'abdlouakilalaoui'
env.key_filename = 'path/to/your/ssh/private/key'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    
    if not os.path.exists(archive_path):
        return False

    try:
     
        put(archive_path, '/tmp/')

        
        archive_filename = os.path.basename(archive_path).split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_filename))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(archive_filename, archive_filename))
        run('rm /tmp/{}.tgz'.format(archive_filename))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(archive_filename, archive_filename))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_filename))

        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False
