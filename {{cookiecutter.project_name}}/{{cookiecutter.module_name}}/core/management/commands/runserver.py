import os
import subprocess
import atexit
import signal
from optparse import make_option

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command\
    as StaticfilesRunserverCommand


class Command(StaticfilesRunserverCommand):
    option_list = StaticfilesRunserverCommand.option_list + (
        make_option(
            '--no-grunt',
            default=True,
            action='store_false',
            dest='grunt',
            help='Prevents grunt from running at the same time as runserver'
        ),
    )

    def inner_run(self, *args, **options):
        grunt = options.get('grunt')
        if grunt:
            self.start_grunt()
        return super(Command, self).inner_run(*args, **options)

    def start_grunt(self):
        self.stdout.write('>>> Starting grunt')
        self.grunt_process = subprocess.Popen(
            ['grunt --gruntfile={}/Gruntfile.js --base=.'.format(settings.PROJECT_PATH)],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('>>> Grunt process on pid {0}'.format(self.grunt_process.pid))

        def kill_grunt_process(pid):
            self.stdout.write('>>> Closing grunt process')
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_grunt_process, self.grunt_process.pid)
