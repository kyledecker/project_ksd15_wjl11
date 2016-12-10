def show_rgb(rgb):
    """
    display RGB image from pixel array

    :param rgb: N x M x 3 RGB pixel array
    """
    from PIL import Image
    import numpy as np

    rgb = rgb.astype(dtype=np.uint8)
    img = Image.fromarray(rgb, 'RGB')
    img.show()


def get_iterable(x):
    """
    convert int value into iterable array

    :param x:
    :return: iterable array
    """
    import collections
    if isinstance(x, collections.Iterable):
        return x
    else:
        return x,


def rgbstring2index(rgbstring):
    """
    converts RGB string into array containing corresponding channel indices

    :param rgbstring: string of letters specifying desired color channels
    :return: array of rgb channel index (np.array)
    """
    import numpy as np
    from accessory import get_iterable

    idx = np.array([])
    if 'r' in rgbstring.lower():
        idx = np.append(idx, 0)

    if 'g' in rgbstring.lower():
        idx = np.append(idx, 1)

    if 'b' in rgbstring.lower():
        idx = np.append(idx, 2)

    idx = idx.astype('int')

    return get_iterable(idx)
