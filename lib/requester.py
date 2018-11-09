import re
import time
import textwrap

import requests

import lib.settings
import lib.formatter


class Requester(object):

    def __init__(self, url, script, headers=None, proxy=None, **kwargs):
        self.url = url
        self.script = script
        self.original_url = url
        self.headers = headers if headers is not None else lib.settings.HEADERS
        self.proxy = {"http": proxy, "https": proxy} if proxy is not None else {}
        self.throttle = kwargs.get("throttle", 0)
        self.timeout = kwargs.get("timeout", 7)

    def load_url(self, prefix, suffix, marker=False):
        if not marker:
            return self.url + prefix + self.script + suffix
        else:
            marker_index = self.url.index("*")
            self.url = self.url[:marker_index] + prefix + self.script + suffix + self.url[marker_index:]
            return self.url.replace("*", "")

    def make_request(self, marker=False, prefix="", suffix=""):
        retval = {}
        try:
            time.sleep(self.throttle)
            self.url = self.load_url(marker=marker, prefix=prefix, suffix=suffix)
            req = requests.get(self.url, timeout=self.timeout, headers=self.headers, proxies=self.proxy)
            content = req.content
            retval[self.script] = content
        except Exception:
            retval[self.script] = None
        return retval

    @staticmethod
    def check_for_script(responses, verification_amount=10, total_amount_to_find=10, test_time=35):
        retval = set()
        parts_in_script = 0
        start_time = time.time()
        while len(retval) != total_amount_to_find:
            if time.time() - start_time > test_time:
                lib.formatter.warning("times up dumping found")
                break
            else:
                if len(retval) == total_amount_to_find:
                    lib.formatter.info("found requested amount of payloads dumping")
                    break
            for item in responses:
                for key, value in item.items():
                    if value is not None:
                        try:
                            key_parts = textwrap.wrap(key, len(key) / 8)
                            for part in key_parts:
                                issue_fixers = {
                                    ")": r"\)", "(": "\(", "[": r"\[", "]": r"\]",
                                    "\\": r"\\", "/*/": r"\/*\/", "((": "\(\(", "+": "\+",
                                    "*": r"\*", "/": r"\/", "%0a": r"(\r\n|\r|\n)"
                                }
                                identifiers = issue_fixers.keys()
                                to_use = ""
                                for c in part:
                                    if c in identifiers:
                                        c = issue_fixers[c]
                                    to_use += c
                                try:
                                    regex = re.compile(to_use, re.I)
                                    if regex.search(value):
                                        parts_in_script += 1
                                    if parts_in_script <= verification_amount:
                                        retval.add(key)
                                except re.error:
                                    pass
                        except ValueError:
                            pass
        return retval

    def check_for_sanitize(self):
        script = '<`"">'
        regex_script = ""
        change_dict = {"<": "&lt;", '"': "&quot;", ">": "&gt;"}
        for c in script:
            if c in change_dict.keys():
                c = change_dict[c]
            regex_script += c
        regex_script = re.compile(regex_script)
        try:
            url = self.original_url + script
            req = requests.get(url, timeout=self.timeout, headers=self.headers, proxies=self.proxy)
            content = req.content
            if regex_script.search(content) is not None:
                return True
            else:
                return False
        except Exception:
            return None

