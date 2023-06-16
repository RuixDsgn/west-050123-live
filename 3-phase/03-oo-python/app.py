# Our Run File

from lib.pet import * 

import ipdb
import os

os.system("clear")
chauncy = Pet("Chauncy", 11, "mutt", "sleepy")
cosmo = Pet("Cosmo", 12, "beardie", "nuts")
chauncy.print_details()
cosmo.print_details()
cosmo.print_details()

chauncy.tell_other_pet_i_said_hi(cosmo)

ipdb.set_trace()
print("DONE!")