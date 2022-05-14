from setuptools import setup, find_packages


setup(name='dummy_api',
      version='1.0',
      description="Automation project for Dummy API automation",
      packages=find_packages(),
      author="Igor Kostenich",
      zip_safe=False,
      install_requires=[
          "pytest>=7.1.1",
          "pytest-html>=3.1.1",
          "requests>=2.27.1",
          "requests-oauthlib>=1.3.0",
          "python-dateutil>=2.8.2",
          "jsonpath-ng>=1.5.3",
      ]
    )
