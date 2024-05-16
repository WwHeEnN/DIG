# bw commented below 
# from .models import GCNConv, GINConv, GINConv_mask, GCNConv_mask, GCN_2l_mask, GCN_2l, GCN_3l, GCN_3l_BN, GIN_2l, GIN_3l, \
#     GIN_2l_mask, GNNPool, GNNBasic, GlobalMeanPool, GraphSequential, IdenticalPool 
from models import GCNConv,GCN_2l
from model_manager import load_model, config_model
from utils import ReadOut
