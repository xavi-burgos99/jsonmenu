from setuptools import setup, find_packages

setup(
    name='jsonmenu',
    version='1.0.0',
    author='Xavi Burgos',
    author_email='xavi@dzin.es',
    description='The easiest way to create interactive console menus in Python using JSON',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xavi-burgos99/jsonmenu',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    keywords='json menu console interactive python',
    license='MIT',
)
