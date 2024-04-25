from ultralytics import YOLO

class Processor:
  model = YOLO("models/best.pt")
  list_image = []
  procesed_img = []

  def proc(self, coef):
    self.model.predict(conf=coef, source=self.list_image, save=True, project = "./static")