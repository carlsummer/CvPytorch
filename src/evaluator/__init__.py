# !/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2020/12/16 9:35
# @Author : liumin
# @File : __init__bak.py

from .eval_classification import ClassificationEvaluator
from .eval_detection import VOCEvaluator, COCOEvaluator
from .eval_segmentation import SegmentationEvaluator

__all__ = [
    'ClassificationEvaluator',
    'VOCEvaluator',
    'COCOEvaluator',
    'SegmentationEvaluator']


def build_evaluator(cfg, dataset):
    'Using adapter design patterns'
    if cfg.EVALUATOR.NAME == 'classification':
        return ClassificationEvaluator(dataset)
    elif cfg.EVALUATOR.NAME == 'voc_detection':
        return VOCEvaluator(dataset)
    elif cfg.EVALUATOR.NAME == 'coco_detection':
        return COCOEvaluator(dataset)
    elif cfg.EVALUATOR.NAME == 'segmentation':
        return SegmentationEvaluator(dataset)
    else:
        raise NotImplementedError
