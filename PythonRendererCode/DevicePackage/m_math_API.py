import numpy as np


def vector_length(p_list):
    l_vector = np.array(p_list)
    o_norm = np.linalg.norm(l_vector)
    return o_norm


def is_perpendicular(p_v1, p_v2):
    l_v1 = np.array(p_v1)
    l_v2 = np.array(p_v2)
    if np.dot(l_v1, l_v2) == 0:
        return True
    else:
        return False


def make_world2camera_matrix(p_cam_position, p_cam_look_at, p_cam_top):
    assert len(p_cam_look_at) == 3
    # normalize
    l_cam_direction = np.array(p_cam_look_at)  # z'
    l_cam_direction = l_cam_direction/vector_length(l_cam_direction)
    l_cam_top = np.array(p_cam_top)  # y'
    l_cam_top = l_cam_top/vector_length(l_cam_top)
    l_cross_vector = np.cross(l_cam_direction, l_cam_top)  # x' = z' x y'
    l_cross_vector = l_cross_vector/vector_length(l_cross_vector)
    l_matrix_rotate = np.array(
        [
            [l_cross_vector[0], l_cross_vector[1], l_cross_vector[2]],
            [l_cam_top[0], l_cam_top[1], l_cam_top[2]],
            [l_cam_direction[0], l_cam_direction[1], l_cam_direction[2]],
        ]
    )
    l_matrix_rotate = np.linalg.inv(l_matrix_rotate)

    o_matrix = [
        [l_matrix_rotate[0][0], l_matrix_rotate[0][1], l_matrix_rotate[0][2], p_cam_position[0]],
        [l_matrix_rotate[1][0], l_matrix_rotate[1][1], l_matrix_rotate[1][2], p_cam_position[1]],
        [l_matrix_rotate[2][0], l_matrix_rotate[2][1], l_matrix_rotate[2][2], p_cam_position[2]],
        [0.0, 0.0, 0.0, 1.0],
                ]
    return list(o_matrix)


def point_transform(p_transform_matrix, p_point):
    assert len(p_point) >= 3
    assert len(p_transform_matrix) == 4
    assert len(p_transform_matrix[0]) == 4
    l_matrix = np.array(p_transform_matrix)
    l_point = np.array(p_point[0:3])
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
