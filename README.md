# pysnmp
experimental python scripts to communicate to SNMP devices

# How to Run

To load a MIB (Management Information Base) file and display a list of values for a device, you can use the `pysnmp` library in Python. This library provides tools for managing SNMP (Simple Network Management Protocol) devices and working with MIB files. Make sure you have the `pysnmp` library installed before running the script. You can install it using `pip`:

```
pip install pysnmp
```



In this script, replace 'your_mib_file.mib' with the actual path to your MIB file, and 'your_device_ip' and 'your_oid' with the IP address of your device and the specific OID you want to retrieve, respectively.

Make sure the MIB file you are loading contains the definitions for the OIDs you are trying to access. The OID can be in either numeric format (e.g., '1.3.6.1.2.1.1.1.0') or symbolic format (e.g., 'SNMPv2-MIB::sysDescr.0'). The script will print the retrieved values for the specified OID on the device.

The OID for the MOXA E1240 is 
```
SNMPv2-MIB::sysDescr.0 = STRING: E1240
```

# Finding OIDs

To find the OID (Object Identifier) for a specific value on your device, you can use SNMP (Simple Network Management Protocol) tools to walk through the MIB tree and discover the OIDs associated with different variables. There are various SNMP management tools available, but one of the commonly used ones is `snmpwalk`.

`snmpwalk` is a command-line tool that queries SNMP agents for a tree of information. You can use it to explore the OID tree and find the OIDs corresponding to the values you are interested in. Here's how you can use `snmpwalk` to find OIDs for your device:

1. Install `snmpwalk`: If you don't have `snmpwalk` installed, you can install it on your system. The installation process depends on your operating system.

   - For Ubuntu/Debian:
     ```
     sudo apt-get install snmp
     ```

   - For CentOS/RHEL:
     ```
     sudo yum install net-snmp-utils
     ```

   - For macOS (using Homebrew):
     ```
     brew install net-snmp
     ```

2. Use `snmpwalk` to explore the MIB tree: Once you have `snmpwalk` installed, you can run the following command to retrieve the entire MIB tree from your device:

   ```
   snmpwalk -v 2c -c public <your_device_ip>
   ```

   Replace `<your_device_ip>` with the IP address of your device. The community string (`-c public` in the example) might vary depending on your SNMP configuration.

3. Filter the output: The output of `snmpwalk` can be extensive. You can use tools like `grep` (Linux/macOS) or `findstr` (Windows) to filter the output and find specific OIDs associated with the values you're interested in.

   For example, if you're looking for the OID of the system description, you can use `grep` like this:

   ```
   snmpwalk -v 2c -c public <your_device_ip> | grep sysDescr
   ```

   This will show you the OIDs related to the system description on your device.

Note: SNMP communities like "public" are common default values, but in practice, you should use more secure community strings to ensure the security of your SNMP configuration.

Keep in mind that the exact output and OID formatting may vary depending on the device and the SNMP agent running on it. Also, if your device is not configured with the proper MIB, the output might not be human-readable, and you may need to refer to the MIB file associated with your device to interpret the results properly.