```python
# default_template.py

# This is a JSON-like dictionary that defines the default project structure.
# Each key represents a directory or a file.
# If the value is a dictionary, it represents a directory and its contents.
# If the value is a string, it represents a file and its contents.

project_structure = {
    'src': {
        '__init__.py': '',
        'main.py': '',
        'utils': {
            '__init__.py': '',
            'helper.py': ''
        },
        'models': {
            '__init__.py': '',
            'model1.py': '',
            'model2.py': ''
        }
    },
    'tests': {
        '__init__.py': '',
        'test_main.py': '',
        'test_helper.py': '',
        'test_model1.py': '',
        'test_model2.py': ''
    },
    'docs': {
        'index.md': '# Documentation\n\nThis is the main index file for the documentation.',
        'api': {
            'index.md': '# API Documentation\n\nThis is the main index file for the API documentation.'
        }
    },
    'data': {
        'raw': {},
        'processed': {}
    },
    'notebooks': {
        'exploration.ipynb': ''
    },
    'README.md': '# Project Title\n\nThis is a brief description of the project.',
    '.gitignore': '*.pyc\n.DS_Store\n.ipynb_checkpoints',
    'requirements.txt': 'numpy\npandas\nmatplotlib\nscikit-learn',
    'setup.py': 'from setuptools import setup, find_packages\n\nsetup(\n    name="project_name",\n    version="0.1",\n    packages=find_packages(),\n)',
    'LICENSE': 'MIT License\n\nCopyright (c) 2022 Your Name\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.',
    'CONTRIBUTING.md': '# Contributing\n\nPlease read this guide if you\'re interested in contributing to the project.'
}

# Write the project structure to a JSON file
with open('default_template.json', 'w') as f:
    json.dump(project_structure, f, indent=4)
```
