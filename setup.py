from distutils.core import setup


setup(
    name='influx-content-client',
    version='0.0.1',
    packages=['influx_content_client'],
    install_requires=[
        'influxdb==0.1.13'
    ]
)
