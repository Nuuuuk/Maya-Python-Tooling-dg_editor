import os
import shutil

# 配置
PROJECT_NAME = "dg_editor"
VERSION = "0.1.0"
SRC_DIR = "src"
FILES_TO_COPY = ["install.mel", "log.ico"]


def build():
    # 1. output directory: build/dg_editor_0.1.0
    output_dir = os.path.join("build", "{}_{}".format(PROJECT_NAME, VERSION))

    # clean old builds
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # 2. copy source from src -> build/src
    # ignore unnecessaries
    shutil.copytree(SRC_DIR, os.path.join(output_dir, "src"),
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))

    # 3. copy install files
    for f in FILES_TO_COPY:
        if os.path.exists(f):
            shutil.copy(f, output_dir)
            print("Copied: {}".format(f))
        else:
            print("Warning: {} not found!".format(f))

    print("-" * 30)
    print("Build Success: {}".format(output_dir))
    print("Drag 'install.mel' from that folder into Maya to install.")


if __name__ == "__main__":
    build()