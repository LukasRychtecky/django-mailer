from setuptools import setup, find_packages

from mailer import get_version


setup(
    name="django-mailer",
    version=get_version(),
    description="A reusable Django app for queuing the sending of email. Forked from pinax/django-mailer.",
    author="Jiri Zamazal",
    author_email="zamazal.jiri@gmail.com",
    url="http://github.com/zamazaljiri/django-mailer",
    packages=find_packages(),
    include_package_data=True,
    package_dir={"mailer": "mailer"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
    ],
    install_requires = [
        'Django >= 1.6',
        'six >= 1.5.2',
        'South >= 0.8.4',
        ],

)
