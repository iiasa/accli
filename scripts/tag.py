import os
import subprocess

with open("accli/_version.py") as vf:
    exec(vf.read())

version = globals()['VERSION']

subprocess.run(
            [
                "git", 
                "tag",
                version
            ],
            check=True
        )


