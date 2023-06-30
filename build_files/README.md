# to build

- in the repo, update the `django_messages/build/setup.py` file as needed. This includes:

    - description
    - metadata about version number, license, etc.
    - dependencies
    - required python

- on your build machine, make a folder named `django_messages_build`.
- get source code and place it in the `django_messages_build` folder.  Either:

    - clone this repository into that folder: `git clone https://github.com/jonathanmorgan/django_messages"
    - or (DO THIS) grab the release source tar ball for the release you want to build.

- move the following files out from the source code into `django_messages_build`:

    - django_messages/build/LICENSE
    - django_messages/build/MANIFEST.in
    - django_messages/build/setup.py
    - django_messages/README.md

- make sure you have `setuptools`, `wheel`, and `twine` packages installed in the Python environment you are using to build.
- in the `django_messages_build` folder:

    - build: `python setup.py sdist bdist_wheel`
    - test upload to test.pypi.org: `python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
    - to install from test: `pip install --index-url https://test.pypi.org/simple/ django-basic-messages`
    - if all works OK, upload to pypi.org: `python3 -m twine upload dist/*`
    - install using pip and test: `pip install django-basic-messages`

# More details

- [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)
- semantic versioning: [https://semver.org/](https://semver.org/)
- More details on all the options for setup.py: [https://packaging.python.org/guides/distributing-packages-using-setuptools/](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
- creating releases on github.com: [https://help.github.com/en/github/administering-a-repository/creating-releases](https://help.github.com/en/github/administering-a-repository/creating-releases)
- making your code citable: [https://guides.github.com/activities/citable-code/](https://guides.github.com/activities/citable-code/)
- packaging django apps: [https://docs.djangoproject.com/en/dev/intro/reusable-apps/](https://docs.djangoproject.com/en/dev/intro/reusable-apps/)
