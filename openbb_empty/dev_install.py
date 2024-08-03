"""Empty OpenBB Platform Setup Script."""

# flake8: noqa

import os


def main(charting):
    """Run the setup script."""
    # pylint: disable=import-outside-toplevel
    import glob
    import subprocess

    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-U", "pip", "setuptools", "poetry"])

    subprocess.check_call(
        [os.sys.executable, "-m", "poetry", "install", "-E", "charting"]
        if charting
        else [os.sys.executable, "-m", "poetry", "install"]
    )

    base_dir = "extensions"
    directories = [
        os.path.join(base_dir, d)
        for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d)) and glob.glob(os.path.join(base_dir, d, "*.toml"))
    ]

    for directory in directories:
        subprocess.check_call([os.sys.executable, "-m", "poetry", "install", "-C", directory])

    subprocess.check_call([os.sys.executable, "-c", "import openbb;openbb.build(verbose=False)"])

    print(
        "\n\nOpenBB Platform Setup Complete. The Fast API can now be launched by entering: openbb-api\n\n"
        + "Note: The first function call may take longer than all subsequent calls.\n"
    )


if __name__ == "__main__":
    if len(os.sys.argv) > 1:
        charting = os.sys.argv[1] == "charting"
    main(charting)
