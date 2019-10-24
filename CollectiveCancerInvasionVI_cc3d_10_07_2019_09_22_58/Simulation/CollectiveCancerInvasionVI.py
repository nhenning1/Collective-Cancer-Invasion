
from cc3d import CompuCellSetup
        


from CollectiveCancerInvasionVISteppables import ConstraintInitializerSteppable

CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))




from CollectiveCancerInvasionVISteppables import GrowthSteppable

CompuCellSetup.register_steppable(steppable=GrowthSteppable(frequency=1))




from CollectiveCancerInvasionVISteppables import MitosisSteppable

CompuCellSetup.register_steppable(steppable=MitosisSteppable(frequency=1))




from CollectiveCancerInvasionVISteppables import DeathSteppable

CompuCellSetup.register_steppable(steppable=DeathSteppable(frequency=1))



from CollectiveCancerInvasionVISteppables import ChemotaxisSteering

CompuCellSetup.register_steppable(steppable=ChemotaxisSteering(frequency=10))

'''
from CollectiveCancerInvasionVISteppables import ConnectivityElongationSteppable

CompuCellSetup.register_steppable(steppable=ConnectivityElongationSteppable(frequency=1))

CompuCellSetup.run()
'''

'''
from CollectiveCancerInvasionVISteppables import CellMotilitySteppable

CompuCellSetup.register_steppable(steppable=CellMotilitySteppable(frequency=30))
'''


from CollectiveCancerInvasionVISteppables import BuildWall3DSteppable

CompuCellSetup.register_steppable(steppable=BuildWall3DSteppable(frequency=1))


CompuCellSetup.run()
