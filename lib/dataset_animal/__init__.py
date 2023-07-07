from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .ap10k import AnimalAP10KDataset as ap10k
from .ap10k_fewshot import AnimalAP10KDataset as ap10k_fewshot
from .ap10k_mt_v3 import AnimalAP10KDataset as ap10k_mt_v3
from .ap10k_category import AnimalAP10KDataset as ap10k_category
from .ap10k_test_category import AnimalAP10KDataset as ap10k_test_category

from .animalweb import AnimalAnimalWebDataset as animalweb
from .animalweb_fewshot import AnimalAnimalWebDataset as animalweb_fewshot
from .animalweb_mt_v3 import AnimalAnimalWebDataset as animalweb_mt_v3
