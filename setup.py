from __future__ import annotations

import setuptools

import versioneer

setuptools.setup(
    name="mapreader",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A computer vision pipeline for the semantic exploration of maps/images at scale",
    author="MapReader team",
    # author_email="",
    license="MIT License",
    keywords=[
        "Computer Vision",
        "Classification",
        "Deep Learning",
        "living with machines",
    ],
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    url="https://github.com/Living-with-machines/MapReader",
    download_url="https://github.com/Living-with-machines/MapReader/archive/refs/heads/main.zip",
    packages=setuptools.find_packages(),
    include_package_data=True,
    platforms="OS Independent",
    python_requires=">=3.9",
    install_requires=[
        "matplotlib>=3.5.0,<4.0.0",
        "numpy>=1.21.5,<2.0.0",
        "pandas>=2.0.0",
        "pyproj>=3.2.0,<4.0.0",
        "azure-storage-blob>=12.9.0,<13.0.0",
        "aiohttp>=3.8.1,<4.0.0",
        "Shapely>=2.0.0,<3.0.0",
        "nest-asyncio>=1.5.1,<2.0.0",
        "scikit-image>=0.18.3",
        "scikit-learn>=1.0.1,<2.0.0",
        "torch>=1.10.0",
        "torchvision>=0.11.1,<0.17.3",
        "jupyter>=1.0.0,<2.0.0",
        "ipykernel>=6.5.1,<7.0.0",
        "ipywidgets>=8.0.0,<9.0.0",
        "ipyannotate==0.1.0-beta.0",
        "Cython>=0.29.24,<0.30.0",
        "PyYAML>=6.0,<7.0",
        "tensorboard>=2.7.0,<3.0.0",
        "parhugin>=0.0.3,<0.0.4",
        "geopy==2.1.0",
        "rasterio>=1.2.10,<2.0.0",
        "simplekml>=1.3.6,<2.0.0",
        "versioneer>=0.28",
        "tqdm<5.0.0",
        "torchinfo<2.0.0",
        "openpyxl>=3.1.2,<4.0.0",
        "geopandas<1.0.0",
        "pyogrio>=0.7.2",
        "cartopy>=0.22.0",
        "joblib>=1.4.0",
    ],
    extras_require={
        "dev": [
            "pytest<9.0.0",
            "pytest-cov>=4.1.0,<6.0.0",
            "timm<1.0.0",
            "transformers<5.0.0",
            "black>=23.7.0,<25.0.0",
            "flake8>=6.0.0,<8.0.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": [
            "mapreader = mapreader:print_version",
        ],
    },
)
