import os
from dinov2.data.datasets import ImageNet
root_directory = os.path.expanduser('~/Tensorleap_data/trax_data_dino_v2')

for split in ImageNet.Split:
    dataset = ImageNet(split=split, root=root_directory, extra=root_directory)
    dataset.dump_extra()