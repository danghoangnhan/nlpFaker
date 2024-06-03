from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'nlpFaker',
  packages = find_packages(exclude=['examples']),
  version = '1.0.0',
  license='MIT',
  description = 'nlpFaker',
  long_description=long_description,
  long_description_content_type = 'text/markdown',
  author = 'Daniel Du',
  author_email = 'danghoangnhan.1@gmail.com',
  url = 'https://github.com/lucidrains/vit-pytorch',
  keywords = [
    'Natural language processing',
    'Data augmentation',
  ],
  install_requires=[
    'pandas'
  ],
  setup_requires=[
    'pytest-runner',
  ],
  tests_require=[
    'pytest',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)