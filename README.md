# NieR: Automata Save Importer - Version 0.1 by Fog
Allows saves from other users to be modified to work with your copy of the game

## Introduction
This tool was originally made for the NieR: Automata speedrunning community, in order to modify my practice saves to work for their games. Inspiration was taken from NieR:AutoModSave by jimmyazrael, but modifies the saves in a different way. Instead of requiring GameData.dat, only a single SlotData_X.dat file is required from the user running the program. This allows not only the header to be modified for the saves to load on a different computer, but it also transfers settings and bindings from the donor save.

As for the actual save data information, it appears that data is stored in Big Endian format. This doesn't matter to us in this case, but it's still good to know. Save data is tied to the Steam User ID, but the save data itself is not encrypted. This is why using a save without modification does not work.

Relevant save data locations:
1. 0x4 (4 bytes) 	- Steam32 ID
2. 0x3974c (264 bytes)	- Game settings (not graphics related, that's stored in SystemData.dat)
3. 0x39854 (172 bytes) 	- Custom controller bindings for gamepad and keyboard (4 bytes per button)
	
Everything else is not modified, so I have not documented it. (TODO: research and document rest of save format)

I've made the extra step to transfer over settings and bindings from a donor save due to the large amount of practice saves made. Instead of the user re-binding everything manually, this tool handles it for them to make it as plug and play as possible.

## Requirements
### On Linux (Ubuntu 19.10 x86_64)
* Python 2
  * `sudo apt-get update -y && sudo apt-get install -y python2`

## Instructions

### On Windows
1. If no save file exists, create one within NieR: Automata. Once created, copy the file (SlotData_X.dat, with numbers from 0 to 2 in place of X) into the same directory as this program.
2. Rename the original save to SlotDataOriginal.dat.
3. Copy the save(s) you wish to import into the same directory as SlotData_X.dat and this program. Every save within the directory (including sub-folders) will be converted to work with your game.
4. Run the program. This will complete all of the steps required to make the imported saves work with your copy of the game.

### On Linux
* 1 to 3: Follow the above instructions
4. Open a Terminal with a CLI (Command Line Interface). Change into the directory of the program. Run the Python program:
  `python2 NierAutomataSaveImporter.py`
5. Expected output is as such :
```
python2 NierAutomataSaveImporter.py
All done! The requested saves have been modified and can now be placed in your save directory.
```

## TODO
1. Allow input/output paths to be specified.
2. Options for header only or settings only.
3. Probably some other stuff which I'm forgetting.
