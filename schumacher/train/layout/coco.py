from pycocotools.coco import COCO
import torchvision 
from pathlib import Path

def read_coco(coco_json_path: Path):

    coco = COCO(coco_json_path)
    cat_ids = coco.getCatIds()

    img = coco.imgs

    x,y,w,h = map(int,ann['bbox'])
    anns_ids = coco.getAnnIds(imgIds=img['id'], catIds=cat_ids, iscrowd=None)
    anns = coco.loadAnns(anns_ids)

    x,y,w,h = map(int,ann['bbox'])
    if ann['category_id'] == 0: # only pictures
        cropped_images.append(image[y:y+h,x:x+w])



class CocoDetection(
torchvision.datasets.CocoDetection):

        self.transform = A.Compose([
                A.RandomCrop(width=450, height=450),
                A.HorizontalFlip(p=0.5),
                A.RandomBrightnessContrast(p=0.2),
            ], bbox_params=A.BboxParams(format='coco',label_fields=['class_labels']))

        self.dataset = []
        for idx in tqdm(range(len(self))):
            img, target = super(CocoDetection, self).__getitem__(idx)

            bbox = [targ['bbox'] for targ in target]
            label = [targ['category_id'] for targ in target]
            try:
                transformed = self.transform(image=np.array(img), bboxes=bbox,class_labels = label, min_area=1024, min_visibility=0.1,)
            except:
                display(img)

            img = transformed['image']

            targ = [
                {
                    'bbox': box,
                    'category_id': label
                }
                for box, label in zip(transformed['bboxes'],transformed['class_labels'])
            ]

            image_id = self.ids[idx]

            target = {'image_id': image_id, 'annotations': target}

            encoding = self.feature_extractor(images=img, annotations=target, return_tensors="pt")


            self.dataset.append((encoding["pixel_values"].squeeze(),encoding["labels"][0] ))
