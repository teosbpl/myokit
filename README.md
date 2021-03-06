# Myokit

Myokit is an [open-source](LICENSE) Python-based toolkit that facilitates modeling and simulation of cardiac cellular electrophysiology.

For details and downloads, see [myokit.org](http://myokit.org)

For the latests documentation, see [docs.myokit.org](http://docs.myokit.org)

_Please note: The github repository contains the development version of Myokit, [official releases are found here](http://myokit.org)._

## Quick-start guide

To install Myokit, follow the [guidelines on the download pages](http://myokit.org/download).

After installation, to quickly test if Myokit works, open a terminal or command window, navigate to the myokit directory and type

    python myo run example
    
To open an IDE window, type

    python myo
    
To see what else the `myo` script can do, type

    python myo -h

## Adding icons etc.
If you're a Gnome or KDE user, you may wish to install a Myokit icon to your menu, add the mime-type information for Myokit `.mmt` files or add syntax highlighting for gtksourceview (Gedit). Scripts to do this are located in
    
    ./install/gnome-kde

Windows users can install icons using the [Myokit installer for Windows](http://myokit.org/windows).

## Using Myokit as a library
If you want to be able to access Myokit from outside the Myokit directory (so that `import myokit` will work in any Python program), run:

    python setup.py develop
