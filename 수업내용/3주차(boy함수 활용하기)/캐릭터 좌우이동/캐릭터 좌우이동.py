from pico2d import*

open_canvas()
character=load_image('run_animation.png')
grass=load_image('grass.png')


running = True
x = 0
frame = 0
dir = 0

def handle_events():
    global running,dir
    events=get_events()
    for events in events:
        if events.type == SDL_QUIT:
            running=False
        elif events.type == SDL_KEYDOWN:
            if events.key == SDLK_ESCAPE:
                running=False
            elif events.key == SDLK_LEFT:
                dir -=1
            elif events.key == SDLK_RIGHT:
                dir +=1
        elif events.type == SDL_KEYUP:
            if events.key == SDLK_RIGHT:
                dir -=1
            elif events.key == SDLK_LEFT:
                dir +=1



#-----게임루프-------
while running and x<800:
    clear_canvas()
    
    grass.draw(400, 30)
    
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    
    update_canvas()
    x += dir * 5
    frame = (frame + 1) % 8
    handle_events()

    
    delay(0.01)
 
    
#-------------------

#-------종료--------  
close_canvas()
