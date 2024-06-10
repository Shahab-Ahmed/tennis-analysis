## Overview

This is a system used to analyze tennis matches. It extracts the keypoints of the court with a CNN and uses a YOLO model to detect the players and the ball.
It also keeps track of the average player speed and average shot speed.

## Output

https://github.com/Shahab-Ahmed/tennis-analysis/assets/127554002/4cedf7bd-a610-4b04-8dfc-ce4d96808ecd

## Training

1. The keypoints extraction was done by training a CNN. The dataset was obtained from this repo: https://github.com/yastrebksv/TennisCourtDetector 
2. The base YOLO model was performing well on the player detection but not the tennis ball detection. So, a seperate YOLO model was trained on a tennis ball dataset obtained on Roboflow.

## Ideas for Improvement

1. The keypoint detection is not performing well. Improving the accuracy of the keypoints would also increase the accuracy of the speed measurements.
2. Add detection for when the ball hits the net.
3. Add detection for when the ball is out of bounds.
4. The tennis ball location is not consistent on the mini court. 

## Acknowledgements

This project was heavily inspired by the video by "Code In a Jiffy"

Link: https://www.youtube.com/watch?v=L23oIHZE14w
