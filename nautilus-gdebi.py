from gi.repository import Nautilus, GObject, Gio
import subprocess

SUPPORTED_FORMATS = "application/vnd.debian.binary-package"

class GNOMEGDebi(GObject.GObject, Nautilus.MenuProvider):
   def menu_activate_ch(self, menu, file):
      if file.is_gone():
        return
   process = subprocess.run(["gdebi-gtk", file])
   print("%d" % process.returncode)
   def get_file_items(self, window, files):
        if len(files) != 1:
            return

        # We're only going to put ourselves on packages context menus
        if not files[0].get_mime_type() in SUPPORTED_FORMATS:
            return

        # Gnome can only handle file:
        # In the future we might want to copy the file locally
        if files[0].get_uri_scheme() != 'file':
            return

        item = Nautilus.MenuItem(name='Nautilus::install_debian',
                                 label='Install Software',
                                 tip='Install this software to your system using GDebi')
        item.connect('activate', self.menu_activate_cb, file)
        return item

   def get_background_items(self, window, file):
        return None

