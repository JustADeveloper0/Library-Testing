import pygame, sys, math

class Circle:
    def __init__(self, window: object, position: list, color: list, radius: int, width: int = 0, dtr: bool = False, dtl: bool = False, dbl: bool = False, dbr: bool = False) -> object:
        self.window=window
        self.position=position
        self.color=color
        self.radius=radius
        self.width=width
        self.dtr=dtr
        self.dtl=dtl
        self.dbl=dbl
        self.dbr=dbr

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.position, self.radius, self.width, self.dtr, self.dtl, self.dbl, self.dbr)

class Rectangle:
    def __init__(self, window: object, position:list, color: list, size: list, width: int = 0, border_radius: int = -1, btlr: int = -1, btrr: int = -1, bblr: int = -1, bbrr: int = -1) -> object:
        self.window=window
        self.color=color
        self.position=position
        self.size=size
        self.width=width
        self.border_radius=border_radius
        self.btlr=btlr
        self.btrr=btrr
        self.bblr=bblr
        self.bbrr=bbrr

    def draw(self):
        rect=pygame.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        pygame.draw.rect(self.window, self.color, rect, self.width, self.border_radius, self.btlr, self.btrr, self.bblr, self.bbrr)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

class Line:
    def __init__(self, window: object, color: list, start_pos: list, end_pos: list, width: int = 1) -> object:
        self.window=window
        self.color=color
        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width=width

    def draw(self):
        pygame.draw.line(self.window, self.color, self.start_pos, self.end_pos, self.width)

class Polygon:
    def __init__(self, window: object, color: list, points: list, width: int = 0) -> object:
        self.window=window
        self.color=color
        self.points=points
        self.width=width

    def draw(self):
        pygame.draw.polygon(self.window, self.color, self.sequence, self.width)

class Arc:
    def __init__(self, window: object, color: list, position: list, size: list, start_angle: float, stop_angle: float, width: int = 1) -> object:
        self.window=window
        self.color=color
        self.position=position
        self.size=size
        self.start_angle=start_angle
        self.stop_angle=stop_angle
        self.width=width

    def draw(self):
        rect=pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.arc(self.window, self.color, rect, self.start_angle, self.stop_angle, self.width)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

class Ellipse:
    def __init__(self, window: object, color: list, position: list, size: list, width: int = 0) -> object:
        self.window=window
        self.color=color
        self.position=position
        self.size=size
        self.width=width

    def draw(self):
        rect=pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.ellipse(self.window, self.color, rect, self.width)

class Lines:
    def __init__(self, window: object, color: list, closed: bool, points: list, width: int = 1) -> object:
        self.window=window
        self.color=color
        self.closed=closed
        self.points=points
        self.width=width

    def draw(self):
        pygame.draw.lines(self.window, self.color, self.closed, self.points, self.width)

class Aaline:
    def __init__(self, window: object, color: list, start_pos: list, end_pos: list, blend: int = 1) -> object:
        self.window=window
        self.color=color
        self.start_pos=start_pos
        self.end_pos=end_pos
        self.blend=blend

    def draw(self):
        pygame.draw.aaline(self.window, self.color, self.start_pos, self.end_pos, self.blend)

class Aalines:
    def __init__(self, window: object, color: list, closed: bool, points: list, blend: int = 1) -> object:
        self.window=window
        self.color=color
        self.closed=closed
        self.points=points
        self.blend=blend

    def draw(self):
        pygame.draw.lines(self.window, self.color, self.closed, self.points, self.blend)

class Text:
    def __init__(self, window: object, color: list, position: list, font: object, size: int, text: str, antialias: bool) -> object:
        self.window = window
        self.color = color
        self.position = position
        self.font = font
        self.size = size
        self.text = text
        self.antialias = antialias

    def draw(self):
        font = pygame.font.Font(self.font, int(self.size))
        text = font.render(self.text, self.antialias, self.color)
        self.window.blit(text, self.position)

class Input:
    def __init__(self, window: object, text_color: list, border_visible: bool, position: list, font: object, border_size: list, text_size: int, buffer_time: int, border_color: list = [255,255,255], border_width: int = 1, border_radius: int = -1, antialias: bool = False) -> object:
        self.window = window
        self.text_color = text_color
        self.border_visible = border_visible
        self.position = position
        self.font = font
        self.border_size = border_size
        self.text_size = text_size
        self.border_color = border_color
        self.border_radius = border_radius
        self.border_width = border_width
        self.antialias = antialias
        self.keys_index_held = set()
        self.reset_time = 0
        self.buffer_time = buffer_time
        self.selected = False
        self.text = ""

    def draw(self):
        rect=pygame.Rect(self.position[0],self.position[1],self.border_size[0],self.border_size[1])
        pygame.draw.rect(self.window, self.border_color, rect, self.border_width, self.border_radius)

        font = pygame.font.Font(self.font, int(self.text_size))
        text = font.render(self.text, self.antialias, self.text_color)
        self.window.blit(text, self.position)

        if self.selected:
            keys = pygame.key.get_pressed()
           
            if self.reset_time == self.buffer_time:
                self.keys_index_held = set()
                self.reset_time = 0
            else:
              self.reset_time += 1
           
            if keys[pygame.K_BACKSPACE] and pygame.key.key_code("backspace") not in self.keys_index_held:
                self.text = self.text[:-1]
                self.keys_index_held.add(pygame.key.key_code("backspace"))
            else:
                for index in range(len(keys)):
                    if keys[index] and index not in self.keys_index_held:
                        self.text += pygame.key.name(index)
                        self.keys_index_held.add(index)
                        break

        mouse_pos = pygame.mouse.get_pos()

        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.selected = True
       
        if not rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.selected = False

    def get_text(self):
        return self.text

class Camera:
    instance = None

    def __new__(cls, window: object, speed: int):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.window = window
            cls.instance.position = [0, 0]
            cls.instance.following_object_id = None
            cls.speed = speed
        return cls.instance

    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y

    def follow_object(self, id: str):
        self.following_object_id = id
               
class Sprite: ######################### CREATE A WAY TO FIND SIZE FOR COLLISION ##############################
    def __init__(self, window: object, image_path: str, position: list, convert: bool = False, convert_alpha: bool = False) -> object:
        self.window=window
        self.image_path=image_path
        self.position=position
        self.convert=convert
        self.convert_alpha=convert_alpha

    def draw(self):
        if self.convert:
            image=pygame.image.load(self.image_path).convert()
            self.window.blit(image, self.position)
        if self.convert_alpha:
            image=pygame.image.load(self.image_path).convert_alpha()
            self.window.blit(image, self.position)
        if self.convert != True and self.convert_alpha != True:
            image=pygame.image.load(self.image_path)
            self.window.blit(image, self.position)

    def get_rect(self) -> pygame.Rect:
        if self.convert:
            rect = pygame.image.load(self.image_path).convert().get_rect()
            rect.center = [self.position[0], self.position[1]]
            return rect
        if self.convert_alpha:
            rect = pygame.image.load(self.image_path).convert_alpha().get_rect()
            rect.center = [self.position[0], self.position[1]]
            return rect
        rect = pygame.image.load(self.image_path).get_rect()
        rect.center = [self.position[0], self.position[1]]
        return rect
   
class Group:
    def __init__(self, objects: list):
        self.objects = []

        for object in objects:
            self.objects.append(object)

    def add(self, objects: list):
        for obj in objects:
            self.objects.append(obj)
           
    def is_empty(self):
        return not self.objects > 0

    def get(self, object: object):
        for obj in self.objects:
            if obj == object:
                return object
               
    def get_objects(self):
        return self.objects

    def remove(self, object: object):
        for obj in self.objects:
            if obj == object:
                self.objects.remove(object)
               
    def clear(self):
        self.objects = []

class ObjectlessGroup(Group):
    def __init__(self, objects_with_id: list[list]):
        self.objects = []

        for object in objects_with_id:
            self.objects.append([object[0], object[1]])

    def add(self, objects_with_id: list[list]):
        for obj in objects_with_id:
            self.objects.append(obj)
           
    def is_empty(self):
        return not self.objects > 0

    def get(self, id: str):
        for obj in self.objects:
            if obj[1] == id:
                return obj[0]
               
    def get_objects(self):
        return self.objects

    def remove(self, id: str):
        for obj in self.objects:
            if obj[1] == id:
                self.objects.remove([obj[0], obj[1]])
               
    def clear(self):
        self.objects = []

class Dodge:
    def __init__(self, background_color: list, size: list, fps: int, after_images: bool, caption: str = None, image_path: str = "") -> object:
        pygame.init()
        pygame.display.set_caption(caption)
        if len(image_path) > 0:
            icon = pygame.image.load(image_path)
            pygame.display.set_icon(icon)
        self.width,self.height=size[0],size[1]
        self.window=pygame.display.set_mode(size)
        self.clock=pygame.time.Clock()
        self.bg=background_color
        self.fps=fps
        self.after_images=after_images
        self.objects=[]
        self.events=[]
        self.functions=[]
        self.groups=[]
        self.objectless_groups=[]
        self.clicked_objects=set()
        self.delta_time=0
        self.camera=None

    def create_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                for func in self.events:
                    if func[2] == True:
                        if event.type == pygame.KEYDOWN:
                            if event.key == getattr(pygame, func[4]):
                                func[1]()
                    elif func[3] == True:
                        if event.type == pygame.KEYUP:
                            if event.key == getattr(pygame, func[4]):
                                func[1]()
                    else:
                        if event.type == getattr(pygame, func[0]):
                            func[1]()

            self.delta_time = self.clock.tick(self.fps) / 1000

            if not self.after_images:
                self.window.fill(self.bg)

            self.clicked_objects = set()

            for object in self.objects:
                if isinstance(object[0], Camera):
                    camera = object[0]
                    if camera.following_object_id != None:
                        for obj in self.objects:
                            if isinstance(obj[0], Camera) != True:
                                if isinstance(obj[0], Circle) or isinstance(obj[0], Rectangle) or isinstance(obj[0], Arc) or isinstance(obj[0], Ellipse) or isinstance(obj[0], Sprite):
                                    if obj[1] != camera.following_object_id:
                                        keys=pygame.key.get_pressed()
                                        if keys[pygame.K_w]:
                                            vector = [0, 1]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].position[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].position[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_s]:
                                            vector = [0, -1]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].position[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].position[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_a]:
                                            vector = [1, 0]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].position[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].position[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_d]:
                                            vector = [-1, 0]

                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].position[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].position[1] += vector[1] * camera.speed * self.get_delta_time()
                                if isinstance(obj[0], Line) or isinstance(obj[0], Aaline):
                                    if obj[1] != camera.following_object_id:
                                        keys=pygame.key.get_pressed()
                                        if keys[pygame.K_w]:
                                            vector = [0, 1]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].start_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].start_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[1] += vector[1] * camera.speed * self.get_delta_time()

                                        if keys[pygame.K_s]:
                                            vector = [0, -1]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].start_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].start_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_a]:
                                            vector = [1, 0]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].start_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].start_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_d]:
                                            vector = [-1, 0]

                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            obj[0].start_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].start_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[0] += vector[0] * camera.speed * self.get_delta_time()
                                            obj[0].end_pos[1] += vector[1] * camera.speed * self.get_delta_time()
                                if isinstance(obj[0], Lines) or isinstance(obj[0], Aalines) or isinstance(obj[0], Polygon):
                                    if obj[1] != camera.following_object_id:
                                        keys=pygame.key.get_pressed()
                                        if keys[pygame.K_w]:
                                            vector = [0, 1]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            for point in obj[0].points:
                                                point[0] += vector[0] * camera.speed * self.get_delta_time()
                                                point[1] += vector[1] * camera.speed * self.get_delta_time()

                                        if keys[pygame.K_s]:
                                            vector = [0, -1]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            for point in obj[0].points:
                                                point[0] += vector[0] * camera.speed * self.get_delta_time()
                                                point[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_a]:
                                            vector = [1, 0]
                                           
                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            for point in obj[0].points:
                                                point[0] += vector[0] * camera.speed * self.get_delta_time()
                                                point[1] += vector[1] * camera.speed * self.get_delta_time()
                                        if keys[pygame.K_d]:
                                            vector = [-1, 0]

                                            length = math.sqrt(vector[0]**2+vector[1]**2)
                                            if length!=0:
                                                vector[0]/=length
                                                vector[1]/=length

                                            for point in obj[0].points:
                                                point[0] += vector[0] * camera.speed * self.get_delta_time()
                                                point[1] += vector[1] * camera.speed * self.get_delta_time()
                else:
                    object[0].draw()

            for function in self.functions:
                function[0]()

            pygame.display.flip()
            self.clock.tick(self.fps)

    def __repr__(self) -> str:
        return f"SIZE: ({self.width}, {self.height}), FPS: {self.fps}, AFTER_IMAGES: {self.after_images}, BACKGROUND: {self.bg}, OBJECTS: {self.objects}"
       
    def create_circle(self, id: str, position: list, color: list, radius: int, width: int = 0, dtr: bool = False, dtl: bool = False, dbl: bool = False, dbr: bool = False):
        circle=Circle(self.window, position, color, radius, width, dtr, dtl, dbl, dbr)
        self.objects.append([circle, id])

    def create_rectangle(self, id: str, position: list, color: list, size: list, width: int = 0, border_radius: int = -1, btlr: int = -1, btrr: int = -1, bblr: int = -1, bbrr: int = -1):
        rect=Rectangle(self.window, position, color, size, width, border_radius, btlr, btrr, bblr, bbrr)
        self.objects.append([rect, id])

    def create_line(self, id: str, color: list, start_pos: list, end_pos: list, width: int = 1):
        line=Line(self.window, color, start_pos, end_pos, width)
        self.objects.append([line, id])

    def create_polygon(self, id: str, color: list, points: list, width: int = 0):
        polygon=Polygon(self.window, color, points, width)
        self.objects.append([polygon, id])

    def create_arc(self, id: str, color: list, position: list, size: list, start_angle: float, stop_angle: float, width: int = 1):
        arc=Arc(self.window, color, position, size, math.radians(start_angle), math.radians(stop_angle), width)
        self.objects.append([arc, id])

    def create_ellipse(self, id: str, color: list, position: list, size: list, width: int = 0):
        ellipse=Ellipse(self.window, color, position, size, width)
        self.objects.append([ellipse, id])

    def create_lines(self, id: str, color: list, closed: bool, points: list, width: int = 1):
        lines=Lines(self.window, color, closed, points, width)
        self.objects.append([lines, id])

    def create_aaline(self, id: str, color: list, start_pos: list, end_pos: list, blend: int = 1):
        aaline=Aaline(self.window, color, start_pos, end_pos, blend)
        self.objects.append([aaline, id])

    def create_aalines(self, id: str, color: list, closed: bool, points: list, blend: int = 1):
        aalines=Aalines(self.window, color, closed, points, blend)
        self.objects.append([aalines, id])

    def create_text(self, id: str, color: list, position: list, font: object, size: int, text: str, antialias: bool = False):
        text=Text(self.window, color, position, font, size, text, antialias)
        self.objects.append([text, id])

    def create_input(self, id: str, text_color: list, border_visible: bool, position: list, font: object, border_size: list, text_size: int, buffer_time: int, border_color: list = [255,255,255], border_width: int = 1, border_radius: int = -1, antialias: bool = False):
        input=Input(self.window, text_color, border_visible, position, font, border_size, text_size, buffer_time, border_color, border_width, border_radius, antialias)
        self.objects.append([input, id])

    def create_event(self, event: str, function, keydown: bool = False, keyup: bool = False, key: str = "K_a"):
        self.events.append([event, function, keydown, keyup, key])

    def create_camera(self, speed: int = 0):
        camera = Camera(self.window, speed)
        self.objects.append([camera])

    def create_sprite(self, id: str, image_path: str, position: tuple, convert: bool = False, convert_alpha: bool = False):
        sprite = Sprite(self.window, image_path, position, convert, convert_alpha)
        self.objects.append([sprite, id])

    def create_group(self, id: str, objects: list):
        group = Group(objects)
        self.groups.append([group, id])

    def create_objectless_group(self, id: str, objects_with_id: list[list]):
        objectless_group = ObjectlessGroup(objects_with_id)
        self.objectless_groups.append([objectless_group, id])

    def remove_object(self, id: str):
        for object in self.objects:
            if isinstance(object[0], Camera) != True:
                if object[1] == id:
                    self.objects.remove([object[0], object[1]])
                    del object[0]
            else:
                if id.lower() == "camera":
                    self.objects.remove([object[0], id])
                    del object[0]

    def remove_object_by_object(self, obj: object):
        for object in self.objects:
            if object[0] == obj:
                self.objects.remove([object[0], object[1]])
                del object[0]

    def remove_group(self, id: str):
        for group in self.groups:
            if group[1] == id:
                self.groups.remove([group[0], group[1]])
                del group[0]

    def remove_objectless_group(self, id: str):
        for objectless_group in self.objectless_groups:
            if objectless_group[1] == id:
                self.objectless_groups.remove([objectless_group[0], objectless_group[1]])
                del objectless_group[0]
                
    def remove_function(self, id: str):
        for function in self.functions:
            if function[1] == id:
                self.functions.remove([function[0], function[1]])

    def check_rectangle_collision(self, rect_1: object, rect_2: object, function):
        def new_function():
            rectangle_1_rect = rect_1.get_rect()
            rectangle_2_rect = rect_2.get_rect()

            if rectangle_1_rect.colliderect(rectangle_2_rect):
                function()

        self.insert_function("rectangle-collision-function", new_function)

    def check_circle_collision(self, circle_1: object, circle_2: object, function):
        def new_function():
            x_axis = circle_1.position[0] - circle_2.position[0]
            y_axis = circle_1.position[1] - circle_2.position[1]
            length = math.sqrt(x_axis**2 + y_axis**2)
           
            if length <= circle_1.radius + circle_2.radius:
                function()
       
        self.insert_function("circle-collision-function", new_function)

    def check_rectangle_clicked(self, rect: object, function, holding: bool = False):

        def new_function():
            def check_inside():
                mouse_pos = pygame.mouse.get_pos()
                rect_rect = rect.get_rect()

                if rect_rect.collidepoint(mouse_pos) and rect not in self.clicked_objects:
                    function()
                    if not holding:
                        self.clicked_objects.add(rect)

            self.create_event("MOUSEBUTTONDOWN", check_inside)

        self.insert_function("rectangle-click-function", new_function)

    def insert_function(self, id:str, function):
        self.functions.append([function, id])

    def get_function(self, id:str):
        for function in self.functions:
            if function[1] == id:
                return function[0]

    def get_object(self, id: str) -> object:
        for object in self.objects:
            if isinstance(object[0], Camera) != True:
                if object[1]==id:
                    return object[0]
            else:
                if id.lower() == "camera":
                    return object[0]
                
    def get_id(self, obj: object):
        for object in self.objects:
            if object[0] == obj:
                return object[1]
               
    def get_group(self, id: str) -> object:
        for group in self.groups:
            if group[1] == id:
                return group[0]
            
    def get_objectless_group(self, id: str) -> object:
        for objectless_group in self.objectless_groups:
            if objectless_group[1] == id:
                return objectless_group[0]
           
    def get_mouse(self, id: str) -> object:
        return pygame.mouse
           
    def get_delta_time(self):
        return self.delta_time
