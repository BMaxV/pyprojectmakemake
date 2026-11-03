

## what does this do?

```
pyprojectmakemake
make install
```

Solves my installation needs. Maybe it solves yours too.

I was previously using a python script to do the same thing, but all the requirements, the up to date checking and condition stuff is already inside of make. 

And I *like* the simplicity of having a common interface for building or installing software. By ideal workflow for installing a project would be `git clone + make install`. Two lines, no BS, if anything needs doing, I expect whoever distributes the software to write functions to make sure everything is covered by `make install`. My command crawls your project, lists all .py filenames as requirements for the build step.

`pyprojectmakemake` is a command line command and produces this kind of makefile:

```
clean:
	rm -rf ./dist

build: {wheelname}

{wheelname}: {filecollection}
	python3 -m build --no-isolation -C--quiet=

install: build
	pip3 install {wheelname} --force
```


