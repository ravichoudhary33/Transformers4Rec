#
# Copyright (c) 2021, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Block related imports
from .block.base import Block, BlockBase, SequentialBlock, build_blocks, right_shift_block
from .block.mlp import MLPBlock
from .block.transformer import TransformerBlock

# Features related imports
from .features.continuous import ContinuousFeatures
from .features.embedding import (
    EmbeddingFeatures,
    FeatureConfig,
    SoftEmbedding,
    SoftEmbeddingFeatures,
    TableConfig,
)
from .features.sequence import SequenceEmbeddingFeatures, TabularSequenceFeatures
from .features.tabular import TabularFeatures

# Model related imports
from .model.head import (
    BinaryClassificationTask,
    Head,
    NextItemPredictionTask,
    PredictionTask,
    RegressionTask,
)
from .model.model import Model
from .tabular.aggregation import (
    ConcatFeatures,
    ElementwiseSum,
    ElementwiseSumItemMulti,
    StackFeatures,
)
from .tabular.tabular import (
    AsTabular,
    FilterFeatures,
    MergeTabular,
    SequentialTabularTransformations,
    TabularAggregation,
    TabularBlock,
    TabularModule,
    TabularTransformation,
)
from .tabular.transformations import StochasticSwapNoise, TabularLayerNorm
from .trainer import Trainer

__all__ = [
    "SequentialBlock",
    "right_shift_block",
    "build_blocks",
    "BlockBase",
    "TabularBlock",
    "Block",
    "MLPBlock",
    "TabularTransformation",
    "SequentialTabularTransformations",
    "TabularAggregation",
    "StochasticSwapNoise",
    "TabularLayerNorm",
    "TransformerBlock",
    "ContinuousFeatures",
    "EmbeddingFeatures",
    "SoftEmbeddingFeatures",
    "TabularSequenceFeatures",
    "SequenceEmbeddingFeatures",
    "FeatureConfig",
    "TableConfig",
    "TabularFeatures",
    "Head",
    "Model",
    "PredictionTask",
    "AsTabular",
    "ConcatFeatures",
    "FilterFeatures",
    "ElementwiseSum",
    "ElementwiseSumItemMulti",
    "MergeTabular",
    "StackFeatures",
    "BinaryClassificationTask",
    "RegressionTask",
    "NextItemPredictionTask",
    "TabularModule",
    "SoftEmbedding",
    "Trainer",
]

try:
    from .data import DataLoader, DataLoaderValidator  # noqa: F401

    __all__.append("DataLoader")
except ImportError:
    pass