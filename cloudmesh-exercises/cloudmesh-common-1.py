# fa19-516-170 E.Cloudmesh.Common.1

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.debug import Variables


class Example(object):
    def demo(self, name, username):
        banner("exercise1")
        HEADING()

        variables = Variables()

        variables['debug'] = True
        variables['trace'] = True
        variables['verbose'] = 10  # set as 10 to let verbose output something

        student = {name: username}
        VERBOSE(student)


if __name__ == "__main__":
    Example().demo("Yanting Wan", "yanwan")
