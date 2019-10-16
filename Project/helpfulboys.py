import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def unflatten(arr):
    return np.reshape(arr, (32, 32, 3))

def display_images_and_labels(ims, labels):
    """Display the first image of each label."""
    unique_labels = set(labels)
    plt.figure(figsize=(15, 15))
    i = 1
    for label in unique_labels:
        # Pick the first image for each label.
        image = ims[labels.index(label)]
        plt.subplot(8, 8, i)  # A grid of 8 rows x 8 columns
        plt.axis('off')
        plt.title("{0} ({1})".format(label, labels.count(label)))
        i += 1
        _ = plt.imshow(unflatten(image))
    plt.show()
    
def display_label_images(ims, label, labels):
    """Display images of a specific label."""
    limit = 32  # show a max of 24 images
    plt.figure(figsize=(15, 5))
    i = 1

    start = labels.index(label)
    end = start + labels.count(label)
    for image in ims[start:end][:limit]:
        plt.subplot(4, 8, i)  # 3 rows, 8 per row
        plt.axis('off')
        i += 1
        plt.imshow(unflatten(image))
    plt.show()

#display_images_and_labels(images, labels)