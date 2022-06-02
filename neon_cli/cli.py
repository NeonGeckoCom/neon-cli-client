# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2021 Neongecko.com Inc.
# BSD-3
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import tempfile
import click

from os.path import join
from click_default_group import DefaultGroup
from neon_utils.configuration_utils import get_neon_cli_config


@click.group("neon-cli", cls=DefaultGroup,  invoke_without_command=True,
             help="Neon CLI Client")
@click.option("--host", "-h", default="0.0.0.0",
              help="Host (IP) Address of the messagebus")
@click.option("--port", "-p", default=8181,
              help="Host (IP) Address of the messagebus")
@click.option("--lang", "-l", default="en-us",
              help="Language of inputs/responses")
@click.option("--ipc-dir",
              default=join(tempfile.gettempdir(), "mycroft", "ipc"),
              help="Path to local IPC directory")
@click.option("--logs-dir", default=get_neon_cli_config()["log_dir"],
              help="Path to local logs directory")
@click.option("--simple", "-s", is_flag=True, default=False,
              help="Use simple CLI without logs")
def neon_cli(host, port, lang, ipc_dir, logs_dir, simple):
    from neon_cli import start_cli_client
    start_cli_client(host, port, lang, ipc_dir, logs_dir, simple)
