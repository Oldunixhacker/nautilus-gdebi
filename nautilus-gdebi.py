# Nautilus context menu item to install .deb packages.

from gi.repository import Nautilus, GObject, Gio
import subprocess

SUPPORTED_FORMATS = 'application/vnd.debian.binary-package'

class GdebiNautilus(GObject.GObject, Nautilus.MenuProvider):
    def menu_activate_cb(self, menu, file):
        if file.is_gone():
            return

        process = subprocess.run(["gdebi-gtk", file.get_location().get_path()])
        print("%d" % process.returncode)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]

        if not file.get_mime_type() in SUPPORTED_FORMATS:
            return

        # Gnome can only handle file:
        # In the future we might want to copy the file locally
        if file.get_uri_scheme() != 'file':
            return

        item = Nautilus.MenuItem(name='Nautilus::install_traditional_package',
                                 label='Install Debian Package',
                                 tip='Install the software archived in this package')
        item.connect('activate', self.menu_activate_cb, file)
        return item,

    def get_background_items(self, window, file):
        return None
