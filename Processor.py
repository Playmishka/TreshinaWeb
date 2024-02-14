from ultralytics import YOLO

class Processor:
  model = YOLO("models/best.pt")

  def proc(self, coef, src):
    self.model.predict(conf=coef, source=src, save=True, project = "./static")