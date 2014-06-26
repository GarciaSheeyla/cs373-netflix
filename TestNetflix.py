#!/usr/bin/env python3

"""
To test the program:
    % coverage3 run --branch TestNetflix.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# ------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_eval, rmse_map_sum, sqre_diff, netflix_solve, netflix_write

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # read
    # ----
    """
    def test_rmse_map_sum_1 (self) :
        a = [1, 2, 1]
        p = [2, 1, 2]
        r = rmse_map_sum(a, p)
        self.assertEqual(r, 1)

    def test_rmse_map_sum_2 (self):
        a = [2, 3, 4]
        p = [4, 5, 6]
        r = rmse_map_sum(a, p)
        self.assertEqual(r, 2)

    def test_rmse_map_sum_3 (self):
        a = [1, 3, 4]
        p = [3, 1.5, 1]
        r = rmse_map_sum(a, p)
        self.assertEqual(r, 2.2546)

    
    # ---------
    # sqre_diff
    # ---------

    def test_sqre_diff_1 (self) :
        v = sqre_diff(4, 2)
        self.assertEqual(v, 4)

    def test_sqre_diff_2 (self) :
        v = sqre_diff(20, 10)
        self.assertEqual(v, 100)

    def test_sqre_diff_3 (self) :
        v = sqre_diff(0, 10)
        self.assertEqual(v, 100)

    
    # -----
    # write
    # -----

    def test_netflix_write_1 (self) :
        w = StringIO()
        netflix_write(w, 'm', 10851)
        self.assertEqual(w.getvalue(), "10851:\n")

    def test_netflix_write_2 (self) :
        w = StringIO()
        netflix_write(w, 'p', 3.56)
        self.assertEqual(w.getvalue(), "3.6\n")

    def test_netflix_write_3 (self) :
        w = StringIO()
        netflix_write(w, 'r', 1.0031)
        self.assertEqual(w.getvalue(), "RMSE: 1.0031\n")
    """
    # -----
    # solve
    # -----
    
    def test_netflix_solve_1 (self) :
        
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringI0()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(),"1:\n3.7\n3.5\n3.7\nRMSE: 0.5085\n" )
    """
    def test_netflix_solve_2 (self) :
        w = StringIO()
        r = StringIO("10:\n1952305\n1531863\n")
        netflix_solve(r, w)     
        self.assertEqual(w.getvalue(),"10:\n3.3\n3.2\nRMSE: 0.23425\n" )

         
    def test_netflix_solve_3 (self) :
        W = StringIO()
        r = StringIO("1000:\n2326571\n977808\n1010534\n1861759")
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1000:\n3.5\n3.3\n3.1\n4.2\nRMSE: 0.7476\n")

    
    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
         mid = 12944
         cid = 1313436
         pa = netflix_eval(mid,cid)
         self.assertEqual(pa.getvalue(),3)

      

    def test_eval_2 (self) :
         mid = 10
         cid = 1952305
         pa = netflix_eval(mid,cid)
         self.assertEqual(pa.getvalue(),3.3)

        

    def test_eval_3 (self) :
         mid = 1000
         cid = 2326571
         pa = netflix_eval(mid,cid)
         self.assertEqual(pa.getvalue(),3.5)
    """
        

# ----
# main
# ----

main()

