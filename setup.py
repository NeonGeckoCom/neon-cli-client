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

from setuptools import setup

setup(
    name='neon_cli_client',
    version='0.0.4',
    packages=['neon_cli'],
    url='https://github.com/NeonGeckoCom/neon_cli',
    license='apache-2.0',
    author='jarbasAi',
    author_email='',
    description='cli client extracted from mycroft-core',
    install_requires=["mycroft-messagebus-client>=0.8.4"],
    entry_points={
        'console_scripts': [
            'neon_cli_client=neon_cli.__main__:main'
        ]
    }
)
