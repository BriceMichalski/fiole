import inspect
import os


class ModuleUtils:

    @staticmethod
    def getMainModule():
        frame = inspect.stack()[-1]
        mainModule = inspect.getmodule(frame[0])
        return mainModule

    @staticmethod
    def getMainModuleAbsPath():
        mainModule = ModuleUtils.getMainModule()
        return os.path.abspath(mainModule.__file__)

    @staticmethod
    def getApplicationFolder():
        mainModuleAbsPAth = ModuleUtils.getMainModuleAbsPath()
        return os.path.abspath(os.path.dirname(mainModuleAbsPAth))

    @staticmethod
    def getApplicationPackage():
        return ModuleUtils.getApplicationFolder().split("/")[-1]

    @staticmethod
    def getModuleName(path):
        moduleFile = str(path).split("/")[-1]
        moduleName = moduleFile.replace(".py","")
        return moduleName

    @staticmethod
    def getSubPackageChain(path):
        fileAbsPath = str(os.path.abspath(os.path.dirname(path)))
        applicationFolder = ModuleUtils.getApplicationFolder() + "/"
        relativePath = fileAbsPath.replace(applicationFolder,"")
        return relativePath.replace('/','.')

    @staticmethod
    def getImportStringFromPath(path):
        appPackage = ModuleUtils.getApplicationPackage()
        subPackageChain = ModuleUtils.getSubPackageChain(path)
        moduleName = ModuleUtils.getModuleName(path)

        moduleImportString = "{appPackage}.{subPackageChain}.{moduleName}".format(
            appPackage= appPackage,
            subPackageChain= subPackageChain,
            moduleName= moduleName
        )

        return moduleImportString, moduleName
