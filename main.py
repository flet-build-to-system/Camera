from flet import *

def main(page: Page):
  page.title = "openCamera "
  page.window_width = 800
  page.window_height = 600

  def open_camera(e):
    camera_button.visible = False
    camera_feed.visible = True
    # Initialize camera feed logic here

  camera_button = ElevatedButton("Open Camera", on_click=open_camera)
  camera_feed = CameraFeed()  # Placeholder for actual camera feed component
  camera_feed.visible = False

  page.add(camera_button, camera_feed)

app(target=main)