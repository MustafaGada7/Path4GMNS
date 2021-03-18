import ctypes
import os.path
from sys import platform


if platform.startswith('win32'):
    _dll_file = os.path.join(os.path.dirname(__file__), 'bin/DTALite.dll')
elif platform.startswith('linux'):
    _dll_file = os.path.join(os.path.dirname(__file__), 'bin/DTALite.so')
elif platform.startswith('darwin'):
    _dll_file = os.path.join(os.path.dirname(__file__), 'bin/DTALite.dylib')
else:
    raise Exception('Please build the shared library compatible to your OS\
                    using source files')

_dtalite_engine = ctypes.cdll.LoadLibrary(_dll_file)

_dtalite_engine.network_assignment.argtypes = [ctypes.c_int, 
                                               ctypes.c_int,
                                               ctypes.c_int]


def perform_network_assignment_DTALite(assignment_mode, 
                                       iter_num,
                                       column_update_num):
    """ python interface to call DTALite (precompiled as shared library)

    WARNING
    -------
        MAKE SURE TO BACKUP agent.csv and link_performance.csv if you have 
        called perform_network_assignment() before. Otherwise, they will be 
        overwritten by results generated by DTALite.
    
    Parameters
    ----------
    assignment_mode
        0: Link based UE, only produces link performance file without agent 
           path file 
        1: Path based UE, produces link performance file and agent path file 
        2: UE + dynamic traffic assignment and simulation , produces link 
           performance file and agent path file 
        3: ODME
    iter_num
        number of assignment iterations to be performed before optimizing
        column pool
    column_update_iter
        number of iterations to be performed on optimizing column pool

    Outputs
    -------
    agent.csv
    link_performance.csv

    Notes
    -----
        The parameters are exactly the same as do_network_assignment()
        The outputs are exactly the same as output_link_performance()
    """
    print('\nDTALite run starts')
    
    _dtalite_engine.network_assignment(assignment_mode, 
                                       iter_num,
                                       column_update_num)

    print('\nDTALite run completes')