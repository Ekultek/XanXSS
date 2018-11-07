import argparse


class StoreDictKeyPairs(argparse.Action):

    """
    custom action to create a dict from a provided string in the format of key=value
    """

    retval = {}

    def __call__(self, parser, namespace, values, option_string=None):
        for kv in values.split(","):
            if ":" in kv:
                splitter = ":"
            else:
                splitter = "="
            if kv.count(splitter) != 1:
                first_equal_index = kv.index(splitter)
                key = kv[:first_equal_index].strip()
                value = kv[first_equal_index + 1:].strip()
                self.retval[key] = value
            else:
                k, v = kv.split(splitter)
                self.retval[k.strip()] = v.strip()
        setattr(namespace, self.dest, self.retval)


class OptParser(argparse.ArgumentParser):

    def __init__(self):
        super(OptParser, self).__init__()

    @staticmethod
    def opts():
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-u", "--url", dest="urlToUse", metavar="http://test.com/test.php?id=",
            help="pass a URL to test for XSS vulnerabilities"
        )
        parser.add_argument(
            "-a", "--amount", type=int, dest="verificationAmount", metavar="VERIFY",
            help="how many verifications steps to be taken"
        )
        parser.add_argument(
            "-f", "--find", type=int, dest="amountToFind", metavar="AMOUNT",
            help="find this amount of working payloads"
        )
        parser.add_argument(
            "-t", "--time", type=int, dest="testTime", metavar="TIME",
            help="amount of time in seconds to spend on testing"
        )
        parser.add_argument(
            "-p", "--payloads", nargs="+", dest="providedPayloads", metavar="SCRIPT,SCRIPT,SCRIPT",
            help="pass a comma separated list of your own payloads"
        )
        parser.add_argument(
            "-F", "--file", dest="payloadFile", metavar="FILE-PATH",
            help="pass a file containing payloads"
        )
        parser.add_argument(
            "-v", "--verbose", action="store_true", dest="runVerbose",
            help="run in verbose mode"
        )
        parser.add_argument(
            "--proxy", dest="proxyToUse", metavar="TYPE://IP:PORT",
            help="pass a proxy in the format type://ip:port"
        )
        parser.add_argument(
            "-H", "--headers", dest="extraHeaders", action=StoreDictKeyPairs, metavar="HEADER=VALUE,HEADER:VALUE",
            help="Add your own custom headers to the request"
        )
        return parser.parse_args()