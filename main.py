import CSVParser
import torch
from torch import nn
from torch.utils.data import DataLoader

playerDataDir = "./playerData"
parsedPlayerDataDir = "./parsedPlayerData"

CSVParser.parsePlayerData(playerDataDir , parsedPlayerDataDir)