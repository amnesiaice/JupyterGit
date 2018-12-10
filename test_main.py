def test_case(p_case):
    if p_case == 0:
        import PythonRendererCode.feature_manger as feamgr
        print('display sphere')
        feamgr.display_sphere()
    elif p_case == 1:
        import PythonRendererCode.resource_manager as rcsmgr
        rcsmgr.current_canvas.set_canvas(10, 5, 'red')
        rcsmgr.current_canvas.draw_canvas()
    elif p_case == 2:
        import PythonRendererCode.resource_manager as rcsmgr
        rcsmgr.current_canvas.set_canvas(800, 600, 'light blue')
        rcsmgr.current_canvas.draw_canvas()


# 0 |   display_sphere()  (this test will be remove after the feature_manager is disused)
# 1 |   canvas test for default red color
# 2 |   canvas test for paint something
test_case(1)
