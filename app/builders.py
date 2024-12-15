""" Actions for building the output 'exe' file. """

import subprocess
import shutil
from pathlib import Path

from app.dirs import DIR_APP, DIR_IMG, DIR_TEMP, DIR_OUT


def glue_scripts_needed(
    output_script: Path,
    input_scripts: list[Path],
) -> None:
    """Combine all the scripts to a single result one."""
    with open(output_script, "w", encoding="utf-8") as out:

        for script in input_scripts:

            with open(script, "r", encoding="utf-8") as lines:

                for line in lines:

                    if "app." in line:
                        continue

                    if "DIR_IMG / " in line:
                        line = line.replace("DIR_IMG / ", "")

                    out.write(line)

                out.write("\n\n")


def format_result_script(
    output_script: Path,
) -> None:
    """Format the result script using linters."""
    subprocess.run(
        [
            "autopep8",
            "--in-place",
            "--aggressive",
            output_script,
        ],
        check=True,
    )

    subprocess.run(["isort", output_script], check=True)


def copy_files_needed() -> None:
    """Create an output folder and puts the necessary files into it."""

    if DIR_OUT.exists():
        shutil.rmtree(DIR_OUT)

    DIR_OUT.mkdir(exist_ok=True, mode=0o777)

    copied_files = [
        DIR_APP / ".env",
        DIR_IMG / "green.png",
        DIR_IMG / "grey.png",
        DIR_IMG / "red.png",
        DIR_IMG / "note.ico",
    ]
    for file in copied_files:
        subprocess.run(
            [
                "copy",
                file,
                DIR_OUT,
            ],
            check=True,
            shell=True
        )


def build_exe_file(output_script: Path) -> None:
    """Build an exe file from the result script."""
    subprocess.run(
        [
            "pyinstaller",
            "--noconfirm",
            "--onefile",
            "--windowed",
            "--icon",
            DIR_IMG / "note.ico",
            "--name",
            "switcher",
            f"{output_script}",
            "--distpath",
            DIR_OUT,
            "--workpath",
            DIR_TEMP / "build",
            "--specpath",
            DIR_TEMP,
        ],
        check=True,
    )


if __name__ == "__main__":

    files = [
        DIR_APP / "dirs.py",
        DIR_APP / "entities.py",
        DIR_APP / "tooltips.py",
        DIR_APP / "payloads.py",
        DIR_APP / "configs.py",
        DIR_APP / "actions.py",
        DIR_APP / "settings.py",
        DIR_APP / "timings.py",
        DIR_APP / "main.py",
    ]

    output_file = DIR_APP / "commons.py"

    glue_scripts_needed(output_file, files)
    format_result_script(output_file)
    copy_files_needed()
    build_exe_file(output_file)
