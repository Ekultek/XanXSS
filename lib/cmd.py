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
            help="pass a URL to test for XSS vulnerabilities. it is recommended that you use a URL with a query "
                 "parameter"
        )
        parser.add_argument(
            "-a", "--amount", type=int, dest="verificationAmount", metavar="VERIFY",
            help="how many verifications steps to be taken, this will determine how reliable the payload is. the more "
                 "verification steps the more reliable the payload will be (*default=5)"
        )
        parser.add_argument(
            "-f", "--find", type=int, dest="amountToFind", metavar="AMOUNT",
            help="attempt to find this amount of working payloads, specifying this does not guarantee you will find "
                 "this amount of working payloads (*default=25)"
        )
        parser.add_argument(
            "-t", "--time", type=int, dest="testTime", metavar="TIME",
            help="amount of time in seconds to spend on testing, this will be used as a timer for the verification"
                 " (*default=35s)"
        )
        parser.add_argument(
            "-p", "--payloads", nargs="+", dest="providedPayloads", metavar=("SCRIPT,", "SCRIPT,"),
            help="pass a comma separated list of your own payloads, must contain at least 5 payloads"
        )
        parser.add_argument(
            "-F", "--file", dest="payloadFile", metavar="FILE-PATH",
            help="pass a textual file containing payloads one per line, must contain at least 5 payloads"
        )
        parser.add_argument(
            "-v", "--verbose", action="store_true", dest="runVerbose",
            help="run in verbose mode and display more output (*default=False)"
        )
        parser.add_argument(
            "--proxy", dest="proxyToUse", metavar="TYPE://IP:PORT",
            help="pass a proxy in the format type://ip:port"
        )
        parser.add_argument(
            "-H", "--headers", dest="extraHeaders", action=StoreDictKeyPairs, metavar="HEADER=VALUE,HEADER:VALUE",
            help="add your own custom headers to the request (*default=connection,user-agent)"
        )
        parser.add_argument(
            "--throttle", type=int, dest="throttleTime", metavar="TIME (secs)", default=0,
            help="throttle each request with a sleep time (*default=0)"
        )
        parser.add_argument(
            "-P", "--polyglot", action="store_true", dest="genPolyglot",
            help="generate a polyglot script to append to the end of the running scripts, if there is XSS this should "
                 "find it (*default=False)"
        )
        parser.add_argument(
            "--prefix", dest="usePrefix", metavar="PREFIX", default="",
            help="choose a prefix to use for the payloads, this will be used at the start of each payload "
                 "(*default=None)"
        )
        parser.add_argument(
            "--suffix", dest="useSuffix", metavar="SUFFIX", default="",
            help="choose a suffix to append to the end of the payloads (*default=None)"
        )
        return parser.parse_args()