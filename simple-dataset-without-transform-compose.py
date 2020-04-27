import torch
from torch.utils.data import Dataset


class toy_set(Dataset):
    def __init__(self, length=100, transform=None):
        self.x = 2*torch.ones(length, 2)
        self.y = torch.ones(length, 1)
        self.len = length
        self.transform = transform

    def __getitem__(self, index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)
        return sample

    def __len__(self):
        return self.len


class add_mult(object):
    def __init__(self, add_x=1, mult_y=1):
        self.add_x = add_x
        self.mult_y = mult_y

    def __call__(self, sample):
        x = sample[0]
        y = sample[1]
        x = x + self.add_x
        y = y + self.mult_y
        sample = x,y
        return sample


transform = add_mult()
dataset = toy_set()
dataset_tr = toy_set(transform=transform)
# print(dataset.len)
# print(dataset.x)
# print(dataset.y)


# print(dataset.__getitem__(0))
# print(dataset[0])

# for i in range(3):
#     x, y = dataset[i]
#     print(i, ":", "x: ", x, "y:", y)

# print("Before Applying Transformation")
# print(dataset.__getitem__(0))
# print(dataset[0])
#
# print("After Applying Transformation")
# print(dataset_tr.__getitem__(0))
# print(dataset_tr[0])
