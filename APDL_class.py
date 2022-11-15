# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:54:26 2022

@author: Jacky Li
"""

class APDL_class:
    
    def __init__(self):
        ##TODO##
        # finish setting up class attributes
        
        return
    
    def parse_input(self, input):
        ##TODO##
        # input : from Korali Opt
        # output : constructed geometry mapdl object
        return
    
    def mesh_apdl(self, args):
        ##TODO##
        # input : object
        # output : finished meshing object
        return
    
    def apply_loads_boundary_conditions(self):
        ##TODO##
        # input: 
        # output: 
        return
    
    def FEA_compute():
        ##TODO##
        # input: 
        # output: 
        return
    
    # getting results
    def get_stiffness(self):
        ##TODO##
        # input: 
        # output: 
        return
    
    def get_VonMises(self):
        ##TODO##
        # input: 
        # output: 
        return
    
    def get_stiffnesspervolume(self):
        ##TODO##
        # input: 
        # output: 
        return
    
    def finish_exec(self):
        ##TODO##
        # input: 
        # output: clear up any unsaved changes in mapdl object and record iterations
        return
    
    # utils for creating geometry
    @staticmethod
    def draw_circle(center_x, center_y, l1, l2, theta):
        ##TODO##
        # input : necessary ellipse parameters
        # output : object with created ellipse
        return

if __name__ == '__main__':
    #start testing this script
    print("hello")