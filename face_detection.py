from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n-face.pt")

video_path = "la_cabra.mp4"
if not os.path.isfile(video_path):
    print(f"Error: Video file '{video_path}' not found.")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "processed_la-cabra.mp4", fourcc, fps, (frame_width, frame_height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame)

    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
