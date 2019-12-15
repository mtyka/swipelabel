# SwipeLabel
Simple phone web app to label images with swipe gestures. Great for binary or tertiary decisions per image. Basically it's Tinder for labelling training image sets. With a bit of practice 2-3 images per second is feasible.

# Requirements
Python, Flask
```
pip install flask
```
# Run
  * Copy images to `images/` subfolder.
  * `sh run.sh`
  * Navigate to `hostname:5000` with your phone and swipe away. 
  * Results are appended to logfile.log and can be processed later.
