import os
import sys
import subprocess


SCRIPTS_DIR = '{{cookiecutter.project_slug}}/scripts'


def list_scripts():
    scripts = [f[:-3] for f in os.listdir(SCRIPTS_DIR) if f.endswith('.py') and f != '__init__.py']
    print("Available scripts:")
    for script in scripts:
        print(f"  - {script}")


def run_script(script_name, args):
    script_path = f"{SCRIPTS_DIR}/{script_name}.py"
    if os.path.isfile(script_path):
        cmd = ["poetry", "run", "python", script_path] + args
        subprocess.run(cmd)
    else:
        print(f"Script '{script_name}' not found.")
        list_scripts()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_scripts()
    else:
        run_script(sys.argv[1], sys.argv[2:])
