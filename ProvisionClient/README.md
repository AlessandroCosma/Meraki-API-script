## ProvisionClient.py:
   This script uploads in the Meraki Console a target list of devices.
    
 ### INPUT:
   * **API KEY:** The API KEY to interact with the target Meraki console
   * **NETWORK ID:** The NETWORK ID of the target Meraki console
   * **CONFIGURATION FILE:** The name of the file with the configuration. This file MUST be a *.txt* and it MUST contain a list of devices, with the following syntax:
      
      ```
      MAC-ADDRESS;DESCRIPTION
      
      MAC-ADDRESS;DESCRIPTION
     
      ...
      
      MAC-ADDRESS;DESCRIPTION
      ```
       **N.B.** The file must be located in the same folder where the script is run.
     
       **N.B.** The file name passed as input MUST NOT include the .*txt* extension.
     
   * **GROUP POLICY NAME**: The name of the GROUP POLICY that the user wants to apply
   * **POLICY ID**: ID of the policy in the Meraki console
    
   ### OUTPUT:
   The list of clients configured and available in the Meraki Console
