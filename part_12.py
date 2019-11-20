import arcade
import os
import math

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

MOVEMENT_SPEED = 5
ANGLE_SPEED = 5

class Bullet(arcade.Sprite):
    def __init__(self,image,center_x,center_y,angle,scale):
        super().__init__(image, scale)
        self.bulletSpeed = 1
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
    def update(self):
        self.center_x += -self.bulletSpeed * math.sin(math.radians(self.angle))
        self.center_y += self.bulletSpeed * math.cos(math.radians(self.angle))

class PlayerShip(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 0

    def update(self):
        angle = math.radians(self.angle)
        self.angle += self.change_angle
        self.center_x += -self.speed * math.sin(angle)
        self.center_y += self.speed * math.cos(angle)


class Enemy(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)





class Spaceshooter(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT,"SPACE SHOOTER")
        self.frame_count = 0
        """LISTS"""
        self.player_list = None
        self.enemy_list = None
        self.enemybullet_list = None
        self.bullet_list = None
        """Early Setup"""
        self.player_sprite = None
        self.bullet_sprite = None

        self.score = 0
        self.remove = 0
        """Remove Mouse Cursor"""
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """PLAYER"""
        self.player_list = arcade.SpriteList()
        self.player_sprite = PlayerShip("slimeBlock.png", .4)
        self.player_sprite.center_x = WINDOW_WIDTH / 2
        self.player_sprite.center_y = WINDOW_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        self.bullet_list = arcade.SpriteList()
        self.enemybullet_list = arcade.SpriteList()

        self.enemy_list = arcade.SpriteList()
        self.Enemy_sprite = Enemy("slimeBlock.png", .4)
        self.Enemy_sprite.center_x = WINDOW_WIDTH -50
        self.Enemy_sprite.center_y = WINDOW_HEIGHT -50
        self.enemy_list.append(self.Enemy_sprite)


    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemybullet_list.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        """ replace on_update function"""
        self.frame_count += 1
        self.player_list.update()
        self.bullet_list.update()
        self.enemybullet_list.update()
        self.enemy_list.update()
        for enemy in self.enemy_list:
            start_x = enemy.center_x
            start_y = enemy.center_y

            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y

            angle = math.atan2(y_diff, x_diff)

            enemy.angle = math.degrees(angle) - 90
            if self.frame_count % 40 == 0:
                bullet = Bullet("New Piskel.gif",start_x,start_y,math.degrees(angle)-90,10)
                self.enemybullet_list.append(bullet)
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemybullet_list)
        for bullet in hit_list:
            bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):

        # Forward
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.speed = MOVEMENT_SPEED
        # Back
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.speed = -MOVEMENT_SPEED

        elif key == arcade.key.SPACE:
            bullet = Bullet("New Piskel.png",self.player_sprite.center_x,self.player_sprite.center_y,self.player_sprite.angle,2)
            self.bullet_list.append(bullet)
            print(self.player_sprite.angle)
            print(bullet.angle)



        # Rotate left/right
        if key == arcade.key.Q:
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.E:
            self.player_sprite.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):

        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.speed = 0
        elif key == arcade.key.E or key == arcade.key.Q:
            self.player_sprite.change_angle = 0
def main():
    window = Spaceshooter()
    window.setup()
    arcade.run()
main()

