# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 Lazar Florentin
#
# This plug-in allows you to search for a given term on wikipedia and
# receive the search result link in weechat. Inspired
#
# History:
# 2012-04-19, Lazar Florentin
#   version 0.1: first release

SCRIPT_NAME    = "wikiLink"
SCRIPT_AUTHOR  = "Lazar Florentin <florentin[dot]lazar[at]gmail[dot]com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "Search for a given term on http://www.wikipedia.org and retrieve the search result link"

try:
    import weechat
except:
    print("This script must be run under WeeChat.")
    print("Get WeeChat now at: http://www.weechat.org/")
    quit()

# Search url en.wikipedia.org/wiki/Special:Search?search=
weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION,
                 SCRIPT_LICENSE, SCRIPT_DESC,"", "")

def build_url_cmd(data, buffer, argv_eol):
    cmd_arguments = ''
    if(not '' == argv_eol):#check for command term
        cmd_arguments = argv_eol
        cmd_arguments = cmd_arguments.replace(" ", "_")
        weechat.command(weechat.current_buffer(), 'http://en.wikipedia.org/wiki/'+cmd_arguments)
    else:
        weechat.prnt("", "No term given, please see /help wikilink")
    return weechat.WEECHAT_RC_OK


# Hook commands to setup stickynote command
hook = weechat.hook_command(SCRIPT_NAME, SCRIPT_DESC,
    "[input]",
    "[input] the term for witch you want a link build",
    "",
    "build_url_cmd",
    "")
