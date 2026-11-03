import toml
import os
from packaging.utils import canonicalize_name
from wheel._bdist_wheel import safer_name
#import argv

def makemake():
        
    with open("pyproject.toml","r") as f:
        projectinfo = toml.load(f)
    
    # crawl the project
    # list all filenames
    
    ignore = [".git","dist","egg","__pycache__",".md"]
    gitignore = []
    if "gitignore" in os.listdir():
        with open(gitignore,"r") as f:
            gitignore = f.readlines()
    ignore += gitignore
    
    all_files = []
    for root, dirs, files in os.walk("."):
                
        # skip dirs
        skip = False
        for name in ignore:
            if name in root:
                #print(f"{name} name ignore, skipping")
                skip = True
                continue
                
        if skip:
            continue
        
        for name in files:
            
            #skip filenames
            if name in ignore:
                #print(f"{name} name ignore, skipping")
                continue
            
            all_files.append(f"{root}/{name}")
    
    modulename = safer_name(projectinfo["project"]["name"])
    modulename = modulename.lower() # ??? necesssary but why does safer_name not do this? maybe the setuptools name generation process doesn't work that way? hm.
    
    version = projectinfo["project"]["version"]
    
    filecollection = " ".join(all_files)
    
    wheelname = f"./dist/{modulename}-{version}-py3-none-any.whl"
    
    s = f"""clean:
	rm -rf ./dist

build: {wheelname}

{wheelname}: {filecollection}
	python3 -m build --no-isolation -C--quiet=

install: build
	pip3 install {wheelname} --force"""
    
    with open("makefile","w") as f:
        f.write(s)
    
    #if argv[0]=="install":
    #    os.subproces("make install")

if __name__=="__main__":
    makemake()
