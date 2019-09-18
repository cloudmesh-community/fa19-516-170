# fa19-516-170 E.Cloudmesh.Common.5

from cloudmesh.common.StopWatch import StopWatch
import time

# My example
print("what's the time of computing fibonacci number using recursion")


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


StopWatch.start("fib time test")
print("35th fibonacci number is: ", fib(35))
StopWatch.stop("fib time test")
print("it takes {0} seconds to compute 35th fibonacci number".format(str(StopWatch.get("fib time test"))))
