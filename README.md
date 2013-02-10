VintageousEx
============

<a href='http://www.pledgie.com/campaigns/19202'><img alt='Click here to lend your support to: Vintageous and make a donation at www.pledgie.com !' src='http://www.pledgie.com/campaigns/19202.png?skin_name=chrome' border='0' /></a>

A rendition of Vim's command-line mode for Sublime Text 3.

<!-- License
=======

This whole package is distributed under the MIT license (see LICENSE.txt).

Compatibility
=============

VintageousEx aims at full cross-platform compatibility. Howerver, I cannot test
under OS X, so patches and feedback are welcome.

Installation
============

Download the `latest version`_, put it under ``Installed Packages`` and restart
Sublime Text.

.. _latest version: https://bitbucket.org/guillermooo/VintageousEx/downloads/VintageousEx.sublime-package
.. TOOD: add link to Vintage's help file

**VintageousEx doesn't replace Vintage**: To use vi key bindings, you need to
enable the `Vintage`_ package (shipped with Sublime Text and *ignored* by default).

.. _Vintage: http://www.sublimetext.com/docs/2/vintage.html

VintageousEx extends the vi-like functionality provided py Vintage by adding
a command-line mode that tries to remain close to Vim's.

Also, because VintageousEx uses commands in the Vintage package, this package
must be under your ``Packages`` folder with that name. This is mostly important
to keep in mind if you contribute code to Vintage and have deleted the original
package.

Overview
========

To open the command line, press ``:``.

VintageousEx offers tab completion of top-level commands, so you can type a letter
and press `Tab` to cycle through available commands.

To see the implemented commands, you can look through ``ex_commands.py``.

Configuration
=============

These settings should be stored in your personal preferences (*Packages/User/Preferences.sublime-settings*).

**VintageousEx_linux_shell** 

The name of the shell through which commands should be executed (``bash``, ``ksh``, etc.).
If empty, the ``$SHELL`` variable will be read when a shell is needed.

**VintageousEx_linux_terminal**

The name of the preferred terminal emulator (``gnome-terminal``, ``xterm``, etc.). If empty,
the variables ``$COLORTERM`` and ``$TERM`` will be read in turn when a terminal is needed.

Donations
=========

If you want to show your appreciation, you can tip me through Gittip: guillermooo_.

.. _guillermooo: http://www.gittip.com/guillermooo/
 -->