from copy import deepcopy

import pytest
import torch
from common_utils import assert_equal
from PIL import Image

from torchvision import datapoints


@pytest.mark.parametrize("data", [torch.rand(3, 32, 32), Image.new("RGB", (32, 32), color=123)])
def test_image_instance(data):
    image = datapoints.Image(data)
    assert isinstance(image, torch.Tensor)
    assert image.ndim == 3 and image.shape[0] == 3


@pytest.mark.parametrize("data", [torch.randint(0, 10, size=(1, 32, 32)), Image.new("L", (32, 32), color=2)])
def test_mask_instance(data):
    mask = datapoints.Mask(data)
    assert isinstance(mask, torch.Tensor)
    assert mask.ndim == 3 and mask.shape[0] == 1


@pytest.mark.parametrize("data", [torch.randint(0, 32, size=(5, 4)), [[0, 0, 5, 5], [2, 2, 7, 7]]])
@pytest.mark.parametrize(
    "format", ["XYXY", "CXCYWH", datapoints.BoundingBoxFormat.XYXY, datapoints.BoundingBoxFormat.XYWH]
)
def test_bbox_instance(data, format):
    bboxes = datapoints.BoundingBox(data, format=format, spatial_size=(32, 32))
    assert isinstance(bboxes, torch.Tensor)
    assert bboxes.ndim == 2 and bboxes.shape[1] == 4
    if isinstance(format, str):
        format = datapoints.BoundingBoxFormat[(format.upper())]
    assert bboxes.format == format


@pytest.mark.parametrize(
    ("data", "input_requires_grad", "expected_requires_grad"),
    [
        ([[[0.0, 1.0], [0.0, 1.0]]], None, False),
        ([[[0.0, 1.0], [0.0, 1.0]]], False, False),
        ([[[0.0, 1.0], [0.0, 1.0]]], True, True),
        (torch.rand(3, 16, 16, requires_grad=False), None, False),
        (torch.rand(3, 16, 16, requires_grad=False), False, False),
        (torch.rand(3, 16, 16, requires_grad=False), True, True),
        (torch.rand(3, 16, 16, requires_grad=True), None, True),
        (torch.rand(3, 16, 16, requires_grad=True), False, False),
        (torch.rand(3, 16, 16, requires_grad=True), True, True),
    ],
)
def test_new_requires_grad(data, input_requires_grad, expected_requires_grad):
    datapoint = datapoints.Image(data, requires_grad=input_requires_grad)
    assert datapoint.requires_grad is expected_requires_grad


def test_isinstance():
    assert isinstance(datapoints.Image(torch.rand(3, 16, 16)), torch.Tensor)


def test_wrapping_no_copy():
    tensor = torch.rand(3, 16, 16)
    image = datapoints.Image(tensor)

    assert image.data_ptr() == tensor.data_ptr()


def test_to_wrapping():
    image = datapoints.Image(torch.rand(3, 16, 16))

    image_to = image.to(torch.float64)

    assert type(image_to) is datapoints.Image
    assert image_to.dtype is torch.float64


def test_to_datapoint_reference():
    tensor = torch.rand((3, 16, 16), dtype=torch.float64)
    image = datapoints.Image(tensor)

    tensor_to = tensor.to(image)

    assert type(tensor_to) is torch.Tensor
    assert tensor_to.dtype is torch.float64


def test_clone_wrapping():
    image = datapoints.Image(torch.rand(3, 16, 16))

    image_clone = image.clone()

    assert type(image_clone) is datapoints.Image
    assert image_clone.data_ptr() != image.data_ptr()


def test_requires_grad__wrapping():
    image = datapoints.Image(torch.rand(3, 16, 16))

    assert not image.requires_grad

    image_requires_grad = image.requires_grad_(True)

    assert type(image_requires_grad) is datapoints.Image
    assert image.requires_grad
    assert image_requires_grad.requires_grad


def test_detach_wrapping():
    image = datapoints.Image(torch.rand(3, 16, 16), requires_grad=True)

    image_detached = image.detach()

    assert type(image_detached) is datapoints.Image


def test_other_op_no_wrapping():
    image = datapoints.Image(torch.rand(3, 16, 16))

    # any operation besides the ones listed in `Datapoint._NO_WRAPPING_EXCEPTIONS` will do here
    output = image * 2

    assert type(output) is torch.Tensor


@pytest.mark.parametrize(
    "op",
    [
        lambda t: t.numpy(),
        lambda t: t.tolist(),
        lambda t: t.max(dim=-1),
    ],
)
def test_no_tensor_output_op_no_wrapping(op):
    image = datapoints.Image(torch.rand(3, 16, 16))

    output = op(image)

    assert type(output) is not datapoints.Image


def test_inplace_op_no_wrapping():
    image = datapoints.Image(torch.rand(3, 16, 16))

    output = image.add_(0)

    assert type(output) is torch.Tensor
    assert type(image) is datapoints.Image


def test_wrap_like():
    image = datapoints.Image(torch.rand(3, 16, 16))

    # any operation besides the ones listed in `Datapoint._NO_WRAPPING_EXCEPTIONS` will do here
    output = image * 2

    image_new = datapoints.Image.wrap_like(image, output)

    assert type(image_new) is datapoints.Image
    assert image_new.data_ptr() == output.data_ptr()


@pytest.mark.parametrize(
    "datapoint",
    [
        datapoints.Image(torch.rand(3, 16, 16)),
        datapoints.Video(torch.rand(2, 3, 16, 16)),
        datapoints.BoundingBox([0.0, 1.0, 2.0, 3.0], format=datapoints.BoundingBoxFormat.XYXY, spatial_size=(10, 10)),
        datapoints.Mask(torch.randint(0, 256, (16, 16), dtype=torch.uint8)),
    ],
)
@pytest.mark.parametrize("requires_grad", [False, True])
def test_deepcopy(datapoint, requires_grad):
    if requires_grad and not datapoint.dtype.is_floating_point:
        return

    datapoint.requires_grad_(requires_grad)

    datapoint_deepcopied = deepcopy(datapoint)

    assert datapoint_deepcopied is not datapoint
    assert datapoint_deepcopied.data_ptr() != datapoint.data_ptr()
    assert_equal(datapoint_deepcopied, datapoint)

    assert type(datapoint_deepcopied) is type(datapoint)
    assert datapoint_deepcopied.requires_grad is requires_grad
    assert datapoint_deepcopied.is_leaf
