# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:23:26 2018

@author: sdong
"""

import tensorflow as tf

graph=tf.get_default_graph()

'''
with tf.Session() as sess:
    sess.run(f)
'''

# constant
a=tf.constant(1.0)
a
print(a)

with tf.Session() as sess:
    print(sess.run(a))
    

# variables
    
b=tf.Variable(2.0,name='test_var')
b

init_op=tf.global_variables_initializer()