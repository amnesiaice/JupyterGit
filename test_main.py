import PythonRendererCode.user_interface as ui
g_max_test_list = [0]


def test_case(p_case):
    if p_case == 0:
        print_test_info(p_case)
        ui.create_empty_canvas(800, 600)


def print_test_info(p_case):
    print('test_case:%d' % p_case)
    if p_case == 0:
        print("Test initialize canvas")


for i in g_max_test_list:
    test_case(i)
