import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib as mpl
import math
graph_limit = 2
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Tracker Pose')
ax.set_xlim(-graph_limit, graph_limit)
ax.set_ylim(-graph_limit, graph_limit)
ax.set_zlim(-graph_limit, graph_limit)
# Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.linspace(0, 15, 1000)
# yline = np.linspace(0, 15, 1000)
# ax.plot3D(xline, yline, zline, 'gray')

def angle_between(v1, v2):
    # rad
    unit_vector_1 = v1 / np.linalg.norm(v1)
    unit_vector_2 = v2 / np.linalg.norm(v2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle

# vive_pose0 = np.array([2.29, 0.51, -0.08])
# vive_pose1 = np.array([2.25, 0.49, -0.03])
vive_pose0 = np.array([1.2, 0.8, 1.9])
vive_pose1 = np.array([1.4, 1.6, 0.3])
# ax.plot3D([vive_pose0[0], vive_pose1[0]], [vive_pose0[1], vive_pose1[1]], [vive_pose0[2], vive_pose1[2]], 'gray')
moved_vector = np.array(vive_pose1) - np.array(vive_pose0)
ax.plot3D([0, moved_vector[0]], [0, moved_vector[1]], [0, moved_vector[2]], 'grey')
theta_rx = angle_between(np.array([1, 0, 0]), moved_vector)
theta_ry = angle_between(np.array([0, 1, 0]), moved_vector)
theta_rz = angle_between(np.array([0, 0, 1]), moved_vector)

print(f'moved_vector: {moved_vector}')
print(f"theta_x: {theta_rx}, theta_y: {theta_ry}, theta_z: {theta_rz},")
print("degrees: ", math.degrees(theta_rx))

sin_rx, cos_rx = np.sin(theta_rx), np.cos(theta_rx)
sin_ry, cos_ry = np.sin(theta_ry), np.cos(theta_ry)
sin_rz, cos_rz = np.sin(theta_rz), np.cos(theta_rz)

print(f'cos: {cos_rx}, sin: {sin_rx}')
# get the rotation matrix on x axis
R_Mx = np.array([[1, 0, 0],
                 [0, cos_rx, sin_rx],
                 [0, -sin_rx, cos_rx]])
# get the rotation matrix on y axis
R_My = np.array([[cos_ry, 0, -sin_ry],
                 [0, 1, 0],
                 [sin_ry, 0, cos_ry]])
# get the rotation matrix on z axis
R_Mz = np.array([[cos_rz, sin_rz, 0],
                 [-sin_rz, cos_rz, 0],
                 [0, 0, 1]])
# compute the full rotation matrix
# R_M = np.dot(np.dot(R_Mx, R_My), R_Mz)
R_M = np.matmul(R_Mz, R_My)
R_M = np.matmul(R_M, R_Mx)

Original = [np.linalg.norm(moved_vector), 0, 0]
# ax.plot3D([0,Original[0]], [0,Original[1]], [0,Original[2]], 'blue')
print(Original)

print('RM: ', R_Mx)

Rotate_X = np.matmul(R_Mx, np.array([1,0,0]))
Rotate_Y = np.matmul(R_My, Rotate_X)
Rotate_Z = np.matmul(R_Mz, Rotate_Y)
# ax.plot3D([vive_pose0[0],Rotate_X[0]], [vive_pose0[1],Rotate_X[1]], [vive_pose0[2],Rotate_X[2]], 'blue')
ax.plot3D([0, Rotate_X[0]], [0, Rotate_X[1]], [0, Rotate_X[2]], 'red')
ax.plot3D([0, Rotate_Y[0]], [0, Rotate_Y[1]], [0, Rotate_Y[2]], 'green')
ax.plot3D([0, Rotate_Z[0]], [0, Rotate_Z[1]], [0, Rotate_Z[2]], 'blue')

Rotate_ZYX = np.matmul(moved_vector, R_M)
ax.plot3D([0, Rotate_ZYX[0]], [0, Rotate_ZYX[1]], [0, Rotate_ZYX[2]], 'pink')

print(f'X:', Rotate_X)


plt.show()