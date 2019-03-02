from setuptools import setup


setup(
    name = "Andela challenges-cli",
    version= "1.0",
    py_modules=["hello"],
    install_requires=[
        "Click", "requests"
    ],
    entry_points= {
         "console_scripts": [
         Helloworld=Helloworld._main_:main
         ]
    })
    
