import setuptools

manifest: dict = {
    "name": "FireBased",
    "license": "MIT",
    "author": "Tricorder",
    "version": "0.0.2.post5",
    "email": "tricorder@isaackogan.com"
}

if __name__ == '__main__':
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name=manifest["name"],
        packages=setuptools.find_packages(),
        version=manifest["version"],
        license=manifest["license"],
        description="Firebase token generation",
        include_package_data=True,  # Ensure non-Python files are included
        author=manifest["author"],
        author_email=manifest["email"],
        url="https://github.com/isaackogan/FireBased",
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords=["Firebase", "Reverse Engineering", "python3", "api", "unofficial"],
        install_requires=[
            "httpx",
            "betterproto==2.0.0b7",
            "pydantic>=2.0.0"
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.12",
            "Framework :: Pydantic :: 2"
        ]
    )
