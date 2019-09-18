from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.yanting.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class YantingCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_yanting(self, args, arguments):
        """
        ::

          Usage:
                yanting --file=FILE
                yanting --text=TEXT
                yanting list

          This command does some useful things.

          Arguments:
              FILE   a file name
              TEXT   string

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None
        arguments.TEXT = arguments['--text'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.TEXT:
            print("text option: ", arguments.TEXT)

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        return ""
