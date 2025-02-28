import unittest
from unittest.mock import patch, mock_open
import os
import hashlib
from file_finder import calc_md5, find_files, build_report_data, create_report

class TestFileFinder(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data=b"test data")
    def test_calc_md5(self, mock_file):
        expected_hash = hashlib.md5(b"test data").hexdigest()
        result = calc_md5("dummy_file.txt")
        self.assertEqual(result, expected_hash)
    
    @patch("os.walk")
    def test_find_files(self, mock_os_walk):
        mock_os_walk.return_value = [
            ("/test", ["subdir"], ["file1.txt", "file2.log"]),
            ("/test/subdir", [], ["file3.txt"])
        ]
        
        result = find_files("/test", "*.txt")
        expected = ["/test/file1.txt", "/test/subdir/file3.txt"]
        self.assertEqual(result, expected)
    
    @patch("file_finder.calc_md5", return_value="dummyhash")
    @patch("os.path.basename", side_effect=lambda x: os.path.split(x)[1])
    @patch("os.path.dirname", side_effect=lambda x: os.path.split(x)[0])
    def test_build_report_data(self, mock_md5, mock_basename, mock_dirname):
        files = ["/test/file1.txt", "/test/subdir/file2.txt"]
        result = build_report_data(files)
        expected = {
            "file1.txt": {"path": "/test", "hash": "dummyhash"},
            "file2.txt": {"path": "/test/subdir", "hash": "dummyhash"}
        }
        self.assertEqual(result, expected)
    
    @patch("builtins.open", new_callable=mock_open)
    def test_create_report(self, mock_file):
        report_data = {
            "file1.txt": {"path": "/test", "hash": "dummyhash"},
            "file2.txt": {"path": "/test/subdir", "hash": "dummyhash"}
        }
        create_report(report_data, "report.txt")
        
        mock_file().write.assert_any_call("file1.txt, /test, dummyhash \n")
        mock_file().write.assert_any_call("file2.txt, /test/subdir, dummyhash \n")
        self.assertEqual(mock_file().write.call_count, 2)

if __name__ == "__main__":
    unittest.main()