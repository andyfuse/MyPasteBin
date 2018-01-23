import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)
path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
						'pastebin'))

os.environ['DJANGO_SETTINGS_MODULE']='pastebin.settings'

from app.models import Post

import datetime


Post.objects.filter(time_to_live__lt=datetime.datetime.now()).delete()