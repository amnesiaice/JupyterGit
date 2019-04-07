import numpy as np


def vector_length(p_list):
    l_vector = np.array(p_list)
    o_norm = np.linalg.norm(l_vector)
    return o_norm


def make_world2camera_matrix(p_cam_position, p_cam_direction):
    o_matrix = []
    return o_matrix


def point_transform(p_transform_matrix, p_point):
    assert len(p_point) == 3
    assert len(p_transform_matrix) == 4
    assert len(p_transform_matrix[0]) == 4
    l_matrix = np.array(p_transform_matrix)
    l_point = np.array(p_point)
    o_point = np.matmul(l_matrix, np.append(l_point, 1))
    return list(o_point[0:3])


if __name__ == "__main__":
    print('#1')
    __test_list = [1.0, 1.0]
    print("norm of (1, 1): %f" % vector_length(__test_list))

    print('#2')
    __test_point = [1.0, 1.0, 1.0]
    __move_matrix = [
        [1.0, 0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    __rotate_matrix = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.577, -0.5, 0.0],
        [0.0, 0.5, 0.577, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    print("move x+1 of (1,1,1) is %s" % point_transform(__move_matrix, __test_point))
    print("rotate x+1 of (1,1,1) is %s" % point_transform(__rotate_matrix, __test_point))
    print(vector_length(point_transform(__rotate_matrix, __test_point)))
