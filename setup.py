from setuptools import setup, find_packages

with open("README.md", "r") as read_me:
    long_description = read_me.read()

setup(
    name='ovl',
    packages=find_packages(),
    version='2021.1.3',
    license='apache-2.0',
    author='Ori Ben-Moshe',
    author_email='ovl.contact.help@gmail.com',
    description='A modular and versatile Python package for computer vision'
                ' object detection pipelines tailored for robotics applications',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/1937Elysium/Ovl-Python',
    install_requires=['numpy', 'pynetworktables', 'opencv-python'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows'
    ]
)
