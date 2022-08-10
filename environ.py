#!/usr/bin/env python3
from os import environ
from time import sleep
import sys
from subprocess import check_call, check_output, CalledProcessError,TimeoutExpired, Popen, PIPE

''' spiegazione  '''
#///descrizione  func 
def write_to_journal(string):
    ''' test 1  '''
    check_output(['systemd-cat'], input=string.encode('utf-8'))

write_to_journal('rclone-script started')

# Save passed arguments
remote_mount = sys.argv[1]
local_mount = sys.argv[2]
sys_args = sys.argv[4].split(',')

# Must add path to environment in order for rclone mount to work
env = environ.copy()
output_raw = check_output(['whereis', 'rclone'],)
path = output_raw.decode('utf-8').split(' ')[1].removesuffix('/rclone')
env['PATH'] = path

# If path extraction does not work enter desired path here
# env['PATH'] = '/usr/bin'

options = []
discarded_options = []

# Load options for rclone mount to consume
for arg in sys_args:
    if not arg.startswith('rc.'):
        discarded_options.append(arg)
        continue
    options.append(f'--{arg[3:]}')

write_to_journal(f'rclone-script options: {options}')
write_to_journal(f'rclone-script discarded options: {discarded_options}')

# Mount folder, if this doesn't work try with full path for rclone
output = Popen(
    ['rclone', 'mount', *options, remote_mount, local_mount ], env=env,
    stdout=PIPE, stderr=PIPE, close_fds=True, shell=False,
)
try:
    output.wait(1)
except TimeoutExpired as e:
    # Must wait for mount to be seen, in order for systemd not to complain
    write_to_journal('rclone-script rclone mount success')
    for tries in range(1, 20):
        try:
            check_call(['mountpoint', local_mount], env=env)
            write_to_journal(f'rclone-script mount found after {tries} tries')
            break
        except CalledProcessError:
            write_to_journal('rclone-script mount not found, sleeping')
            sleep(0.1)
    else:
        write_to_journal('rclone-script mount not found, not looking anymore')
        sys.exit(1)

    sys.exit(0)
else:
    write_to_journal(f'rclone-script mount failed. ErrMsg: {output.stderr.read().decode("utf-8")}')
    sys.exit(1)