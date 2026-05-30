from setuptools import find_packages,setup
from typing import List

# cons value
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    # these function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="edupulse-predictive-analytics-ml-EndTo-EndProject",
    version="0.0.1",
    author="alnooristiak",
    author_email="alnooristiak@gmail.com",
    packages=find_packages(),
    # install_requires=['pandas','seaborn','numpy'],
    install_requires=get_requirements('requirements.txt')
)