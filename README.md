<!-- SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in> -->
<!-- SPDX-License-Identifier: CC0-1.0 -->

gentle
======

[![Build Status](https://drone.tildegit.org/api/badges/CyberTaIlor/gentle/status.svg)](https://drone.tildegit.org/CyberTaIlor/gentle)

**Gent**oo **L**azy **E**ntry — a `metadata.xml` generator.

If you need a distro-agnostic solution, try [upstream-ontologist][u-o]!

[u-o]: https://github.com/jelmer/upstream-ontologist


Supported generators
--------------------

* Crystal ([Shards](https://github.com/crystal-lang/shards/blob/master/docs/shard.yml.adoc))
* Haskell ([Hpack](https://github.com/sol/hpack/blob/main/README.md))
* Java ([Maven](https://maven.apache.org/pom.html))
* Node.js ([npm](https://docs.npmjs.com/files/package.json/), [Bower](https://github.com/bower/spec/blob/master/json.md))
* PHP ([Composer](https://getcomposer.org/doc/04-schema.md), [PEAR/PECL](https://pear.php.net/manual/en/guide.developers.package2.php))
* Python ([PEP 621](https://peps.python.org/pep-0621/), [PEP 643](https://peps.python.org/pep-0643/))
* Rust ([Cargo](https://doc.rust-lang.org/cargo/reference/manifest.html))

Language-independent:

* [DOAP](https://github.com/ewilderj/doap/wiki)


Dependencies
------------

* [Portage](https://pypi.org/project/portage/)
* [pkginfo](https://pypi.org/project/pkginfo/) *(optional)*
* [PyYAML](https://pyyaml.org/) *(optional)*
* [rdflib](https://pypi.org/project/rdflib/) *(optional)*
* [Tomli](https://pypi.org/project/tomli/) *(optional)*


Installing
----------

### Gentoo

```sh
emerge app-portage/gentle
```

### Other systems

`pip install gentle-mxml --user`


Packaging
---------

You can track new releases using an [atom feed][atom] provided by GitHub.

[atom]: https://github.com/cybertailor/gentle/releases.atom


Contributing
------------

Patches and pull requests are welcome. Please use either [git-send-email(1)][1]
or [git-request-pull(1)][2], addressed to <cyber@sysrq.in>.

If you prefer GitHub-style workflow, use the [mirror repo][gh] to send pull
requests.

Your commit message should conform to the following standard:

```
file/changed: Concice and complete statement of the purpose

This is the body of the commit message.  The line above is the
summary.  The summary should be no more than 72 chars long.  The
body can be more freely formatted, but make it look nice.  Make
sure to reference any bug reports and other contributors.  Make
sure the correct authorship appears.
```

[1]: https://git-send-email.io/
[2]: https://git-scm.com/docs/git-request-pull
[gh]: http://github.com/cybertailor/gentle


License
-------

WTFPL
