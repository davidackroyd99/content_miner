import unittest

from src.content_miner.analysis import analyse_content


class AnalysisIntegrationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        text = "Cuando me despierto, el otro lado de la cama está frío. La cara de Prim es fresca."
        self.analysed_content = analyse_content(text, ["cama", "cuando"])

    def test_token_count(self):
        self.assertEqual(self.analysed_content.token_count, 17)

    def test_target_count(self):
        self.assertEqual(self.analysed_content.target_count, 4)

    def test_all_targets(self):
        self.assertListEqual(self.analysed_content.all_targets, ['despertar', 'frío', 'cara', 'fresca'])
