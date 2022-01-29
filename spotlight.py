from shutil import copy
from os import environ, mkdir, chdir, listdir, getcwd, getenv
from os.path import exists, join
from PIL import Image
from configparser import ConfigParser

currentFolder = getcwd()

config = ConfigParser()
result = config.read('config.ini')


assetsFolder = getenv('LOCALAPPDATA')
assetsFolder = join(
    assetsFolder, "Packages", "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy", "LocalState", "Assets")


desktop = join(join(environ['USERPROFILE']), 'Desktop')
defaultOutputPortrait = join(currentFolder, 'portrait')
defaultOutputLandscape = join(currentFolder, 'landscape')


if result == []:
    config.add_section('image')
    config['image']['portrait'] = 'True'
    config['image']['landscape'] = 'True'

    config.add_section('output')
    config['output']['portrait'] = defaultOutputPortrait
    config['output']['landscape'] = defaultOutputLandscape

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        
    print('config.ini file created.')
else:
    imagePortrait = config['image']['portrait'].strip().lower()
    imageLandscape = config['image']['landscape'].strip().lower()

    outputPortrait = config['output']['portrait'].strip()
    outputLandscape = config['output']['landscape'].strip()


    if imagePortrait == 'true':
        imagePortrait = bool(True)
        if outputPortrait == '':
            if not exists(defaultOutputPortrait):
                mkdir(defaultOutputPortrait)
                outputPortrait = defaultOutputPortrait
        else:
            if not exists(outputPortrait):
                mkdir(outputPortrait)
    else:
        imagePortrait = bool(False)

    if imageLandscape == 'true':
        imageLandscape = bool(True)
        if outputLandscape == '':
            if not exists(defaultOutputLandscape):
                mkdir(defaultOutputLandscape)
                outputLandscape = defaultOutputLandscape
        else:
            if not exists(outputLandscape):
                mkdir(outputLandscape)
    else:
        imageLandscape = bool(False)

    chdir(assetsFolder)

    p = 0
    l = 0

    for file in listdir("."):
        image = Image.open(file)

        filename = (file[:6]) + ".jpg"

        # print(filename)

        w, h = image.size

        if w < h:
            if imagePortrait:
                copy(file, join(outputPortrait, filename))
                p += 1
        else:
            if imageLandscape:
                copy(file, join(outputLandscape, filename))
                l += 1

    if imagePortrait:
        print(f"{p} portrait image copied.")


    if imageLandscape:
        print(f"{l} landscape image copied.")
