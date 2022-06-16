import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_sql_queries",
    version="v1.0.0",
    author="Aman Prajapati",
    author_email="techieaman94@gmail.com",
    description="Middleware to print out all SQL queries done, their count and execution time for each view that is processed for a request",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/techieaman94/django-db-queries",
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    keywords=["database queries", "sql queries", "django request"],
)