import matplotlib.pyplot as plt
import random


def display(image_generator):

  figure, axes = plt.subplots(nrows = 1, ncols = 5, figsize = (15,20))

  for  i in range(5):

    train_sample = image_generator.next()
    index = random.randint(0,len(train_sample[0]) -1 )
    axes[i].imshow(train_sample[0][index] * 1/255.)
    numeric_label =  [char for char in range(len(train_sample[1][index])) if train_sample[1][1][char] == 1.0][0]
    axes[i].set_title(class_labels[numeric_label])
  plt.show()
  plt.tight_layout()