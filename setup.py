from setuptools import setup, find_packages


setup(
    name="news",
    version="1.0",
    packages=find_packages(),
    include_package_date=True,
    install_requires=["click", "rich", "playsound", "gtts", "gnewsclient"],
    entry_points="""
        [console_scripts]
        news=news.cli:cli
    """,
    author="Zayed Malick",
    author_email="thexurde123@gmail.com",
    license="MIT",
    long_description=open("README.md", "r").read() +
    "\n\n"+open("CHANGELOG.txt", "r").read(),
    keywords="python",
)
