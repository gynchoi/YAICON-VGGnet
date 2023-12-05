from ImageBind.imagebind.models import imagebind_model_modify
from ImageBind.imagebind import data
import torch


class ImageBindEmbedding:
    def __init__(self):
        
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"

        # Instantiate model
        self.model = imagebind_model_modify.imagebind_huge(pretrained=True)
        self.model.eval()
        # freeze imagebind
        for param in self.model.parameters():
            param.requires_grad = False
        self.model.to(self.device)
        
    def __call__(self, input_list, type):
        if type == 'text':
            inputs = {
                imagebind_model_modify.ModalityType.TEXT: data.load_and_transform_text(input_list, self.device)
            }
            # print(data.load_and_transform_text(input_list, self.device).shape)
        elif type == 'vision':
            inputs = {
                imagebind_model_modify.ModalityType.VISION: data.load_and_transform_vision_data(input_list, self.device)
            }
        elif type == 'audio':
            inputs = {
                imagebind_model_modify.ModalityType.AUDIO: data.load_and_transform_audio_data(input_list, self.device)
            }
        else:
            raise Exception("type: text, vision, audio")
        with torch.no_grad():
            embedding = self.model(inputs)
        return embedding
    
    
    
    