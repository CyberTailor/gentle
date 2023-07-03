.. SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
.. SPDX-License-Identifier: WTFPL
.. No warranty.

Release Notes
=============

0.4.0
-----
* New generator: Apache Maven POM
* New generator: Dart Pubspec
* New generator: PEAR/PECL
* Add ``kde-invent`` remote-id
* Trim ".git" suffix when extracting remote-id

0.3.1
-----

* Replace NIH metadata parser with Portage API-based parser
* Replace use of ``os.getlogin`` with a more reliable implementation
* Support setting ``EPREFIX`` via cli
