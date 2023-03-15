import setuptools

with open("README.md","r",encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="FH_project",
	version="0.0.1",
	author="Felix",
	author_email="felixhuang1806@gmail.com",
	description="A small example package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="http://github.com/pypa/sampleproject",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)
