from flask import Flask, request, make_response,render_template,send_from_directory
import base64
import os
import sys
import datetime

app = Flask(__name__)

PATH = "images/"
LOGFILE = "logfile.log"

# Load image list
raw_images = os.listdir(PATH)
images = []
proc_images = []
next_image = 0

## read logfile, filter out already-processed images
if os.path.isfile(LOGFILE):
  with open(LOGFILE, "r") as logfile:
    logs = logfile.read()
    for raw in raw_images:
      if raw in logs: proc_images.append(PATH + raw)
      else: images.append(PATH + raw)

# Open logfile in append mode
logfile = open(LOGFILE, "a", 0)

# Custom static data
@app.route('/images/<path:filename>')
def custom_static(filename):
  return send_from_directory('images/', filename)

# Main server
@app.route("/")
def get_image():
  log = request.args.get('log')
  if log:
    print "LOG:", log
    logfile.write(str(datetime.datetime.now()) + " ")
    logfile.write(os.path.basename(log))
    logfile.write("\n");
    next_image += 1

  image_index = request.args.get('image_index')
  if image_index:
    current_image = images[int(image_index)]
  else:
    global next_image
    current_image = images[next_image]

  # Render a new image:
  return render_template('index.html', image=current_image, image_index=image_index)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
