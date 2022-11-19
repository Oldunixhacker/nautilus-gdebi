# GDebi Package Installer for Nautilus

Installs Debian packages quickly with the Nautilus (GNOME Files) file context
menu.

## Motivation

In GNOME, the default app to open `.deb` packages is the Archive Manager.
This is because GNOME is not specific to Debian and is not developed by
Debian. Also, there are a few cases when GNOME Software, which creates the
"Software Install" desktop file, is not available. An example is Manjaro,
where Software is replaced with the more advanced Pamac.

This Nautilus Python add-on adds the option to install the package you have
easily, by right-clicking and selecting "Install Debian Package".

## Install

You must have `gdebi-gtk` installed.

There's no package for this extension, but you can install manually:

1. Run the following command to create the folder where Nautilus scripts
   are located: `mkdir ~/.local/share/nautilus-python/extensions`
2. Go to that directory with: `cd ~/.local/share/nautilus-python/extensions`
3. Download the script: `wget https://raw.githubusercontent.com/TylerMS887/nautilus-gdebi/main/nautilus-gdebi.py`
4. Restart all instances of Nautilus.
