from distutils.core import setup
setup(
    name='skytap',
    packages=['skytap'],
    version='1.0.0',
    description='Skytap REST API access modules',
    author='Fulcrum Technologies',
    author_email='mknowles@fulcrum.net',
    install_requires=['requests']
    url='https://github.com/FulcrumIT/skytap',
    download_url='https://github.com/FulcrumIT/skytap/tarball/1.0.0',
    keywords=['skytap', 'cloud', 'client', 'rest', 'api', 'development'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Internet",
        ],
)
