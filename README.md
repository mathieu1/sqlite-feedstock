About sqlite
============

Home: http://www.sqlite.org/

Package license: Public-Domain (http://www.sqlite.org/copyright.html)

Feedstock license: BSD 3-Clause

Summary: Implements a self-contained, zero-configuration, SQL database engine.



Current build status
====================

Linux: [![Circle CI](https://circleci.com/gh/conda-forge/sqlite-feedstock.svg?style=shield)](https://circleci.com/gh/conda-forge/sqlite-feedstock)
OSX: [![TravisCI](https://travis-ci.org/conda-forge/sqlite-feedstock.svg?branch=master)](https://travis-ci.org/conda-forge/sqlite-feedstock)
Windows: [![AppVeyor](https://ci.appveyor.com/api/projects/status/github/conda-forge/sqlite-feedstock?svg=True)](https://ci.appveyor.com/project/conda-forge/sqlite-feedstock/branch/master)

Current release info
====================
Version: [![Anaconda-Server Badge](https://anaconda.org/mathieu/sqlite/badges/version.svg)](https://anaconda.org/mathieu/sqlite)
Downloads: [![Anaconda-Server Badge](https://anaconda.org/mathieu/sqlite/badges/downloads.svg)](https://anaconda.org/mathieu/sqlite)

Installing sqlite
=================

Installing `sqlite` from the `mathieu` channel can be achieved by adding `mathieu` to your channels with:

```
conda config --add channels mathieu
```

Once the `mathieu` channel has been enabled, `sqlite` can be installed with:

```
conda install sqlite
```

It is possible to list all of the versions of `sqlite` available on your platform with:

```
conda search sqlite --channel mathieu
```




Updating sqlite-feedstock
=========================

If you would like to improve the sqlite recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`mathieu` channel, whereupon the built conda packages will be available for
everybody to install and use from the `mathieu` channel.
Note that all branches in the conda-forge/sqlite-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](http://conda.pydata.org/docs/building/meta-yaml.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](http://conda.pydata.org/docs/building/meta-yaml.html#build-number-and-string)
   back to 0.
