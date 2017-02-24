from conans import ConanFile, ConfigureEnvironment
from conans.tools import download, unzip
import os

class ChakraCoreConan(ConanFile):
    name = "ChakraCore"
    version = "1.4.1"
    ZIP_FOLDER_NAME = "ChakraCore-%s" % version
    settings = {"os": ["Windows"],
        "compiler": {"Visual Studio": {"version": ["12", "14"], "runtime" : None }},
        "arch": None,
        "build_type": None}
    exports = ["FindChakraCore.cmake"]
    build_policy = "missing"
    url="https://github.com/lhcorralo/conan-chakracore"
    license="https://github.com/Microsoft/ChakraCore/blob/master/LICENSE.txt"
    description="ChakraCore test Conan package"
    short_paths=True
        
    def config(self):
        pass

    def source(self):
        # The file is extracted from github
        zip_name = "v%s.tar.gz" % self.version
        download("https://github.com/Microsoft/ChakraCore/archive/%s" % zip_name, zip_name, verify=True)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
    
        self.output.info("ChakraCore build:")
        self.output.info("arch %s" % self.settings.arch)
        
        # Use msbuild in Windows, and cmake in linux and macos
        env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
        # Set options:
        msbuild_options="/m"
        # Available platforms: x86, x64 and arm
        if (self.settings.arch == "x86"):
            msbuild_options += " /p:Platform=x86"
        elif (self.settings.arch == "x86_64"):
            msbuild_options += " /p:Platform=x64"
        elif (self.settings.arch == "arm"):
            msbuild_options += " /p:Platform=arm"
        else:
            self.output.error("Invalid arch %s" % self.settings.arch)
        # Available configurations: Debug, Release and Test. Debug and Release are used
        msbuild_options += (" /p:Configuration=%s" % self.settings.build_type)
        # Link static runtime
        if(self.settings.compiler.runtime == "MT" or self.settings.compiler.runtime == "MTd"):
            msbuild_options += " /p:RuntimeLib=static_library"
        # Launch build process
        command = ('%s && cd %s && msbuild %s Build\\Chakra.Core.sln' \
            % (env.command_line_env, self.ZIP_FOLDER_NAME, msbuild_options))
        self.run(command)

    def package(self):
        # Copy CARESConfig.cmake to package
        self.copy("FindChakraCore.cmake", dst=".", src=".", keep_path=False)
        
        # Copying headers
        headerFiles = ['ChakraCore.h', 'ChakraCommon.h', 'ChakraCommonWindows.h', 'ChakraDebug.h']
        headerDir = self.ZIP_FOLDER_NAME + "\\lib\\Jsrt"
        for headerFile in headerFiles:
            self.copy(pattern=headerFile, dst="include", src=headerDir, keep_path=False)
        
        # Copying static and dynamic libs
        buildDir = self.ZIP_FOLDER_NAME + "\\Build\\VCBuild\\bin"
        self.output.info("buildDir? %s" % buildDir)
		# Looking the files by its exact name seems to fail
        self.copy(pattern="*Core.lib", dst="lib", src=buildDir, keep_path=False)
        self.copy(pattern="*Core.dll", dst="bin", src=buildDir, keep_path=False)
        self.copy(pattern="*Core.pdb", dst="bin", src=buildDir, keep_path=False)

    def package_info(self):
        # Define the libraries
        self.cpp_info.libs = ['ChakraCore']
