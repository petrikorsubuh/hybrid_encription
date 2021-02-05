from django.test import TestCase
import os
import shutil
import subprocess
from pathlib import Path
from os import path
import subprocess
# Create your tests here.
subprocess.run(['pyhton','ntru.py', '-v', 'gen' ,'167','3','128', 'test_priv', 'test_pub'])
