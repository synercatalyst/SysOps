from setuptools import setup, find_packages

setup(
    name='cstation',
    version='0.1.3',
    # packages=find_packages(),
    install_requires=[
        'Click',
        'auto_click_auto',
        'ansible',
    ],
    entry_points={
        'console_scripts': [
            'cstation = cstation:cli',
        ],
    },
)