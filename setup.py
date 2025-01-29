from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='skin_lens',
      version="0.0.4",
      description="Skin Lens model (api_pred)",
      license="MIT",
      author="Batch 1911-Le Wagon DS-Bootcamp",
      author_email="vlacortegalina@gmail.com",
      #url="https://github.com/ViniciusGalina1995/skin_lens/",
      install_requires=requirements,
      packages=find_packages()
      )
