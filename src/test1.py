import arcade


if __name__ == '__main__':
    print('Demo to set up first test game')

    # Open the window. Set the window title and dimensions (width and height)
    arcade.open_window(600, 600, "Explosion game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

    print('Finished')