
from aluneth.rinlearn.cv.utils import *

def load_image_dataset(num,resolution,dataset_name):
    w,h = resolution
    images = torch.zeros([1,4,w,h])
    if dataset_name == "sprites" or dataset_name == "sprite":
        for i in range(num):
            image = load_image("/Users/melkor/Documents/GitHub/euclidean-concept-learner/sprites/train/train_{}.png".format(i))
            image = resize(image,(w,h))
            images = torch.cat([images,image],0)
        return images[1:]