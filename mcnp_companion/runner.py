import os
import subprocess
import notify2 as n
from os.path import expanduser

class runner:
    def __init__(self, filename, command, remote="local", sys='linux',
                 renderer=None, blocking=False):
        if remote in ['solar system', 'Solar System', 'solar_system',
                         'solar sys']:
            pass
        # check in the completed directory, and if there is an out file with
        # exactly the same infile, then, don't run
        self.needs_to_run = True
        # Then, check the current processes to see if there are any instances
        # running on this machine

        # If there are, then we will run it on the solarsystem

        # initialize a notification system
        n.init('MCNP')
        # construct the command
        if blocking:
            cmd = []
        else:
            cmd = ["nohup"]

        cmd.extend([command])
        cmd.extend(['inp=' + filename + '.inp'])
        cmd.extend(['out=' + filename + '.out'])
        cmd.extend(['run=' + filename + '_runtpe'])
        cmd.extend(['mctal=' + filename + '_tallies.out'])
        cmd.extend(['tasks %d' % processors[remote]])
        if not blocking:
            cmd += ' &'
        print cmd
        # construct the notification
        notification = n.Notification(command, 'Will now run %s.' % cmd)
        notification.show()
        # check if there is an output file that has the EXACT same input and
        # has completed
        if renderer is not None:
            pass
            # renderer.run()cd
        # now run the actual mcnp
        if self.needs_to_run:
            p = subprocess.Popen(cmd)#, shell=True)
            if blocking:
                p.communicate()
                print "waiting for the process to finish"
        # now start a daemon to watch the output file
        # checker = mcnpdaemon('/tmp/mcnpchecker.pid').set_notification_daemon(notification).start()
        # notify when it updates
        # notify when it ends
