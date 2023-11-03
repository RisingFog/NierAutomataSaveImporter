#!/usr/bin/env python3
"""
NieR: Automata Save Importer - Version 0.1 by Fog

This tool was originally made for the NieR: Automata speedrunning community, in order to modify my practice saves to work for their games.
Inspiration was taken from NieR:AutoModSave by jimmyazrael, but modifies the saves in a different way. 
Instead of requiring GameData.dat, only a single SlotData_X.dat file is required from the user running the program.
This allows not only the header to be modified for the saves to load on a different computer, but it also transfers settings and bindings from the donor save.

As for the actual save data information, it appears that data is stored in Big Endian format. This doesn't matter to us in this case, but it's still good to know.
Save data is tied to the Steam User ID, but the save data itself is not encrypted. This is why using a save without modification does not work.

Relevant save data locations:
    1. 0x4 (4 bytes)        - Steam32 ID
    2. 0x3974c (264 bytes)	- Game settings (not graphics related, that's stored in SystemData.dat)
    3. 0x39854 (172 bytes)  - Custom controller bindings for gamepad and keyboard (4 bytes per button)

Everything else is not modified, so I have not documented it. (TODO: research and document rest of save format)

I've made the extra step to transfer over settings and bindings from a donor save due to the large amount of practice saves made.
Instead of the user re-binding everything manually, this tool handles it for them to make it as plug and play as possible.

Instructions:
    1. If no save file exists, create one within NieR: Automata. Once created, copy the file (SlotData_X.dat, with numbers from 0 to 2 in place of X) into the same directory as this program.
    2. Rename the original save to SlotDataOriginal.dat.
    3. Copy the save(s) you wish to import into the same directory as SlotData_X.dat and this program. Every save within the directory (including sub-folders) will be converted to work with your game.
    4. Run the program. This will complete all of the steps required to make the imported saves work with your copy of the game.

TODO:
    1. Allow input/output paths to be specified.
    2. Options for header only or settings only.
    3. Probably some other stuff which I'm forgetting.
"""

import os, glob, fnmatch

# Open original save file
while not glob.glob("SlotDataOriginal.dat"):
    print("Original save file not found. Please make sure that your original save file is in the same directory and is renamed to SlotDataOriginal.dat.\n\nPress Enter to try again.")
    input()

f = open('SlotDataOriginal.dat', 'rb')

# Declare required variables
steamid = ''
settings = ''
controls = ''

try:
    f.seek(0x4)
    steamid = f.read(4)
    f.seek(0x3974c)
    settings = f.read(264)
    f.seek(0x39854)
    controls = f.read(172)
finally:
    f.close()

# Open all SlotData_X.dat files recursively and write the new values.
for root, dirnames, filenames in os.walk(os.getcwd()):
    for name in fnmatch.filter(filenames, 'SlotData_?.dat'):
        abs = os.path.join(root,name)
        print(f"Processing: {abs}")
        f = open(abs, 'r+b')
        try:
            f.seek(0x4)
            f.write(steamid)
            f.seek(0x3974c)
            f.write(settings)
            f.seek(0x39854)
            f.write(controls)
        finally:
            f.close()

print("All done! The requested saves have been modified and can now be placed in your save directory.\n\nPress Enter to exit.")
input()
