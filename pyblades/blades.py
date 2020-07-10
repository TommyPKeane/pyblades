#!/usr/bin/env python3
# @file
# @brief
# 
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2016, Tommy P. Keane
# @website https://www.tommypkeane.com


# Python Standard Library
import math;
import cmath;


class Blade(object):
    """
    """

   def __init__(self, n, l, k,):
      """
      Args:
         self ():
         n (int):
         l (int):
         k (int):
      """
      self.dimensionality = n;
      self.plicality = l;
      self.gradality = k;
      return (None);
   # fed

   def isVector(self,):
      """Report if this blade is a "vector"
      """
      self.IS_VECTOR = bool(self.gradality == 1);
      return (self.IS_VECTOR);
   # fed

   def isScalar(self,):
      """Report if this blade is a "scalar"
      """
      self.IS_SCALAR = bool(self.gradality == 0);
      return (self.IS_SCALAR);
   # fed

   def isPseudoscalar(self,):
      """Report if this blade is a "scalar"
      """
      self.IS_PSEUDOSCALAR = bool(self.gradality == self.dimensionality);
      return (self.IS_PSEUDOSCALAR);
   # fed

   def __mul__(self, b):
      """Compute the Inner-Product between this blade and the provided blade.
      """
      if not isinstance(b, Blade):
         raise ValueError("Inner-Product is only computable between 'Blade' instances." );
      elif not (self.dimensionality == b.dimensionality):
         raise ValueError("Blades need to be in the same Space.")
      else:
         pass;
      # fi

      inner_prod = None;

      return (inner_prod)
   # fed

   def __rmul__(self, a):
      """Compute the Inner-Product between this blade and the provided object.
      """
   # fed

   def __matmul__(self, b,):
      return (None);
   # fed

   def __rmatmul__(self, b,):
      return (None);
   # fed

   def __gt__(self, b,):
      return (None);
   # fed

   def __lt__(self, b,):
      return (None);
   # fed

   def __add__(self, b,):
      return (None);
   # fed
# ssalc
