import argparse
import shlex
import subprocess
import sys
import uuid
from getpass import getpass


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='Destination application version')
    return parser.parse_args()


def main():
    parser = get_args()
    version = parser.version
    if not version:
        version = uuid.uuid4().hex[:6]

    password = getpass()

    cmd = ('appcfg.py update ./genesis '
           '--application=s~kennethtrytek '
           '--version={version} '
           '--email=jmarkeyburger@gmail.com '
           '--passin '
           '--no_cookies'.format(version=version))

    cmd = shlex.split(cmd)
    stdin = subprocess.PIPE
    p = subprocess.Popen(cmd, stdin=stdin)
    p.stdin.write(password + '\n')
    p.communicate()
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
