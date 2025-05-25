import package, pygame, math

program = package.Dodge((0, 255, 0), (800, 800), 120, False, "Program", "assets\download.png")

program.create_sprite("gRY45$", "assets\download.jpeg", [600, 200], False, True)

#program.create_rectangle("g$Gt34g", [100, 600], [255, 255, 0], [100, 100])

program.create_circle("gf45h$g", [100,600], [255, 255, 0], 25)
circle_1 = program.get_object("gf45h$g")

program.create_circle("1gG34", [400, 400], [255, 0, 0], 50)
circle_2 = program.get_object("1gG34")

#program.create_rectangle("gr4e$", [375,375], [0,0,255], [50,50])

program.check_circle_collision(circle_1, circle_2, lambda: program.remove_object("gf45h$g"))

program.create_camera(500)
camera = program.get_object("camera")
camera.follow_object("1gG34")

program.create_loop()
