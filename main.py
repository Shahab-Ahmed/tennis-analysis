from utils import read_video, save_video
from trackers import PlayerTracker, BallTracker

def main():
    # Read the video frames
    input_video_path = "input_video/input_video.mp4"
    video_frames = read_video(input_video_path)

    # Detect players from video frames
    player_tracker = PlayerTracker(model_path="yolov8x")
    ball_tracker = BallTracker("models/tennis_ball/last.pt")
    player_detections = player_tracker.detect_frames(video_frames, 
                                                     read_from_stub=True,
                                                     stub_path="tracker_stubs/player_detections.pkl")
    ball_detections = ball_tracker.detect_frames(video_frames, 
                                                     read_from_stub=True,
                                                     stub_path="tracker_stubs/ball_detections.pkl")

    # Draw outputs
    ## Draw player bounding boxes
    output_video_frames = player_tracker.draw_bboxes(video_frames, player_detections)
    output_video_frames = ball_tracker.draw_bboxes(video_frames, ball_detections)

    # Save the video with detections
    save_video(video_frames, "output_videos/output_video.avi")

if __name__ == "__main__":
    main()