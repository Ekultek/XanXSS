from lib.cmd import OptParser
from lib.requester import Requester
from lib.payload_generation import PayloadGeneration
from lib.polyglot_generator import generate_polyglot
from lib.settings import (
    PAYLOADS,
    prettify,
    BANNER,
    HEADERS,
    heuristics
)
from lib.formatter import (
    info,
    debug,
    warning,
    error
)


def main():
    print(BANNER)
    placement_marker = False

    try:
        opts = OptParser.opts()
        retval = []
        if opts.urlToUse is None:
            error("must provide a URL to test")
            exit(1)
        else:
            url_validation = heuristics(opts.urlToUse)
            if not url_validation["validated"]:
                error(
                    "the provided URL could not be validated as a URL, check the URL and try again. a valid URL "
                    "looks something like this: 'http://somesite.com/some/path.php?someid=param'"
                )
                exit(1)
            else:
                if url_validation["query"] == "nogo":
                    warning(
                        "heuristic testing has detected that the provided URL lacks a GET parameter "
                        "this may interfere with testing results"
                    )
            try:
                if url_validation["marker"] == "yes":
                    info("marker for attack placement found, prioritizing")
                    placement_marker = True
                if url_validation["multi_marker"]:
                    warning("multiple markers are not supported, only the first one will be used")
            except:
                pass
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
        if opts.testTime is not None:
            test_time = opts.testTime
        else:
            test_time = 10
        info("generating payloads")
        generator = PayloadGeneration(payloads, amount_of_payloads)
        info("running payloads through tampering procedures")
        tampers = generator.create_tampers()
        info("payloads tampered successfully")
        payloads = generator.obfuscate_tampers(tampers)
        if opts.genPolyglot:
            info("generating polyglot script")
            polyglot = generate_polyglot()
            info("script generated: {}".format(polyglot))
        info("running payloads")
        times_ran = 0
        for payload in payloads:
            if opts.genPolyglot and times_ran != 1:
                warning("running polyglot first")
                times_ran += 1
                payload = polyglot
            if opts.runVerbose:
                debug("running payload '{}{}{}'".format(opts.usePrefix, payload, opts.useSuffix))
            requester = Requester(
                opts.urlToUse, payload, headers=headers,
                proxy=opts.proxyToUse, throttle=opts.throttleTime
            )
            soup = requester.make_request(
                marker=placement_marker, prefix=opts.usePrefix, suffix=opts.useSuffix
            )
            retval.append(soup)
        info("running checks")
        working_payloads = Requester.check_for_script(
            retval, verification_amount=verification_amount, test_time=test_time
        )
        if opts.useSuffix != "" or opts.usePrefix != "":
            working_payloads = [opts.usePrefix + p + opts.useSuffix for p in working_payloads]
        if len(working_payloads) == 0:
            warning("no working payloads found for requested site")
            info("checking if scripts are being sanitized")
            requester = Requester(
                opts.urlToUse, None, headers=headers,
                proxy=opts.proxyToUse, throttle=opts.throttleTime
            )
            results = requester.check_for_sanitize()
            if results:
                warning("it seems that the scripts are being sanitized properly")
            elif results is None:
                warning("hit an error in request, possible WAF?")
            else:
                info("it appears that the scripts are not being sanitized, try manually?")
            exit(1)
        else:
            info("working payloads:")
            prettify(working_payloads)
            info("found a total of {} working payloads".format(len(working_payloads)))
    except Exception as e:
        import sys
        import traceback

        error("something bad happened, failed with error: {}, traceback:".format(str(e)))
        print("Traceback (most recent call):\n    {}".format("".join(traceback.format_tb(sys.exc_info()[2])).strip()))
    except KeyboardInterrupt:
        error("user quit")