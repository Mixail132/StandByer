"""
Run the linters locally.
"""

import subprocess

from app.dirs import DIR_APP, DIR_LINT


def run_linters() -> None:
    """
    Executes a series of commands to run linters
    with certain parameters.
    """
    commands = (
        [
            "pylint",
            f"--rcfile={DIR_LINT / '.pylintrc'}",
            f"{DIR_APP}",
        ],
        # ["isort", "-c", f"{DIR_APP}"],
        # [
        #     "flake8",
        #     "--config",
        #     f"{DIR_LINT / '.flake8'}",
        #     f"{DIR_APP}",
        # ],
        # [
        #     "black",
        #     "--diff",
        #     "--config",
        #     f"{DIR_LINT / '.black'}",
        #     f"{DIR_APP}",
        # ],
        # [
        #     "mypy",
        #     "--config-file",
        #     f"{DIR_LINT / 'mypy.ini'}",
        #     f"{DIR_APP}",
        # ],
    )
    for command in commands:
        print(
            "\n",
            "🔥 ",
            command[0],
        )
        command_ = " ".join(command)
        subprocess.run(command_, check=False)


if __name__ == "__main__":
    run_linters()
