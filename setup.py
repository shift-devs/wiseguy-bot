import setuptools
import wiseguy_bot as module

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=module.APP_NAME,
    version=module.APP_VERSION,
    author=module.APP_AUTHOR,
    license=module.APP_LICENSE,
    description=module.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=module.APP_URL,
    project_urls={
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
		"argparse==1.4.0",
		"twitchAPI==4.2.0"
    ],
    extras_require={
        "dev": [
        ]
    },
    python_requires='>=3.9.0',
    entry_points={
        "console_scripts": [
            f'{module.APP_NAME} = {module.APP_NAME.lower().replace("-", "_").replace(" ", "_")}.__main__:main'
        ]
    }
)
