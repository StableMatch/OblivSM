# OblivSM
# MP-SPDZ
Installation & Usage : [MP-SPDZ](https://github.com/data61/MP-SPDZ)  
Add the ```.mpc``` files to ```Programs/Source``` directory.    
Add ```inputs.py``` to ```Player-Data``` directory.  
For generating random inputs run ```python inputs.py <set size>```  or replace ```Input-P0-0``` & ```Input-P1-0``` with custom inputs.    

Modify set size within the ```.mpc``` files before execution to align with the input files set size.
# SCALE-MAMBA
Installation & Usage : [SCALE-MAMBA](https://homes.esat.kuleuven.be/~nsmart/SCALE/Documentation-SCALE.pdf)  
Add the ```.mpc``` files to ```Programs/<file name>``` directory.  
Replace ```Input_Output_Simple.cpp``` & ```Input_Output_Simple.h``` in ```src/Input_Output``` with the provided files & modify ```Line 28``` in ```Input_Output_Simple.cpp``` for reading inputs.  
Add ```inputs.py``` to ```src/Input_Output``` directory.  
For generating random inputs run ```python inputs.py <set size>``` or replace ```input_1.txt``` with custom inputs.    

Modify set size within the ```.mpc``` files before execution to align with the input files set size.
