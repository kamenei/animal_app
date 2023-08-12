#animal.py
# 必要なモジュールのインポート
from torchvision import transforms
import pytorch_lightning as pl
import torch.nn as nn
# 学習時に使ったのと同じ学習済みモデルをインポート
from torchvision.models import resnet50 

# 学習済みモデルに合わせた前処理を追加
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# ネットワークの定義
class Net(pl.LightningModule):

    def __init__(self):
        super().__init__()

        # 学習時に使ったのと同じ学習済みモデルを定義
        self.model = resnet50(weights=None)  # Note the change here from self.feature to self.model
        num_ftrs = self.model.fc.in_features  # Modified this line
        self.model.fc = nn.Linear(num_ftrs, 2)  # Modified this line

    def forward(self, x):
        # 学習時に使ったのと同じ順伝播
        return self.model(x)  # Modified this line