import random
from moviepy.editor import VideoFileClip


def extract_random_clips(video_path, num_clips=3, clip_duration=60):
    video = VideoFileClip(video_path)

    # Get the duration of the video
    video_duration = video.duration

    clips = []

    for _ in range(num_clips):
        # Generate a random start time for the clip
        start_time = random.uniform(0, video_duration - clip_duration)

        # Define the end time of the clip
        end_time = start_time + clip_duration

        # Extract the clip
        clip = video.subclip(start_time, end_time)

        # Store the clip
        clips.append(clip)

    # Save the clips
    for i, clip in enumerate(clips):
        clip_filename = f"clip_{i + 1}.mp4"
        clip.write_videofile(clip_filename, codec="libx264")

    print(f"Extracted {num_clips} clips of {clip_duration} seconds each.")

