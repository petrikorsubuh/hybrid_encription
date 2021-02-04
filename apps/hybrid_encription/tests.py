from django.test import TestCase
import os
import shutil
import subprocess
from pathlib import Path

# Create your tests here.
# my_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# link_tolib = os.path.join(my_dir,'../../media/files')
# ntru_dir = os.path.join(my_dir, '../hybrid_libs/ntru_ok/priv_key.npz')




# print(link_tolib)
# print(my_dir)
# print(ntru_dir)
# pindah = shutil.move(ntru_dir,link_tolib)
#
# source = Path('../hybrid_libs/ntru_ok/pub_key.npz')
# destination = Path('../../media/files/pub_key.npz')
# shutil.move(source, destination)
# shutil.move(destination, source)




def key_name(a,b):
    source ='../hybrid_libs/ntru_ok/'+ a + '.npz'
    des = '../../media/files/'+ b+'.npz'
    source,des = Path(source),Path(des)
    print(f"public_key : {source} , private_key : {des}")
    return source,des


key_name('key2_pub','key2_priv')
