.. SPDX-FileCopyrightText: 2023-2024 Anna <cyber@sysrq.in>
.. SPDX-License-Identifier: WTFPL
.. No warranty.

Release Notes
=============

1.0.0
-----

- **Gone**: Python 3.10 support.

- Fix metadata schema violation for URLs with whitespace in them.

*Generators changelog:*

- **Ruby Gem**:

  - Support extracting metadata from Gemspec files, not just Gems.

*Tests changelog:*

- Monkey patch :pypi:`build` so it doesn't call Pip. With this change, ``--net``
  option became obsolete and was removed.

- Add ``--with-ruby`` flag to enable tests that need Ruby.

0.4.1
-----

- **New generators**:

  * Perl CPAN::Meta::Spec
  * Ruby Gem

*Tests changelog:*

- Add command-line flags to control tests selection.

*Documentation changelog:*

- Fix configuration of Sphinx plugins.

0.4.0
-----

- **New generators**:

  * Apache Maven POM
  * Dart Pubspec
  * GNU Autoconf
  * NuGet
  * PEAR/PECL
  * Python Setuptools
  * Python Wheel

- **New**: ``--quick`` option to skip slow generators.

- Add ``kde-invent`` to known remote-ids.

- Trim ".git" suffix when extracting remote-id.

- Don't write :file:`metadata.xml` if there are no changes.

*Dependencies introduced:*

* :pypi:`lxml`
* :pypi:`build` *(optional)*

0.3.1
-----

- Replace NIH metadata parser with Portage API-based parser.

- Replace use of :py:func:`os.getlogin` with a more reliable implementation.

- Support setting ``EPREFIX`` via cli.

0.3.0
-----

- **New generators**:

  * DOAP
  * Haskell Hpack
  * Python PKG-INFO

*Dependencies introduced:*

* :pypi:`pkginfo` *(optional)*
* :pypi:`rdflib` *(optional)*

*Documentation changelog:*

- Add Sphinx documentation.

0.2
---

- **New generators**:

  * Bower
  * Node.js NPM
  * PHP Composer
  * Rust Cargo

*Packaging:*

- Change Python dist-name from "gentle" to "gentle-mxml".

- Include tests in sdist.

0.1
---

- First release.
