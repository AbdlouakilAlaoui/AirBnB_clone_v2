#!/usr/bin/env bash
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from web_static folder """ 
    if not os.path.exists('version'):
       os.makedirs('versions')
       now = datatime.now()
       timestamp = now.strftime("%Y%m%d%H%M%S")
      
    archive_name ='versions/web_static_{}.tgz'.format(timestamp) 
    command = 'tra -cvzf {} web_static'.format(archive_name)
    result = local(command)
    if result.failed:
         return None
   else:
    return archive_name

