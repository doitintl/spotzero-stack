import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="SpotZero",
    version="0.1.0",

    description="SpotZero scheduled Fargate task",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Alexei Ledenev",

    package_dir={"": "spotzero"},
    packages=setuptools.find_packages(where="spotzero"),

    install_requires=[
        "aws-cdk.core==1.83.0",
        "aws-cdk.aws_ecs==1.83.0",
        "aws-cdk.aws_ecs_patterns==1.83.0",
        "aws-cdk.aws_applicationautoscaling==1.83.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
