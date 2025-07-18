import argparse
import os
import shutil

def init(args):
    repo = "https://github.com/sinofarmonov323/aiogram-bot-template.git"
    project_name = repo.replace("https://github.com/", "").replace(".git", "").split("/")[1]

    os.system(f"git clone {repo}")

    os.makedirs(args.path, exist_ok=True)

    source_dir = project_name
    dest_dir = args.path

    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(dest_dir, item)
        shutil.move(src_path, dst_path)

    shutil.rmtree(source_dir)

def main():
    parser = argparse.ArgumentParser(prog="cli-tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize project")
    init_parser.add_argument("path", nargs="?", default=".", help="Path to initialize")
    init_parser.set_defaults(func=init)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
