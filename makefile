clean:
	rm -rf ./dist

build: ./dist/py_project_makefile-0.1-py3-none-any.whl

./dist/py_project_makefile-0.1-py3-none-any.whl: ./pyproject.toml ./setup.py ./readme.md ./makefile ./pyprojectmakefile/script.py ./pyprojectmakefile/__init__.py
	python3 -m build --no-isolation -C--quiet=

install: build
	pip3 install ./dist/py_project_makefile-0.1-py3-none-any.whl --force