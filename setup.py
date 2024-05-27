from setuptools import setup, find_packages


VERSION = '0.1.5'
DESCRITPION = 'An "easier" version of the pystray package used to create app in the system tray'
LONG_DESCRIPTION = 'A package for adding a system tray app, based on pystray, this package is an "easier" version of pystray to manipulate'

# Setting up
setup(
    name="tray_manager",
    version=VERSION,
    author="Adastram (Github : Adastram1)",
    author_email="",
    url="https://github.com/Adastram1/tray_manager",
    description=DESCRITPION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    requires=['pystray', 'typing', 'types', 'threading', 'pillow', 'enum'],
    keywords=['python', 'manager', 'system tray', 'pystray'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)