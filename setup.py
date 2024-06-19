from setuptools import setup, find_packages

setup(
    name='systracker',
    version='0.1.1',
    author='Mrinaal Arora',
    author_email='marora16@asu.edu',
    description='Real-time system statistics monitoring.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VenturaSync/SysTrack',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'appnope==0.1.4',
        'asttokens==2.4.1',
        'click==8.1.7',
        'colorama==0.4.6',
        'comm==0.2.2',
        'debugpy==1.8.1',
        'decorator==5.1.1',
        'exceptiongroup==1.2.1',
        'executing==2.0.1',
        'importlib_metadata==7.1.0',
        'ipykernel==6.29.4',
        'ipython==8.18.1',
        'jedi==0.19.1',
        'jupyter_client==8.6.2',
        'jupyter_core==5.7.2',
        'markdown-it-py==3.0.0',
        'matplotlib-inline==0.1.7',
        'mdurl==0.1.2',
        'nest-asyncio==1.6.0',
        'packaging==24.1',
        'parso==0.8.4',
        'pexpect==4.9.0',
        'platformdirs==4.2.2',
        'prompt_toolkit==3.0.47',
        'psutil==5.9.8',
        'ptyprocess==0.7.0',
        'pure-eval==0.2.2',
        'Pygments==2.18.0',
        'python-dateutil==2.9.0.post0',
        'pyzmq==26.0.3',
        'rich==13.7.1',
        'shellingham==1.5.4',
        'six==1.16.0',
        'stack-data==0.6.3',
        'tabulate==0.9.0',
        'tornado==6.4.1',
        'traitlets==5.14.3',
        'typer==0.12.3',
        'typing_extensions==4.12.2',
        'wcwidth==0.2.13',
        'zipp==3.19.2'
    ],
    entry_points={
        'console_scripts': [
            'systrack=systrack.main:main',
        ],
    },
    include_package_data=True,
)
