import matplotlib.pyplot as plt
import PythonRendererCode.ProjectConst as PrjConst
# My module
import PythonRendererCode.ResourceManager as RscMgr

# test code
print('1')
print(PrjConst.light_direct)

img = RscMgr.blank_target
tex = RscMgr.texture_mario
plt.axis('off')
# plt.imshow(tex)
plt.imshow(img)
plt.show()
