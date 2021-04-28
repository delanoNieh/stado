from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import torch
from torch import nn

def fill_fc_weights(layers):
    for m in layers.modules():
        if isinstance(m, nn.Conv2d):
            if m.bias is not None:
                nn.init.constant_(m.bias, 0)


class MOC_Branch(nn.Module):
    def __init__(self, input_channel, arch, head_conv, branch_info, K):
        super(MOC_Branch, self).__init__()
        assert head_conv > 0
        wh_head_conv = 64 if arch == 'resnet' else head_conv

        self.hm = nn.Sequential(
            nn.Conv2d(K * input_channel, head_conv,
                      kernel_size=3, padding=1, bias=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(head_conv, branch_info['hm'],
                      kernel_size=1, stride=1,
                      padding=0, bias=True))
        self.hm[-1].bias.data.fill_(-2.19)

        self.mov = nn.Sequential(
            nn.Conv2d(K * input_channel, head_conv,
                      kernel_size=3, padding=1, bias=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(head_conv, branch_info['mov'],
                      kernel_size=1, stride=1,
                      padding=0, bias=True))
        fill_fc_weights(self.mov)

        self.wh = nn.Sequential(
            nn.Conv2d(input_channel, wh_head_conv,
                      kernel_size=3, padding=1, bias=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(wh_head_conv, branch_info['wh'] // K,
                      kernel_size=1, stride=1,
                      padding=0, bias=True))
        fill_fc_weights(self.wh)

        # added for STADO
        self.mgan = MGAN(input_channel)
        fill_fc_weights(self.mgan)

    def forward(self, input_chunk):
        output = {}

        output_wh = []
        output_mgan = []
        for feature in input_chunk:
            output_wh.append(self.wh(feature))
            output_mgan.append(self.mgan(feature))
        output['wh'] = torch.cat(output_wh, dim=1)
        output['mgan'] = torch.cat(output_mgan, dim=1)

        input_chunk = torch.cat(input_chunk, dim=1)
        output['hm'] = self.hm(input_chunk)
        output['mov'] = self.mov(input_chunk)
        return output


# --------------------- added for STADO -----------------------
class MGAN(nn.Module):
    def __init__(self, in_channels, conv_out_channels=512):
        super(MGAN, self).__init__()
        self.convs = nn.ModuleList()
        self.convs.append(nn.Conv2d(in_channels, conv_out_channels, 3, padding=1))
        self.convs.append(nn.Conv2d(conv_out_channels, conv_out_channels, 3, padding=1))
        self.conv_logits = nn.Conv2d(conv_out_channels, 1, 1)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        feat = x
        for conv in self.convs:
            x = conv(x)
            x = self.relu(x)
        out = self.conv_logits(x).sigmoid() * feat
        return out
# -------------------------------------------------------------

