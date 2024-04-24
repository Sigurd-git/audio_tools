from setuptools import setup


requirements = [
    "scipy>=1.7.0",
    "numpy",
    "soundsig",
]
setup(
    name="audio_tools",
    version="1.0",
    packages=["audio_tools"],
    include_package_data=True,
    install_requires=requirements,
)
