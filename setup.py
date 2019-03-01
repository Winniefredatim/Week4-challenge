from setuptools import setup


setup(
    name = "Favourite news headlines",
    version= "1.0",
    py_modules=["Welcome"],
    install_requires=[
        "Click",
    ],
    entry_points="""
         [console_scripts]
    """

)
    
