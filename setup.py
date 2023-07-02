from setuptools import find_packages, setup

setup(
    name="bakorder",
    version="0.0.1",
    description="Author: J.Iszatt\nPython script to reorder bacterial genomes from bakta output",
    url="https://github.com/JoshuaIszatt",
    author="Joshua Iszatt",
    author_email="joshiszatt@gmail.com",
    python_requires=">3",
    packages=find_packages(),
    install_requires=["biopython==1.81", "pandas==1.5.3"],
    entry_points={
        'console_scripts': [
            'bakorder.py = Bakorder.main:main',
        ],
    },
    include_package_data=True,
)
