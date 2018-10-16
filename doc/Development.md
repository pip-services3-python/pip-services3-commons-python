### Release

Create **~/.pypirc file**

```text
[distutils]
index-servers =
	pypi
	pypitest

[pypi]
repository = https://pypi.python.org/pypi
username = <your login>
password = <your password>

[pypitest]
repository = https://testpypi.python.org/pypi
username = <your login>
password = <your password>
```

Then update version in **setup.py**, then execute:

```bash
python setup.py register -r pypi
```

```bash
python setup.py sdist upload -r pypi
```