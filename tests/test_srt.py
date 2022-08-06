import unittest

from src.content_miner.file_loader import _remove_srt


class RemoveSrtTestCase(unittest.TestCase):
    def test_srt(self):
        srt = '''\
1
00:31:37,894 --> 00:31:39,928
OK, look, I think I have a plan here.

2
00:31:39,931 --> 00:31:41,931
Using mainly spoons,

3
00:31:41,933 --> 00:31:43,435
we dig a tunnel under the city and release it into the wild.

'''
        srt_removed = "OK, look, I think I have a plan here. Using mainly spoons, we dig a tunnel under the city and " \
                      "release it into the wild."

        self.assertEqual(_remove_srt(srt), srt_removed)
