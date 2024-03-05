from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Pilih file gambar')
outputPath = easygui.filesavebox(title='Simpan gambar ke...')

inputImage = Image.open(inputPath)
outputImage = remove(inputImage)
outputImage.save(outputPath)
