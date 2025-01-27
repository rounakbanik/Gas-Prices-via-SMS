from setuptools import setup, find_packages

setup(
    name='gas_prices_sms',
    version='1.0',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=['Flask','twilio','websocket-client','rd', 'pickle-mixin'],
    entry_points={
        'console_scripts': [
            'runwebhook = app:run',
        ],
    }
)
