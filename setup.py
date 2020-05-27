import setuptools

setuptools.setup(
    name="euler",
    version="1.0.0",
    author="Ali Şentaş",
    author_email="alisentas96@gmail.com",
    description="My solutions to the project euler problems",
    license='Unlicense',
    packages=['euler', 'euler.utils'],
    install_requires=['numpy', 'jupyterlab', 'matplotlib']
)