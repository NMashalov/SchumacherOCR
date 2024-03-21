def process_img(img: list[np.array]):
    anns_ids = coco.getAnnIds(imgIds=img['id'], catIds=cat_ids, iscrowd=None)
    anns = coco.loadAnns(anns_ids)
    image = np.array(Image.open(img['file_name']).convert('L'))
    cropped_images = []

    for ann in anns:
        x,y,w,h = map(int,ann['bbox'])
        if ann['category_id'] == 0: # only pictures
            cropped_images.append(image[y:y+h,x:x+w])
    return cropped_images