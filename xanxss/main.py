from lib.cmd import OptParser
from lib.requester import Requester
from lib.payload_generation import PayloadGeneration
from lib.settings import (
    PAYLOADS,
    prettify,
    BANNER,
    HEADERS
)
from lib.formatter import (
    info,
    debug,
    warning,
    error
)


def main():
    print(BANNER)
    try:
        opts = OptParser.opts()
        retval = []
        if opts.urlToUse is None:
            error("must provide a URL to test")
            exit(1)
        if opts.extraHeaders is not None:
            info("using extra headers")
            headers = opts.extraHeaders
        else:
            headers = HEADERS
        if opts.amountToFind is not None:
            amount_of_payloads = opts.amountToFind
        else:
            amount_of_payloads = 25
        if opts.verificationAmount is not None:
            verification_amount = opts.verificationAmount
        else:
            verification_amount = 5
        if opts.providedPayloads is not None:
            info("using provided payloads")
            payloads = []
            for payload in opts.providedPayloads:
                payloads.append(payload)
        elif opts.payloadFile is not None:
            info("using payloads from a file")
            payloads = []
            with open(opts.payloadFile) as f:
                for payload in f.readlines():
                    payloads.append(payload.strip())
        else:
            info("using default payloads")
            payloads = PAYLOADS
        if len(payloads) < 5:
            error("must provide at least 5 payloads")
            exit(1)
        info("generating payloads")
        generator = PayloadGeneration(payloads, amount_of_payloads)
        info("running payloads through tampering procedures")
        tampers = generator.create_tampers()
        info("payloads tampered successfully")
        payloads = generator.obfuscate_tampers(tampers)
        info("running payloads")
        for payload in payloads:
            if opts.runVerbose:
                debug("running payload '{}'".format(payload))
            requester = Requester(
                opts.urlToUse, payload, headers=headers,
                proxy=opts.proxyToUse
            )
            soup = requester.make_request()
            retval.append(soup)
        working_payloads = Requester.check_for_script(retval, verification_amount=verification_amount)
        if len(working_payloads) == 0:
            warning("no working payloads found for requested site")
            exit(1)
        else:
            info("working payloads:")
            prettify(working_payloads)
            info("found a total of {} working payloads".format(len(working_payloads)))
    except Exception as e:
        import sys
        import traceback

        error("something bad happened, failed with error: {}, traceback:".format(str(e)))
        print("Traceback (most recent call):\n{}".format("".join(traceback.format_tb(sys.exc_info()[2])).strip()))
    except KeyboardInterrupt:
        error("user quit")