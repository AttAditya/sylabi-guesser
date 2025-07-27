from mediapipe import solutions
from cv2 import cvtColor, COLOR_BGR2RGB, circle

inf = float('inf')
MOUTH_OPEN_RATIO = 0.35
MOUTH_EEE_RATIO = 0.43
MOUTH_EHH_RATIO = 0.52
MOUTH_OOO_RATIO = 0.60
MOUTH_AAA_RATIO = 0.75

mp_face_mesh = solutions.face_mesh # type: ignore
face_mesh = mp_face_mesh.FaceMesh(
  static_image_mode=False,
  max_num_faces=1
)

def get_lips_landmarks(frame):
  rgb = cvtColor(frame, COLOR_BGR2RGB)
  results = face_mesh.process(rgb)
  lips = []
  corners = {
    "left": (inf, 0),
    "right": (-inf, 0),
    "top1": (0, inf),
    "top2": (0, inf),
    "bottom": (0, -inf),
  }

  if results.multi_face_landmarks:
    for landmark in results.multi_face_landmarks:
      FML = mp_face_mesh.FACEMESH_LIPS
      indices = list(i for pair in FML for i in pair)

      h, w, _ = frame.shape
      for idx in indices:
        x = int(landmark.landmark[idx].x * w)
        y = int(landmark.landmark[idx].y * h)
        lips.append((x, y))

        if x < corners["left"][0]:
          corners["left"] = (x, y)

        if x > corners["right"][0]:
          corners["right"] = (x, y)

        if y > corners["bottom"][1]:
          corners["bottom"] = (x, y)

        if y < corners["top1"][1]:
          corners["top1"] = (x, y)
          continue

        if y <= corners["top2"][1]:
          corners["top2"] = (x, y)

  corners["top"] = (
    (corners["top1"][0] + corners["top2"][0]) // 2,
    (corners["top1"][1] + corners["top2"][1]) // 2
  )

  del corners["top1"]
  del corners["top2"]

  return lips, corners

def draw_lips_landmarks(frame):
  lips, corners = get_lips_landmarks(frame)
  if not lips: return frame

  for x, y in lips:
    circle(frame, (x, y), 3, (0, 0, 255), -1)

  for x, y in corners.values():
    circle(frame, (x, y), 3, (0, 255, 0), -1)

  return frame

def get_mouth_ratio(frame):
  lips, corners = get_lips_landmarks(frame)
  if not lips: return False

  vdiff = corners["bottom"][1] - corners["top"][1]
  hdiff = corners["right"][0] - corners["left"][0]

  ratio = vdiff / hdiff

  return ratio

def classify_mouth_state(frame):
  mouth_ratio = get_mouth_ratio(frame)

  if mouth_ratio > MOUTH_AAA_RATIO:
    return f"AAA"
  
  if mouth_ratio > MOUTH_OOO_RATIO:
    return f"OOO"
  
  if mouth_ratio > MOUTH_EHH_RATIO:
    return f"EHH"

  if mouth_ratio > MOUTH_EEE_RATIO:
    return f"EEE"

  return f"Silent"

