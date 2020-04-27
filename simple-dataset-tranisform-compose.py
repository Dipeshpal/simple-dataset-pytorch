import torch
from torch.utils.data import Dataset
from torchvision import transforms


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


class mult(object):
    def __init__(self, mul=100):
        self.mul = mul

    def __call__(self, sample):
        x = sample[0]
        y = sample[1]
        x = x * self.mul
        y = y * self.mul
        sample = x, y
        return sample


transform = add_mult()
dataset = toy_set()
print(dataset.len)
print(dataset.x)
print(dataset.y)


print(dataset.__getitem__(0))
print(dataset[0])

for i in range(3):
    x, y = dataset[i]
    print(i, ":", "x: ", x, "y:", y)

dataset_tr = toy_set(transform=transform)
print("Before Applying Transformation")
print(dataset.__getitem__(0))
print(dataset[0])

print("After Applying Transformation")
print(dataset_tr.__getitem__(0))
print(dataset_tr[0])

data_transform = transforms.Compose([add_mult(), mult()])

print("Without Transformation- ")
print(dataset[0])

print("With composed transformation of add_mult and mult")
print(data_transform(dataset[1]))
