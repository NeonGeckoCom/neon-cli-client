# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys
import signal
import io
import os.path
import curses
import tempfile
from neon_utils.configuration_utils import NGIConfig
from neon_cli.text_client import start_log_monitor, start_mic_monitor, \
    connect_to_mycroft, simple_cli, load_settings, ctrl_c_handler, gui_main, \
    save_settings

sys.stdout = io.StringIO()
sys.stderr = io.StringIO()


def custom_except_hook(exctype, value, traceback):
    print(sys.stdout.getvalue(), file=sys.__stdout__)
    print(sys.stderr.getvalue(), file=sys.__stderr__)
    sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = custom_except_hook  # noqa


def main():
    import argparse

    logs_dir = NGIConfig("ngi_local_conf").content.get("dirVars", {}).get("logsDir", "/var/log/mycroft")
    parser = argparse.ArgumentParser()
    parser.add_argument("--ipc_dir", dest="ipc_dir", type=str, help="the base",
                        default=os.path.join(tempfile.gettempdir(), "mycroft", "ipc"))
    parser.add_argument("--logs_dir", dest="logs_dir", type=str,
                        help="directory where mycroft logs are stored",
                        default=logs_dir)
    parser.add_argument("--lang", dest="lang", type=str,
                        help="lang code",
                        default="en-us")
    parser.add_argument("--simple", dest="simple", type=bool,
                        help="use simple cli without logs",
                        default=False)
    args = parser.parse_args()

    # Monitor system logs
    start_log_monitor(os.path.join(args.logs_dir, 'skills.log'))
    start_log_monitor(os.path.join(args.logs_dir, 'voice.log'))
    start_log_monitor(os.path.join(args.logs_dir, 'audio.log'))
    start_log_monitor(os.path.join(args.logs_dir, 'extras.log'))
    # Monitor IPC file containing microphone level info
    start_mic_monitor(os.path.join(args.ipc_dir, "mic_level"))

    connect_to_mycroft()
    if args.simple:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        simple_cli(args.lang)
    else:
        # Special signal handler allows a clean shutdown of the GUI
        signal.signal(signal.SIGINT, ctrl_c_handler)
        load_settings()
        curses.wrapper(gui_main, args.lang)
        curses.endwin()
        save_settings()


if __name__ == "__main__":
    main()
