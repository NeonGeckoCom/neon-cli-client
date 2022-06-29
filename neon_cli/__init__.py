# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
#
# Copyright 2008-2021 Neongecko.com Inc. | All Rights Reserved
#
# Notice of License - Duplicating this Notice of License near the start of any file containing
# a derivative of this software is a condition of license for this software.
# Friendly Licensing:
# No charge, open source royalty free use of the Neon AI software source and object is offered for
# educational users, noncommercial enthusiasts, Public Benefit Corporations (and LLCs) and
# Social Purpose Corporations (and LLCs). Developers can contact developers@neon.ai
# For commercial licensing, distribution of derivative works or redistribution please contact licenses@neon.ai
# Distributed on an "AS IS” basis without warranties or conditions of any kind, either express or implied.
# Trademarks of Neongecko: Neon AI(TM), Neon Assist (TM), Neon Communicator(TM), Klat(TM)
# Authors: Guy Daniels, Daniel McKnight, Regina Bloomstine, Elon Gasper, Richard Leeds
#
# Specialized conversational reconveyance options from Conversation Processing Intelligence Corp.
# US Patents 2008-2021: US7424516, US20140161250, US20140177813, US8638908, US8068604, US8553852, US10530923, US10530924
# China Patent: CN102017585  -  Europe Patent: EU2156652  -  Patents Pending

import signal
import curses
import os.path
import sys

from neon_cli.text_client import start_log_monitor, start_mic_monitor, \
    connect_to_mycroft, simple_cli, load_settings, ctrl_c_handler, gui_main, \
    save_settings


def start_cli_client(host: str, port: int, lang: str,
                     ipc_dir: str, logs_dir: str, simple: bool):
    # Monitor system logs
    start_log_monitor(os.path.join(logs_dir, 'skills.log'))
    start_log_monitor(os.path.join(logs_dir, 'voice.log'))
    start_log_monitor(os.path.join(logs_dir, 'audio.log'))
    start_log_monitor(os.path.join(logs_dir, 'extras.log'))
    # Monitor IPC file containing microphone level info
    start_mic_monitor(os.path.join(ipc_dir, "mic_level"))

    connect_to_mycroft(host, port)
    if simple:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        simple_cli(lang)
    else:
        # Special signal handler allows a clean shutdown of the GUI
        signal.signal(signal.SIGINT, ctrl_c_handler)
        load_settings()
        curses.wrapper(gui_main, lang=lang)
        curses.endwin()
        save_settings()
