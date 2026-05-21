import unittest
import pandas as pd
import sys
import os

# So Python can find analysis.py
sys.path.insert(0, os.path.dirname(__file__))

class TestStudentAnalysis(unittest.TestCase):

    def setUp(self):
        """Create sample test data"""
        self.df = pd.DataFrame({
            'student_id'          : [1, 2, 3, 4, 5],
            'name'                : ['Alice','Bob','Charlie','Diana','Eve'],
            'total_hours_studied' : [520, 610, 480, 580, 390],
            'rank'                : [3, 1, 5, 2, 4]
        })

    def test_average_hours(self):
        """Test average hours calculation"""
        avg = self.df['total_hours_studied'].mean()
        self.assertEqual(avg, 516.0)
        print(f"\n✅ Average Hours Test Passed: {avg} hrs")

    def test_rank1_student(self):
        """Test rank 1 student is correct"""
        rank1 = self.df[self.df['rank'] == 1].iloc[0]
        self.assertEqual(rank1['name'], 'Bob')
        self.assertEqual(rank1['total_hours_studied'], 610)
        print(f"\n✅ Rank 1 Test Passed: {rank1['name']} - {rank1['total_hours_studied']} hrs")

    def test_last_student(self):
        """Test last ranked student is correct"""
        last = self.df[self.df['rank'] == self.df['rank'].max()].iloc[0]
        self.assertEqual(last['name'], 'Charlie')
        print(f"\n✅ Last Rank Test Passed: {last['name']}")

    def test_hours_are_positive(self):
        """Test no student has negative hours"""
        self.assertTrue((self.df['total_hours_studied'] > 0).all())
        print("\n✅ All Hours Positive Test Passed")

    def test_ranks_are_unique(self):
        """Test no duplicate ranks"""
        self.assertEqual(
            len(self.df['rank']),
            len(self.df['rank'].unique())
        )
        print("\n✅ Unique Ranks Test Passed")


if __name__ == '__main__':
    unittest.main()