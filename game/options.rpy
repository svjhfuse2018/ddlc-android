

## TO!DONE: thank you, lolbot! Displays current script:line and screen, file:line
python early:
    def widget__info():
        import os
        def editoverlay():
            fullfn, line = renpy.get_filename_line()
            ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=0, xminimum=200)
            ui.text(u"%s:%d" % (os.path.basename(fullfn), line), size=16)
            if renpy.current_screen() is None:
                return
            ui.button(clicked=None, xpos=0.75, xanchor=1.0, ypos=2, xpadding=0, xminimum=200)
            ui.text(u"%s, %s" % (renpy.current_screen(), str(renpy.current_screen()._location)), size=16)
            out_str = "scr %s (%s), fl %s:%d" % (renpy.current_screen(), str(renpy.current_screen()._location), os.path.basename(fullfn), line)
            print out_str.encode('utf-8')
        config.overlay_functions.append(editoverlay)
init 9000 python:
    if config.developer:
        widget__info()












define config.name = "Doki Doki Literature Club!"





define gui.show_name = False




define config.version = "1.1.0"





define gui.about = _("")






define build.name = "DDLC"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
















define config.save_directory = "DDLC-1454445547"







define config.window_icon = "gui/window_icon.png"



define config.allow_skipping = True

define config.autosave_slots = 8
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init 65533 python:
    config.has_autosave = True  # TO!DONE: see #1 for more details
    config.autosave_on_quit = True
    config.autosave_frequency = 10  # FIX!ME: lagging? Nope.
    config.save_on_mobile_background = True
    config.quit_on_mobile_background = False

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:




















    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "audio")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)









    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False











define build.itch_project = "teamsalvato/ddlc"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
