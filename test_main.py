def test_case(p_case):
    if p_case == 0:
        import PythonRendererCode.feature_manger as feamgr
        print('display sphere')
        feamgr.display_sphere()
    elif p_case == 1:
        import PythonRendererCode.resource_manager as rscmgr
        rscmgr.current_canvas.init_canvas(10, 5, 'red')
        rscmgr.current_canvas.draw_canvas()
    elif p_case == 2:
        import PythonRendererCode.resource_manager as rscmgr
        from PythonRendererCode.GraphEntities.Triangle import Triangle
        from PythonRendererCode.GraphEntities.Point import Point
        rscmgr.current_canvas.init_canvas(200, 200, 'light blue')
        rscmgr.set_draw_mode_point()
        # =================
        # set triangle
        # =================
        l_triangle = Triangle()
        l_point1 = Point()
        l_point1.set_point([0, 0, 0, 1], [15, 20, 0])
        l_point2 = Point()
        l_point2.set_point([0, 0, 0, 1], [150, 100, 0])
        l_point3 = Point()
        l_point3.set_point([0, 0, 0, 1], [20, 110, 0])
        l_triangle.set_point(l_point1, l_point2, l_point3)

        rscmgr.current_canvas.set_entity(l_triangle, [0, 0], rscmgr.current_draw_mode)
        rscmgr.current_canvas.draw_canvas()

# =================
# 0 |   display_sphere()  (this test will be remove after the feature_manager is disused)
# 1 |   canvas test for default red color
# 2 |   canvas test for paint triangle
# =================
test_case(2)
