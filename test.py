from src import save_savefile
from src.code_generator import coded_gen, add_count
import os
import uuid
import time

test_path = os.path.abspath(__file__)

test1 = save_savefile.AutoCodedFileName()
test2 = save_savefile.AutoCodedFileName(coded_gen(uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=test_path)))
test3 = save_savefile.AutoCodedFileName(coded_gen(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())))

print(test_path)
print(test1.coded(test_path))
print(test1.coded(test_path))
print(test2.coded(test_path))
print(test3.coded(test_path))
