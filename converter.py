import sys
from pathlib import Path
import os

import cadexchanger.CadExCore as cadex

sys.path.append(os.path.abspath(os.path.dirname(Path(__file__).resolve()) + r"/../../"))
import cadex_license as license


def main(theSource: str, theDest: str):
    aKey = license.Value()

    if not cadex.LicenseManager.Activate(aKey):
        print("Failed to activate CAD Exchanger license.")
        return 1

    aModel = cadex.ModelData_Model()

    print("Conversion started...")

    aReader = cadex.ModelData_ModelReader()
    # Opening and converting the file
    if not aReader.Read(cadex.Base_UTF16String(theSource), aModel):
        print("Failed to open and convert the file " + theSource)
        return 1

    cadex.Base_Settings.Default().SetValue(cadex.Base_Settings.UseExceptions, True)
    try:
        aWriter = cadex.ModelData_ModelWriter()
        # Converting and writing the model to file
        if not aWriter.Write(aModel, cadex.Base_UTF16String(theDest)):
            print("Failed to convert and write the file to specified format " + theDest)
            return 1
    except cadex.Base_Exception as anEx:
        print(anEx.What())
        return 1

    print("Completed")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("    <input_file>  is a name of the STEP file to be read")
        print("    <output_file> is a name of the JT file to Save() the model")     
        sys.exit()

    aSource = os.path.abspath(sys.argv[1])
    aDest = os.path.abspath(sys.argv[2])

    sys.exit(main(aSource, aDest))