import os
import sys
import logging
sys.path.insert(0, os.path.abspath('./src/'))

if __name__ == "__main__":
    from preprocess import read_tiff, rgb_histogram

    rgb = read_tiff(filename='./test/ExampleAbnormalCervix.tif')

    rh, gh, bh = rgb_histogram(rgb, verb=True, exclude_bg=True,
                               upper_lim=(0,  0,  150))
