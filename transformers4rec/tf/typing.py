import sys
import typing
from typing import Dict

import tensorflow as tf

if sys.version_info < (3, 7):
    ForwardRef = typing._ForwardRef  # pylint: disable=protected-access
else:
    ForwardRef = typing.ForwardRef

# TODO: Make this more generic and work with multi-hot features
TabularData = Dict[str, tf.Tensor]
TensorOrTabularData = typing.Union[tf.Tensor, TabularData]

_tabular_module = "transformers4rec.tf.tabular.tabular"
TabularTransformation = ForwardRef(f"{_tabular_module}.TabularTransformation")
TabularAggregation = ForwardRef(f"{_tabular_module}.TabularAggregation")
SequentialTabularTransformations = ForwardRef(f"{_tabular_module}.SequentialTabularTransformations")
TabularTransformationType = ForwardRef(f"{_tabular_module}.TabularTransformationType")
TabularAggregationType = ForwardRef(f"{_tabular_module}.TabularAggregationType")
TabularBlock = ForwardRef(f"{_tabular_module}.TabularBlock")

FeatureAggregator = ForwardRef("transformers4rec.tf.aggregator.FeatureAggregation")
MaskSequence = ForwardRef("transformers4rec.tf.masking.MaskSequence")

Block = ForwardRef("transformers4rec.tf.block.base.Block")
SequentialBlock = ForwardRef("transformers4rec.tf.block.base.SequentialBlock")
BuildableBlock = ForwardRef("transformers4rec.tf.block.base.BuildableBlock")
BlockWithHead = ForwardRef("transformers4rec.tf.block.with_head.BlockWithHead")

Head = ForwardRef("transformers4rec.tf.head.Head")
PredictionTask = ForwardRef("transformers4rec.tf.head.PredictionTask")

LossReduction = typing.Callable[[typing.List[tf.Tensor]], tf.Tensor]

__all__ = [
    "TabularData",
    "TensorOrTabularData",
    "TabularTransformation",
    "TabularAggregation",
    "SequentialTabularTransformations",
    "TabularTransformationType",
    "TabularAggregationType",
    "TabularBlock",
    "LossReduction",
    "FeatureAggregator",
    "MaskSequence",
    "Block",
    "SequentialBlock",
    "BuildableBlock",
    "BlockWithHead",
    "Head",
    "PredictionTask",
]