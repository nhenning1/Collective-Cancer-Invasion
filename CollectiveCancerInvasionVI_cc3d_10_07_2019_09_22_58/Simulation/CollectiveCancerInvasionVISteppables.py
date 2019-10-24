
from cc3d.core.PySteppables import *
from random import uniform


class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self,frequency)

    def start(self):

        for cell in self.cell_list:

            cell.targetVolume = 25
            cell.lambdaVolume = 2.0
         
'''
class ConnectivityElongationSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=10):
        SteppableBasePy.__init__(self,_simulator,_frequency)

    def start(self):
        for cell in self.cellList:
            if cell.type==1:
                cell.connectivityOn = True

            elif cell.type==2:
                cell.connectivityOn = True
'''                
'''                
class ConnectivitySteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
        
    def start(self):
        # will turn connectivity for first n cells
        for cell in self.cell_list:
            if cell.id < 2:
                cell.connectivityOn = True   
                self.connectivityGlobalPlugin.setConnectivityStrength(cell,20000000) 
'''
    
    
class GrowthSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def step(self, mcs):
    
        for cell in self.cell_list:
            cell.targetVolume += .01        

        # # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        

        # field = self.field.CHEMICAL_FIELD_NAME
        
        # for cell in self.cell_list:
            # concentrationAtCOM = field[int(cell.xCOM), int(cell.yCOM), int(cell.zCOM)]

            # # you can use here any fcn of concentrationAtCOM
            # cell.targetVolume += 0.01 * concentrationAtCOM       

        
class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,frequency=1):
        MitosisSteppableBase.__init__(self,frequency)

    def step(self, mcs):

        cells_to_divide=[]
        for cell in self.cell_list:
            if cell.type == 2:
                if cell.volume>75:
                    cells_to_divide.append(cell)
            
            elif cell.type == 2:
                if cell.volume>150:
                    cells_to_divide.append(cell)

        for cell in cells_to_divide:

            self.divide_cell_random_orientation(cell)
            # Other valid options
            # self.divide_cell_orientation_vector_based(cell,1,1,0)
            # self.divide_cell_along_major_axis(cell)
            # self.divide_cell_along_minor_axis(cell)

    def update_attributes(self):
        # reducing parent target volume
        self.parent_cell.targetVolume /= 5.0                  

        self.clone_parent_2_child()            

        # for more control of what gets copied from parent to child use cloneAttributes function
        # self.clone_attributes(source_cell=self.parent_cell, target_cell=self.child_cell, no_clone_key_dict_list=[attrib1, attrib2]) 
        
        if self.parent_cell.type==2:
            self.child_cell.type=2
        else:
            self.child_cell.type=1

        
class DeathSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def step(self, mcs):
        if mcs == 1000:
            for cell in self.cell_list:
                if cell.type==1:
                    cell.targetVolume=0
                    cell.lambdaVolume=100

class ChemotaxisSteering(SteppableBasePy):
    def __init__(self, frequency=50):
        SteppableBasePy.__init__(self, frequency)

    def start(self):

        for cell in self.cell_list:
            if cell.type == self.LEADER:
                cd = self.chemotaxisPlugin.addChemotaxisData(cell, "ATTR")
                cd.setLambda(30.0)
                cd.assignChemotactTowardsVectorTypes([self.MEDIUM, self.FOLLOWER])
                break
            elif cell.type == self.INTERMEDIATE:
                cd = self.chemotaxisPlugin.addChemotaxisData(cell, "ATTR")
                cd.setLambda(10.0)
                cd.assignChemotactTowardsVectorTypes([self.MEDIUM, self.FOLLOWER])
                break

    def step(self, mcs):
        if mcs > 100 and not mcs % 100:
            for cell in self.cell_list:
                if cell.type == self.LEADER:

                    cd = self.chemotaxisPlugin.getChemotaxisData(cell, "ATTR")
                    if cd:
                        lm = cd.getLambda() - 3
                        cd.setLambda(lm)
                    break
                elif cell.type== self.INTERMEDIATE:
                    
                    cd = self.chemotaxisPlugin.getChemotaxisData(cell, "ATTR")
                    if cd:
                        lm = cd.getLambda() - 5
                        cd.setLambda(lm)
                    break
                    
                    
                    
'''class CellMotilitySteppable(SteppableBasePy):
    def __init__(self, frequency=30):
        SteppableBasePy.__init__(self, frequency)

    def step(self, mcs):
        # Make sure ExternalPotential plugin is loaded
        # negative lambdaVecX makes force point in the positive direction

        for cell in self.cellList:
            # force component pointing along X axis
            cell.lambdaVecX = 10.1 * uniform(-0.5, 0.5)
            # force component pointing along Y axis
            cell.lambdaVecY = 10.1 * uniform(-0.5, 0.5)
            
'''

class BuildWall3DSteppable(SteppableBasePy):

    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        self.build_wall(self.WALL)

    def step(self, mcs):
        print('MCS=', mcs)
        if mcs == 4:
            self.destroy_wall()
            self.resize_and_shift_lattice(new_size=(80, 80, 0), shift_vec=(10, 10, 0))
        if mcs == 6:
            self.build_wall(self.WALL)
