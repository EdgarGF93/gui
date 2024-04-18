from pyFAI.gui.model.ImageModel import ImageFromFilenameModel
from pyFAI.gui.model.MaskedImageModel import MaskedImageModel
from pyFAI.io.image import read_image_data
import matplotlib.pyplot as plt

model = ImageFromFilenameModel()
filename = '/scisoft/edgar/ewoksparallel/ewoksparallel/test/config_files/difflab6_eiger2_lab6.edf'

model.setFilename(filename=filename)
data=read_image_data(image_path=filename)
model.setValue(value=data)
model.setSynchronized(True)

print(model.isSynchronized())




data_path = '/scisoft/edgar/ewoksparallel/ewoksparallel/test/config_files/difflab6_eiger2_lab6.edf'
mask_path = '/scisoft/edgar/ewoksparallel/ewoksparallel/test/config_files/eiger_mask.edf'

data = read_image_data(data_path)
mask = read_image_data(mask_path)

image_model = ImageFromFilenameModel()
mask_model = ImageFromFilenameModel()

image_model.setFilename(filename=data_path)
image_model.setValue(value=data)
image_model.setSynchronized(True)


mask_model.setFilename(filename=mask_path)
mask_model.setValue(value=mask)
mask_model.setSynchronized(True)


mask_image_model = MaskedImageModel(image=image_model, mask=mask_model)

fig, axes = plt.subplots(ncols=2)
axes[0].imshow(image_model.value())
axes[0].set_title("Unmasked")
axes[1].imshow(mask_image_model.value())
axes[1].set_title("Masked")

plt.show()