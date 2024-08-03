"""Empty OpenBB Platform Setup Script."""

# flake8: noqa

import os


def main(charting):
    """Run the setup script."""
    # pylint: disable=import-outside-toplevel
    import glob
    import subprocess

    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-U", "pip", "setuptools"])

    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "poetry"])

    subprocess.check_call(
        [os.sys.executable, "-m", "poetry", "install", "-E", "all"]
        if charting
        else [os.sys.executable, "-m", "poetry", "install"]
    )

    subprocess.check_call(
        [
            os.sys.executable,
            "-m",
            "pip",
            "install",
            "openbb-platform-pro-backend",
            "--no-deps",
        ]
    )

    base_dir = "extensions"
    directories = [
        os.path.join(base_dir, d)
        for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d))
        and glob.glob(os.path.join(base_dir, d, "*.toml"))
        and not d.startswith("empty")
    ]

    for directory in directories:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-e", directory])

    subprocess.check_call([os.sys.executable, "-c", "import openbb;openbb.build()"])

    print(
        "\n\nOpenBB Platform Setup Complete. The Fast API can now be launched by entering: openbb-api\n\n"
        + "Note: The first function call may take longer than all subsequent calls.\n"
    )


if __name__ == "__main__":
    charting = os.sys.argv[1] == "charting" if len(os.sys.argv) > 1 else False
    main(charting)
