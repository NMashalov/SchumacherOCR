# Load model directly
from transformers import AutoImageProcessor, AutoModelForObjectDetection

processor = AutoImageProcessor.from_pretrained("NMashalov/PhysicsYoLO")
model = AutoModelForObjectDetection.from_pretrained("NMashalov/PhysicsYoLO")