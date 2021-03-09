from setuptools import setup

setup(
    name='neon_cli_client',
    version='0.0.2',
    packages=['neon_cli'],
    url='https://github.com/NeonJarbas/debug_cli',
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
