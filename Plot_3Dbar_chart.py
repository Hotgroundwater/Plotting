from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


XX = [5 ,7, 9, 11, 13]### 1,3,5,7 control size of the bar
YY = [20,20,20,20,20]
ZZ = [99,96,94,80,28]###number of models control height of the bar

##99% of Australia’s rice
##94% of Australia cotton
##96% of Orange
##80% of Australia grapes
##28% of Australia’s dairy


LABELS = ['Australia’s Rice','Australia’s Orange','Australia’s Cotton','Australia’s Grapes', 'Australia’s Dairy']
#COLOURS = ['lightcoral','darksalmon','salmon','lightsalmon']
fig = plt.figure(figsize = (20,20))
ax1 = fig.add_subplot(111, projection = '3d')##axisbg='gray'

dx = np.ones(10)##4
dy = np.ones(10)##4
dz = [-99,-96,-94,-80, -28]### to fill the base, opposite to ZZ data


ax1.bar3d(XX, YY,ZZ,dx,dy,dz, alpha=0.5,color= ('aqua','lime','yellow','tomato', 'purple'), linewidth= 1)##color= ('aqua','lime','yellow','tomato','purple')  ##align='center', antialiased=False
#ax1.axis['left'].set_axis_direction('bottom')
ax1.set_zlim3d(0,100)
ax1.zaxis.set_rotate_label(False)
ax1.set_zlabel('MDB agricultural produce (%)', rotation = 92,fontsize = 30, fontweight = 'bold', labelpad = 50)

##ax1.set_xlabel(LABELS, labelpad =30)##new
ax1.yaxis.set_major_locator(plt.NullLocator())

##ax1.set_xticks([])
##ax1.set_yticks([])

tmp_planes = ax1.zaxis._PLANES 
ax1.zaxis._PLANES = ( tmp_planes[2], tmp_planes[3], 
                     tmp_planes[0], tmp_planes[1], 
                     tmp_planes[4], tmp_planes[5])
view_1 = (25, -135)
view_2 = (25, -45)
init_view = view_2
ax1.view_init(*init_view)

##a = ax1.zaxis.label.get_rotation()
##if a < 180:
##   a += 181
##ax1.zaxis.label.set_rotation(a)
##a = ax1.zaxis.label.get_rotation() ### put the actual angle in the z-label
##ax1.set_zlabel(u'number of models developed'.format(a))

####ax1.view_init(ax1.elev, ax1.azim+180)## reverse back to front

ax1.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
ax1.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
ax1.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))

plt.gca().patch.set_facecolor('white')##foreground
plt.tick_params(axis = 'both', which = 'major', labelsize= 30, pad = 20)
plt.xticks(XX, LABELS, fontsize =24,fontweight = 'bold')##XX,fontweight = 'bold'


plt.savefig("C:\\Users\\Nang Kittiya\\Documents\\Python_test\\Out_files\\MDBproduce4"+'.png', transparent = True)
plt.clf()
plt.close()
print("Done")
